import random
import time

responses = ["Yes", "No", "Maybe", "Ask again later"]

print("🔮 Welcome to the Magic 8-Ball!")

while True:
    question = input("\nAsk a yes/no question (or type 'quit' to stop): ")
    if question.strip().lower() in ("quit", "exit"):
        print("Goodbye! 👋")
        break
    print("Thinking...")
    time.sleep(1)
    print("🎱", random.choice(responses))

