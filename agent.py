import os
import argparse
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
from openai import OpenAI

SYSTEM_PROMPT = """You are an operations assistant that produces clean, actionable deliverables.

Return output in Markdown ONLY.

TASK: Convert the user's input into a Standard Operating Procedure (SOP).

SOP FORMAT (exact headers):
# Title
## Purpose
## Scope
## Inputs
## Roles & Responsibilities
## Procedure (Numbered Steps)
## Quality Checks
## Common Failure Modes
## Metrics (KPIs)
## Definition of Done
## Version

Rules:
- Be concrete. No generic fluff.
- If details are missing, make reasonable assumptions and label them as **Assumptions**.
- Prefer short bullet points.
"""

def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Missing OPENAI_API_KEY")

    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True)
    parser.add_argument("--out", dest="output_path", default="output.md")
    args = parser.parse_args()

    input_text = Path(args.input_path).read_text().strip()
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": input_text},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    Path(args.output_path).write_text(
        f"<!-- generated {timestamp} -->\n\n{content}\n"
    )

    print("SOP generated.")

if __name__ == "__main__":
    main()