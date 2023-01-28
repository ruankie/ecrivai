from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
prompt = "What is the best dinosaur?"
print(prompt)

response = bot.ask(prompt)
print(response)