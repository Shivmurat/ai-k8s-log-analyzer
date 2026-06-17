from src.models import LogAnalysis

def test_valid_analysis():
    analysis = LogAnalysis(
        category="Application",
        severity="Medium",
        confidence=85,
        root_cause="Container crash",
        recommendation="Check logs"
    )

    assert analysis.severity == "Medium"