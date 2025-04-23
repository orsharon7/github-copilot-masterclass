# Step-by-Step Guide

## Step 1: Initial Application Setup
Use the following initial prompt in GitHub Copilot Agent Mode:

**Prompt (include `chat.png`!):**
```prompt
Generate a basic Python Flask application based on the image. The app should enable a chat interaction styled similarly to the provided image, simulating a conversation with Steve Jobs.
```
<div align="center">
    <img src="media/Initial_Chat.png" alt="Final App" />
    </br>
</div>


- When Copilot asks for an empty workspace, use the predefined action to create a `chat` directory and continue.
- After Copilot finishes coding the initial chat app, explore the different files and run the application. The result should look similar to this:

<div align="center">
    <img src="media/Initial_Chat_Steve.png" alt="Initial Chat" width="600"/>
</div>

## Step 2: Setting Up GitHub Copilot Agent Instructions

To enhance GitHub Copilot's responses specifically for this workshop, copy the file [copilot-instructions.md](/copilot-instructions.md) to the `.github` directory.

GitHub Copilot will automatically begin following these custom instructions, improving accuracy and relevance.

Now let's refine our application's UI:

**Prompt (include `chat.png` again):**
```prompt
Improve the page content, style, and layout based on the provided image. Ensure the chat window dynamically adapts to browser size. Add steve and user image to the user picture from the media directory. Overall I aim for a cleaner interface. Ensure Enter is send.
```
Run the Flask application to verify the interface updates are applied correctly.


## Step 3: Real-Time Chat with Azure OpenAI

GitHub Copilot offers multiple models for writing code. Click on GPT-4o and explore the different offerings:

![Github Copilot Models](media/Copilot-Models.png)

Now switch to `Claude 3.7 Sonnet` and use the following prompt:

**Prompt:**
```prompt
Integrate real-time chat functionality into the existing Flask application using Azure OpenAI's GPT-4o. Utilize the latest openai Python package to interact with Azure OpenAI. Ensure the integration supports streaming responses for a seamless user experience. Handle authentication using Azure OpenAI credentials and manage API requests appropriately.
```

Complete the `.env` file created in the root directory by replacing the placeholder values with your actual Azure OpenAI details. 
**Note:** Ensure the deployment name and API versions are correct.

Install dependencies, run the application, and test GPT-4o in real-time:

<div align="center">
    <img src="media/chat_vid.gif" alt="Chat" width="600"/>
</div>

## Next Modules

1. [Learn About Github Copilot](docs/01-explore-github-copilot.md)
2. [Creating MCP Server](docs/03-creating-mcp-server.md)
