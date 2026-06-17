from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal

class LogAnalysis(BaseModel):
    model_config = {"extra": "forbid"}
    category: Literal[
        "Network",
        "Image",
        "Memory",
        "Application",
        "Unknown"
    ]
    confidence: int = Field(ge=0, le=100)
    root_cause: str
    severity: Literal["Low", "Medium", "High", "Critical"]
    recommendation: str


class AnalysisResult(BaseModel):
    model: str
    analysis_time: datetime
    analysis: LogAnalysis