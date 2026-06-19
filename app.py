import os
import gradio as gr
import requests
import pandas as pd
from typing import Dict, List


# custom imports
from agents import Agent
from tool import get_tools
from model import get_model


# question processing
async def process_question(agent, question: str, task_id: str):
    """
    process a single question and return both answer and full log entry
    """
    try:
        answer = agent(question)
        return {
            "submission": {"task_id": task_id, "submitted_answer": answer},
            "log": {
                "Task ID": task_id,
                "Question": question,
                "Submitted Answer": answer,
            },
        }

    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        return {
            "submission": {"task_id": task_id, "submitetd_answer": error_msg},
            "log": {
                "Task ID": task_id,
                "Question": question,
                "Submitted Answer": error_msg,
            },
        }


async def run_questions_async(agent, questions_data: List[Dict]) -> tuple:
    pass
