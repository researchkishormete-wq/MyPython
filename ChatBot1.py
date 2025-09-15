#Simple chatbot
name = input("What's your name? ")
print(f"Hello, {name}! I'm your friendly chatbot.")
feeling = input("How are you today? ")
print("That's good to hear!" if "good" in feeling else "Hope you feel better soon!")
