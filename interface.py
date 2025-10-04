from model_loader import ModelLoader
from chat_memory import ChatMemory

def build_prompt(memory, user_input):
    
    user_input_clean = user_input.strip()
    context = memory.get_context()
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if any(user_input_clean.lower().startswith(greet) for greet in greetings):
        prompt = (
            "You are a polite and friendly assistant. Respond naturally and briefly.\n\n"
            f"Previous conversation: {context}\n"
            f"User: {user_input_clean}\n"
            "Assistant:"
        )
    else:
        prompt = (
           "You are a knowledgeable and factual assistant. "
            "Always provide the *official and correct factual answer* in one short sentence. "
            "For example, if asked for a country's capital, give the official capital city only. "
            "Example:\n"
            "Q: What is the capital of Switzerland?\nA: Bern.\n"
            "Q: What is the capital of United States of America?\nA: Washington, D.C.\n"
            "Q: Who won the FIFA World Cup 2022?\nA: Argentina.\n\n"
            f"Previous conversation: {context}\n"
            f"Q: {user_input_clean}\nA:"
        )

    return prompt


def main():
    print("Chatbot (type /exit to quit)\n")

    model = ModelLoader()
    memory = ChatMemory(max_turns=3)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["/exit", "/quit"]:
            print("Exiting chatbot...")
            break

        prompt = build_prompt(memory, user_input)
        bot_reply = model.generate(prompt)

        bot_reply = bot_reply.replace("Assistant:", "").replace("A:", "").replace("bot:", "").strip()

        print(f"Bot: {bot_reply}\n")

        memory.add_message("user", user_input)
        memory.add_message("bot", bot_reply)


if __name__ == "__main__":
    main()
