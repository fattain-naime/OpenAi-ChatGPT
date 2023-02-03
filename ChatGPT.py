import openai

def chat_with_gpt(api_key, username):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Hi, my name is {username}. How can I help you today?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    print(message)

    while True:
        user_input = input(f"{username}: ")
        if user_input.lower() == "exit":
            break

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{username}: {user_input}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = response.choices[0].text
        print(f"GPT-3: {message}")

if __name__ == "__main__":
    api_key = input("Enter your OpenAI API key: ")
    username = input("Enter your name: ")
    chat_with_gpt(api_key, username)
