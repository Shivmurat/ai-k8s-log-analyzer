import pytest

from src.models import LogAnalysis

def test_valid_analysis():
    analysis = LogAnalysis(
        category="Application",
        severity="Medium",
        confidence=85,
        root_cause="Container crash",
        recommendation="Check logs"
    )
    assert analysis.confidence == 85


def test_invalid_confidence():
    with pytest.raises(Exception):
        LogAnalysis(
            category="Application",
            confidence=150,
            root_cause="Container crash",
            severity="Medium",
            recommendation="Check logs"
            )