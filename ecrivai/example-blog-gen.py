from topic_selector import TopicSelector
from content_generator import ContentGenerator


def main():
    # get topic
    ts = TopicSelector()
    topic = ts.select_topic()

    # generate content body
    cgen = ContentGenerator()
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
