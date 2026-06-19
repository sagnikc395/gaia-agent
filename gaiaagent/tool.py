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


def get_tools() -> List[Tool]:
    # return a list of available tools for the agent 
    tools = [
        FinalAnswerTool(),
        DuckDuckGoSearchTool(),
        PythonInterpreterTool(),
        WikipediaSearchTool(),
        VisitWebpageTool(),
    ]
    
    return tools 