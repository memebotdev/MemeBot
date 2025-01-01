import os
import sys

# So that we can do `import MEMEBOTai in our tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import MEMEBOTai # noqa: E402

MEMEBOT.api_base = os.getenv("MEMEBOT_API_BASE")  # type: ignore
MEMEBOT.api_key = os.getenv("MEMEBOT_API_KEY")  # type: ignore
