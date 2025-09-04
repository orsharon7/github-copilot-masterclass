"""
Flask application for chat interface with Azure OpenAI GPT-4o integration.
"""
import os
import logging
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from openai import AzureOpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Azure OpenAI configuration
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

@app.route('/')
def home():
    """
    Render the home page with chat interface.
    
    Returns:
        rendered HTML template
    """
    try:
        logger.info("Home page accessed")
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        return jsonify({"error": "Failed to load the application"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """
    Process chat request and return response.
    
    Returns:
        JSON response or streaming response
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            logger.warning("Invalid request data")
            return jsonify({"error": "Invalid request"}), 400
        
        user_message = data['message']
        logger.info(f"Received message: {user_message}")
        
        # Check if streaming is requested
        stream = data.get('stream', False)
        
        if stream:
            return Response(
                stream_with_context(generate_streaming_response(user_message)),
                content_type='text/event-stream'
            )
        else:
            response = generate_response(user_message)
            return jsonify({"response": response})
            
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        return jsonify({"error": "Failed to process your request"}), 500

def generate_response(message):
    """
    Generate response using Azure OpenAI GPT-4o.
    
    Args:
        message (str): User's message
        
    Returns:
        str: Response from GPT-4o
    """
    try:
        # Set the system message to simulate Steve Jobs' persona
        system_message = "You are Steve Jobs. Respond in his unique style - visionary, direct, passionate about design and innovation."
        
        # Call Azure OpenAI API
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ],
            max_tokens=150
        )
        
        # Extract and return the response content
        content = response.choices[0].message.content
        logger.info(f"Generated response: {content}")
        return content
        
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return "Sorry, I'm having trouble connecting right now. Please try again later."

def generate_streaming_response(message):
    """
    Generate streaming response using Azure OpenAI GPT-4o.
    
    Args:
        message (str): User's message
        
    Yields:
        str: Chunks of response from GPT-4o
    """
    try:
        # Set the system message to simulate Steve Jobs' persona
        system_message = "You are Steve Jobs. Respond in his unique style - visionary, direct, passionate about design and innovation."
        
        # Call Azure OpenAI API with streaming enabled
        stream = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            stream=True
        )
        
        # Yield data in SSE format
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                yield f"data: {content}\n\n"
                
    except Exception as e:
        logger.error(f"Error generating streaming response: {str(e)}")
        yield f"data: Sorry, I'm having trouble connecting right now. Please try again later.\n\n"

if __name__ == '__main__':
    # Verify environment variables are set
    required_env_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set these in your .env file")
    else:
        logger.info("Starting Flask application")
        app.run(debug=True, host='0.0.0.0', port=5001)