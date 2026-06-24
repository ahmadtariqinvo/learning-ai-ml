from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Llama-3.3-70B-Instruct",
    token="***"

messages = []

print("Chat started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat_completion(
        messages=messages,
        max_tokens=512,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    print("\nAI:", assistant_reply, "\n")

    messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    print(messages)