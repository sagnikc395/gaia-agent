from dataclasses import dataclass


@dataclass(frozen=True)
class GAIAAgentConfig:
    API_URL = "https://agentsc-course-unit4-scoring.hf.space"

    ## model config
    # since using groq,using gpt-oss-120b for inference
    MODEL_ID = "openai/gpt-oss-120b"

    ## max retries for
    MAX_RETRY = 5


config = GAIAAgentConfig()
