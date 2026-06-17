import argparse
from pathlib import Path

from src.analyzer import LogAnalyzer

parser = argparse.ArgumentParser()
parser.add_argument("log_file", help="Path to Kubernetes log file")
args = parser.parse_args()
log_file = Path(args.log_file)

analyzer = LogAnalyzer()

result = analyzer.analyze(log_file.read_text())
analysis = result.analysis

print(f"model: {result.model}")
print(f"time: {result.analysis_time}")
print(f"Category: {analysis.category}")
print(f"severity: {analysis.severity}")
print(f"confidence: {analysis.confidence}%")
print(f"root_cause: {analysis.root_cause}")
print(f"recommendation: {analysis.recommendation}")