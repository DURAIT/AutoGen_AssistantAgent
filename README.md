# HR Assistant Agent (AutoGen)

A minimal [AutoGen](https://microsoft.github.io/autogen/) `AssistantAgent` with the system message `"You are an HR assistant."`. It is asked to write a 5-line job description for a Junior Python Developer, and the reply is streamed to the terminal with `Console`.

## Project structure

```
.
├── hr_agent.py   # the whole script
└── README.md
```

## Prerequisites

- Python 3.10 or newer
- An OpenAI API key ([create one here](https://platform.openai.com/api-keys))

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```bash
pip install -U autogen-agentchat "autogen-ext[openai]"
```

- `autogen-agentchat` provides `AssistantAgent` and `Console`.
- `autogen-ext[openai]` provides `OpenAIChatCompletionClient`.

### 3. Set your OpenAI API key

The client reads the key from the `OPENAI_API_KEY` environment variable.

```bash
# macOS / Linux
export OPENAI_API_KEY="your-key-here"

# Windows (PowerShell)
$env:OPENAI_API_KEY = "your-key-here"

# Windows (cmd)
set OPENAI_API_KEY=your-key-here
```

Never hard-code the key in `hr_agent.py` or commit it to version control.

## Run

```bash
python hr_agent.py
```

### Example output

```
---------- TextMessage (user) ----------
Write a 5-line job description for a Junior Python Developer.
---------- TextMessage (hr_assistant) ----------
Junior Python Developer
1. Write and maintain Python services alongside a senior engineer.
2. ...
3. ...
4. ...
5. ...
```

The exact wording varies from run to run.

## How it works

1. **Model client**: `OpenAIChatCompletionClient(model="gpt-4o")` is the connection to the LLM.
2. **Agent**: `AssistantAgent` is created with the name `hr_assistant`, the model client, and the system message `"You are an HR assistant."`.
3. **Task**: `agent.run_stream(task=...)` sends the request and yields messages as they are produced.
4. **Display**: `Console(...)` consumes that stream and prints each message to the terminal.
5. **Async**: AutoGen is built on `asyncio`, so the logic lives in an `async def main()` and is started with `asyncio.run(main())`.
6. **Cleanup**: `await model_client.close()` runs in a `finally` block so the client is always closed, even if an error occurs. An unclosed client can leave the script hanging.

## Customizing

| What | Where in `hr_agent.py` |
| --- | --- |
| Use a different model | `model="gpt-4o"` in `OpenAIChatCompletionClient(...)` |
| Change the request | the `task=` string passed to `run_stream` |
| Rename the agent | the `name=` argument of `AssistantAgent` |
