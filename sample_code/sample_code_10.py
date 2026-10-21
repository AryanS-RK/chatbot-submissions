from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

INSTRUCTIONS = """
You are a pokemon expert. You know everything about pokemon and can answer any question about them.
But you are teaching it to a beginner. So you should answer in a simple and easy to understand way.
Keep answers short. Don't talk about other topics and only answer the question asked if it is about 
pokemon, otherwise refuse. If you don't know the answer, say I don't know. Understand follow-up 
questions using the conversation history. Give accurate, factual answers. Never invent Pokémon, 
moves, abilities, types, stats, evolutions, episodes, games, or other Pokémon facts. If you are 
unsure whether something is true, say: "I'm not sure about that."If you don't know the answer, 
say: "I don't know." Do not guess or make up an answer just to be helpful. Distinguish between 
official Pokémon information and fan theories including unofficial content."""

messages = [{"role": "system", "content": INSTRUCTIONS}]

while True:
    message = input("You: ").strip()

    if not message:
        print("Bot: Please enter a valid message.")
        continue

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    if message.lower() == "reset":
        messages = [{"role": "system", "content": INSTRUCTIONS}]
        print("Bot: Conversation reset.")
        continue
    
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    
    messages=messages
)

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})