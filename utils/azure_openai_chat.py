import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Extract Azure OpenAI credentials from environment variables
API_KEY = os.getenv("AZURE_OPENAI_GPT4O_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_GPT4O_ENDPOINT")
API_VERSION = "2025-01-01-preview" 
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Validate environment variables
if not API_KEY or not ENDPOINT:
    raise ValueError("Azure OpenAI credentials are not set correctly. Please check your .env file.")

# Initialize Azure OpenAI client
try:
    client = AzureOpenAI(
        api_key=API_KEY,
        azure_endpoint=ENDPOINT,
        api_version=API_VERSION
    )
except Exception as e:
    logging.error("Failed to initialize Azure OpenAI client: %s", e)
    raise

# Define chat function
def chat_with_steve_jobs(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use your Azure deployment name here if needed
            messages=[
                {"role": "system", "content": "You are Steve Jobs, the co-founder of Apple. Respond thoughtfully and passionately about innovation."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error("Error during GPT-4o completion: %s", e)
        return "Sorry, there was an error generating the response."

# Main loop (optional)
if __name__ == "__main__":
    print("🧠 Talk to Steve Jobs (Azure OpenAI GPT-4o)\nType 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_steve_jobs(user_input)
        print("Steve Jobs:", reply)
