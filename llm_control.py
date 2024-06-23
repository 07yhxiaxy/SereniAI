from openai import OpenAI
def generate_action(user_emotion, target_emotion):
    # Initialize the OpenAI client with your API key
    API_KEY = "OPENAI KEY HERE"
    client = OpenAI(api_key=API_KEY)
    # Function to create a prompt with the desired formatting
    def create_prompt(question):
        return [
            {"role": "system", "content": "You are an AI assistant helping a user to achieve the target emotion. You have limited output actions, they include: magnitude--'soft, medium, hard' and movement--'slap, squeeze, pat, tickle, jab'. You only need to provide the action (magnitude and movement) and reasoning. For example, if i am upset and I want to be happy, you should output:'magnitude: soft, movement: pat, reason: because soft pat comfort human's feeling and show caring' "},
            {"role": "user", "content": question}
        ]
    # Get user input from the terminal
    user_question = 'I am ' + user_emotion + ' and I want to be ' + target_emotion + '.'
    # Create the prompt with the user's question
    messages = create_prompt(user_question)
    # Use the API to get a completion
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )
    # Print the response
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content