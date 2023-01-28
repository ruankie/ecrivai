"""
Generates the main body of the blog 
based on a topic.
"""

import logging

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


class ContentGenerator:
    def __init__(self, bot=None) -> None:
        self.bot = bot
        self.content_body: str = ""

    def _revise_with_keywords(self, keywords: list[str]) -> str:
        """Revise content body by using the given keywords."""
        logger.info(f"Revising body by injecting keywords: {keywords}...")
        prompt = (
            f"Now revise the content by using these keywords: {', '.join(keywords)}"
        )
        response = self.bot.ask(prompt)
        return response

    def _to_markdown_format(self) -> str:
        """Revise content body by reformatting using markdown."""
        logger.info("Reformatting body to markdown...")
        prompt = f"Now give it in markdown format"
        response = self.bot.ask(prompt)
        return response

    def _get_initial_content_body(
        self, topic: str, sections: int, word_count: int
    ) -> str:
        """Get initial content body from ChatGPT."""
        logger.info("Generating initial content body...")
        prompt = f'Write a {word_count} word blog post in {sections} sections on the topic "{topic}"'
        response = self.bot.ask(prompt)
        return response

    def get_content_body(
        self,
        topic: str,
        word_count: int = 800,
        sections: int = 5,
        use_keywords: list[str] = [],
        as_markdown: bool = True,
    ) -> str:
        """
        Return the content of the blog.

        Args:
            sections (int): Number of sections in the blog.
            use_keywords (list[str]): A list of keywords to use in the body.
            as_markdown (bool): Whether to return in markdown format.
            
        Returns:
            str: The body of the blog broken down into sections.
        """
        self.content_body = self._get_initial_content_body(
            topic=topic, sections=sections, word_count=word_count
        )
        if len(use_keywords) > 0:
            self.content_body = self._revise_with_keywords(use_keywords)
        if as_markdown:
            self.content_body = self._to_markdown_format()
        return self.content_body
