from topic_selector import TopicSelector
from bot_session import ChatGPTSession


def main():
    session = ChatGPTSession()
    ts = TopicSelector(bot=session.bot)
    topic = ts.select_topic()
    print("TOPIC:")
    print(topic)


if __name__ == "__main__":
    main()
