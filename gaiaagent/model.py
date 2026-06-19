import os
from typing import Any

from smolagents import LiteLLMModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from functools import lru_cache

from litellm import RateLimitError
from .config import MAX_RETRY
#from groq import Groq 

from dotenv import load_dotenv

import time

import re 



load_dotenv()

class LocalTransformersModel:
    def __init__(self, model_id: str, **kwargs):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
        self.pipeline = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )

    def __call__(self, prompt: str, **kwargs):
        outputs = self.pipeline(prompt, **kwargs)
        return outputs[0]["generated_text"]


class WrapperLiteLLMModel(LiteLLMModel):
    def __call__(self, messages, **kwargs):
        for attempt in range(MAX_RETRY):
            try:
                return super().__call__(messages, **kwargs)
            except RateLimitError as e:
                print(f"RateLimitError (attempt {attempt + 1}/{MAX_RETRY})")

                # try to extract retry time from the exception string
                # kinda hacky, need to improve 
                match = re.search(r'"retryDelay": ? "(\d+)s"', str(e))
                retry_seconds = int(match.group(1)) if match else 50

                print(f"Retrying after {retry_seconds} s ...")
                time.sleep(retry_seconds)

        raise RateLimitError(f" ERROR: Rate limit exceeded after {MAX_RETRY} retires.")

# cache the local model    
@lru_cache(maxsize=1)
def get_lite_llm_model(model_id: str, **kwargs) -> WrapperLiteLLMModel:
    # return a LiteLLM model instance 
    return WrapperLiteLLMModel(model_id=model_id,api_key=os.getenv("GROQ_API_KEY"),**kwargs)


@lru_cache(maxsize=1)
def get_local_model(model_id: str, **kwargs) -> LocalTransformersModel:
    # return a local transformer modle 
    return LocalTransformersModel(model_id=model_id,**kwargs)

def get_model(model_type: str, model_id: str, **kwargs):
    # return a model instance based on the specified type
    
    models: dict[str,callable[..., Any]] = {
        "LiteLLMModel": get_lite_llm_model,
        "LocalTransformerModel": get_local_model,
    }
    
    if model_type not in models:
        raise ValueError(f"Unknown model type: {model_type}")

    return models[model_type](model_id,**kwargs)