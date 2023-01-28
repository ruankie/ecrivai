import os
from topic_selector import TopicSelector
from content_generator import ContentGenerator
from bot_session import ChatGPTSession

CONTENT_PATH = "../content"


def main():
    # set up dir
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # start session
    session = ChatGPTSession()

    # select topic
    ts = TopicSelector(bot=session.bot)
    topic = ts.select_topic()

    # generate body
    cgen = ContentGenerator(bot=session.bot)
    body = cgen.get_content_body(
        topic=topic, word_count=800, sections=4, use_keywords=[], as_markdown=True,
    )

    # show content
    print(body)

    # save content to markdown file
    md_file_name = topic.lower().strip().replace(" ", "_").replace(".", "")
    md_file_name = md_file_name[:25] + ".md"
    md_file_path = os.path.join(CONTENT_PATH, md_file_name)
    with open(md_file_path, "w") as f:
        f.write(body)


if __name__ == "__main__":
    main()
