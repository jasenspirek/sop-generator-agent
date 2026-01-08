# SOP Generator Agent

CLI-based AI agent that converts messy process descriptions into clean, structured SOPs.

## Setup
1. Create a `.env` file in the repo root:
   ```text
   OPENAI_API_KEY=your_key_here
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run
```bash
python agent.py --in examples/input.txt --out examples/output.md
```

## Notes
- The `.env` file is intentionally ignored and should never be committed.
- Output files can be regenerated at any time.
