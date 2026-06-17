import json
from datetime import datetime

from ollama import chat

from src.models import LogAnalysis, AnalysisResult
from src.prompts import K8S_ANALYZER_PROMPT


class LogAnalyzer:

    def __init__(self, model="qwen2.5:latest"):
        self.model = model


    def _generate(self, log_text: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {"role": "system", "content": K8S_ANALYZER_PROMPT},
                {"role": "user", "content": log_text}
            ]
        )

        return response.message.content


    def analyze(self, log_text: str) -> AnalysisResult:

        try:
            analysis = LogAnalysis.model_validate(json.loads(self._generate(log_text)))
            return AnalysisResult(
                model=self.model,
                analysis_time=datetime.now(),
                analysis=analysis
            )
        except Exception as e:
            raise RuntimeError(f"Failed to parse AI response: {e}")