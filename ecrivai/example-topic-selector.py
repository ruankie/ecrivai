from topic_selector import TopicSelector


def main():
    ts = TopicSelector()

    topic = ts.select_topic()
    print("TOPIC:")
    print(topic)


if __name__ == "__main__":
    main()
