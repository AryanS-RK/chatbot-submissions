previous_response_id = None

while True:
    message = input("You: ").strip()

    if not message:
        print("Bot: Please type something.")
        continue

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    if message.lower() == "reset":
        previous_response_id = None
        print("Bot: Conversation reset.")
        continue

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message,
        previous_response_id=previous_response_id
    )

    print("Bot:", response.output_text)

    previous_response_id = response.id