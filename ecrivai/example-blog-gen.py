from topic_selector import TopicSelector
from content_generator import ContentGenerator
from bot_session import ChatGPTSession


def main():
    # start session
    session = ChatGPTSession()

    # select topic
    ts = TopicSelector(bot=session.bot)
    topic = ts.select_topic()

    # generate body
    cgen = ContentGenerator(bot=session.bot)
    body = cgen.get_content_body(
        topic=topic, 
        word_count=800, 
        sections=4, 
        use_keywords=[], 
        as_markdown=False,
    )

    # show content
    print(body)

    # TODO save content to markdown file


if __name__ == "__main__":
    main()
