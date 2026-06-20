# getter for tools 

from typing import List 
from smolagents import (
    DuckDuckGoSearchTool,
    PythonInterpreterTool, 
    Tool,
    VisitWebpageTool,
    WikipediaSearchTool,
    FinalAnswerTool
)

from .tools.describe_image import DescribeImageTool
from .tools.openai_speech_to_text import OpenAISpeechToTextTool
from .tools.read_file import ReadFileTool
from .tools.table_extractor import TableExtractorTool
from .tools.youtube_transcription import YouTubeTranscriptionTool


def get_tools() -> List[Tool]:
    # return a list of available tools for the agent 
    tools = [
        FinalAnswerTool(),
        DuckDuckGoSearchTool(),
        PythonInterpreterTool(),
        WikipediaSearchTool(),
        VisitWebpageTool(),
        ReadFileTool(),
        TableExtractorTool(),
        OpenAISpeechToTextTool(),
        YouTubeTranscriptionTool(),
        DescribeImageTool(),
    ]
    
    return tools 
