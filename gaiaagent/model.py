import os

from smolagents import LiteLLMModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from functools import lru_cache

from litellm import RateLimitError


class LocalTransformersModel:
    def __init__(self, model_id: str, **kwargs):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
        self.pipelien = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )
