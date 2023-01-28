"""Selects an interesting topic for a blog post."""

"""
Some keywords to use while looking for a good topic:
- high search volume
- low competition
"""
import logging
import random
from chatgpt_wrapper import ChatGPT

# set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class TopicSelector:
    def __init__(self) -> None:
        self.topic: str = None

    def _get_potential_topics(
        self, prompt: str = "list 5 random topics to write a blog about"
    ) -> list[str]:
        """
        Return a list of potential topics to write a blog about. 
        Optionally, provide a custom prompt to, for example,
        include specific keywords or sub-topics.
        """
        logger.info("Connecting to ChatGPT...")
        bot = ChatGPT()

        logger.info(f"Getting initial topics with prompt: {prompt}")
        response = bot.ask(prompt)

        logger.info("Cleaning response...")
        try:
            initial_topics = response.split("\n")
        except Exception as ex:
            logger.warning(f"Exception during cleaning of response: {ex}")
            initial_topics = []

        # remove numbers if list is numbered
        starts_with_and_dot = initial_topics[0].split(". ")[0].isnumeric()
        starts_number = initial_topics[0].split(" ")[0].isnumeric()
        if starts_number:
            logger.info("Found numbered list. Removing numbers...")
            initial_topics = [topic.split(" ")[1:] for topic in initial_topics]
        elif starts_with_and_dot:
            logger.info("Found numbered list with periods. Removing numbers...")
            initial_topics = [topic.split(". ")[1:] for topic in initial_topics]
        else:
            logger.info(f"Topic list not numbered. Continuing...")

        # exclude last empty line
        return initial_topics[:-1]

    def select_topic(self) -> str:
        """Returns a topic to blog about."""
        logger.info("Attempting to gather a list of random topics...")
        potential_topics = self._get_potential_topics()
        logger.info("Selecting random topic from list of potential topics...")
        self.topic = random.choice(potential_topics)
        logger.info(f"Selected topic: {self.topic}")
        return self.topic
