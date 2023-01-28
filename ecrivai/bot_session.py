"""Handles ChatGPT session."""

import logging
from chatgpt_wrapper import ChatGPT

# set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a stream handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class ChatGPTSession:
    def __init__(self) -> None:
        """Start new ChatGPT session."""
        logger.info("Connecting to ChatGPT...")
        self.bot = ChatGPT()
