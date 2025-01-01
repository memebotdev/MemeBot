# MEMEBOT Python SDK

[![PyPI version](https://img.shields.io/pypi/v/MEMEBOT.svg)](https://pypi.org/project/MEMEBOTai)

The MEMEBOT Python SDK provides convenient access to the MEMEBOT REST API from any Python 3.8+
application. The SDK includes rich type definitions and enables receiving real-time executions
via WebSockets.

## Documentation

Full documentation of the SDK is available at [https://MEMEBOT.ai/docs/sdk/introduction](https://MEMEBOT.ai/docs/sdk/introduction). You may also want to check out the [REST API Reference](https://MEMEBOT.ai/docs/api/v1/introduction).

## Installation

You can install the SDK via `pip`:

```bash
pip install MEMEBOTai```

## Usage

Once installed, you can use it to make requests.

### Create an Agent

```python
import MEMEBOTai
MEMEBOT.api_key = "YOUR_API_KEY"

agent = MEMEBOT.Agent.create(
    name="My Agent",
    script="def main(request):\n    return request.payload",
    requirements="requests==2.31.0\npandas==2.1.4",
    env_vars="FOO=bar\nBAZ=qux",
    python_version="3.11",
)
```

### Execute an Agent

```python
import MEMEBOTai
MEMEBOT.api_key = "YOUR_API_KEY"

agent = MEMEBOT.Agent.retrieve(id="15d19ca3-26f1-4adb-9cea-3955b73d9b4e")

execution = agent.execute(payload={"key": "value"})
```

These are only a few examples of what you can do with the SDK. Refer to the [full documentation](https://MEMEBOT.ai/docs/sdk/introduction) to learn more about the SDK.
