from typing import Any, List, Optional

from smolagents import CodeAgent
from logger import get_logger

import time

# logger init
logger = get_logger(__name__)

from config import config


class Agent:
    # wraps a CodeAgent and provides a callable interface for answering questions.

    def __init__(
        self,
        model: Any,
        tools: Optional[List[Any]] = None,
        prompt: Optional[str] = None,
        verbose: bool = False,
    ) -> None:
        logger.info("Initializing Agent")
        self.model = model
        self.tools = tools
        self.verbose = verbose
        # fill the imports with the things
        self.imports = [
            "pandas",
            "numpy",
            "os",
            "requests",
            "tempfile",
            "datetime",
            "json",
            "time",
            "re",
            "openpyxl",
            "pathlib",
            "sys",
        ]
        self.agent = CodeAgent(
            model=self.model,
            tools=self.tools,
            add_base_tools=True,
            additional_authorized_imports=self.imports,
        )

        self.final_answer_check = [check_reasoning, ensure_formatting]
        self.base_prompt = prompt
        self.prompt_templates = get_prompt_templates()
        logger.info("Agent initialized")

    def __call__(self, question: str, files: List[str] = None) -> str:
        # main interface that logs inputs/outputs and handles the timing
        if self.verbose:
            print(f"Agent received question: {question[:50]} ... with files: {files}")

        time.sleep(25)
        return self.answer_question(question, files[0] if files else None)

    def answer_question(
        self, question: str, task_file_path: Optional[str] = None
    ) -> str:
        # process a GAIA benchmark question with optional file context.

        try:
            context = self._build_context(question, task_file_path)
            full_prompt = self.base_prompt.format(context=context)

            if self.verbose:
                print(f"Generated prompt: {full_prompt[:200]} ...")
            answer = self.agent.run(full_prompt)
            return self._clean_answer(str(answer))

        except Exception as e:
            logger.error(f"Error processing question: {str(e)}")
            return f"ERROR: {(str(e))}"

    def _build_context(self, question: str, file_path: Optional[str]) -> str:
        # construct the context section based on question and file
        context_lines = [f"QUESTION: {question}"]

        if file_path:
            context_lines.append(
                f"FILE: Available at {config.API_URL}/files/{file_path}\n"
                "Use appropriate tools to analyze this file if needed"
            )

        # handle reversed text questions
        if self._is_reversed_text(question):
            context_lines.append(
                f"NOTE: This question contains reversed text. "
                f"Original: {question}\nReversed: {question[::-1]}"
            )
        return "\n".join(context_lines)

    def _is_reversed_text(self, text: str) -> bool:
        pass

    def _clean_answer(self, answer: str) -> str:
        # clean the raw answer to match the GAIA requirements
        # remove the common prefixes/ suffixes
        for prefix in ["Final Answer:", "Answer:", "=>"]:
            if answer.startswith(prefix):
                answer = answer[len(prefix) :]

        # remove the quotes and whitespaces
        answer = answer.strip(" '\"")

        # special handling for reversed answers
        if self._is_reversed_text(answer):
            return answer[::-1]

        return answer
