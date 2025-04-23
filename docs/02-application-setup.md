# Building Your Chat Application with GitHub Copilot

This guide will walk you through creating an interactive chat application using GitHub Copilot, Flask, and Azure OpenAI integration. By the end of this module, you'll have a functional chat interface that simulates a conversation with Steve Jobs.

## Step 1: Initial Application Setup

Let's start by creating a basic Flask application that simulates a chat interface:

**Prompt for GitHub Copilot Agent Mode (include `chat.png`!):**
```prompt
Generate a basic Python Flask application based on the image.
The app should enable a chat interaction styled similarly to the provided image, simulating a conversation with Steve Jobs.
```
<div align="center">
    <img src="../media/Initial_Chat.png" alt="Final App" />
    </br>
</div>

### Key Instructions:
- When Copilot asks for an empty workspace, use the predefined action to create a `chat` directory and continue.
- Let Copilot generate the necessary files for the application, including Flask routes, HTML templates, and static assets.
- After Copilot finishes coding the initial chat app, explore the different files to understand the structure.
- Run the application with `flask run` or `python app.py` to see your basic chat interface.

Your initial chat application should look similar to this:

<div align="center">
    <img src="../media/Initial_Chat_Steve.png" alt="Initial Chat" width="600"/>
</div>

## Step 2: Setting Up GitHub Copilot Agent Instructions

To make GitHub Copilot more effective for this specific project, we'll customize its instructions:

1. Create a `.github` directory in your project root if it doesn't exist already
2. Copy the file [copilot-instructions.md](/copilot-instructions.md) to the `.github` directory

These custom instructions will guide Copilot to provide more relevant and specialized assistance throughout the workshop.

### Improving the UI

Now let's enhance the visual design of our application:

**Prompt for GitHub Copilot (include `chat.png` again):**
```prompt
Improve the page content, style, and layout based on the provided image.
Ensure the chat window dynamically adapts to browser size.
Add steve and user image to the user picture from the media directory.
Overall I aim for a cleaner interface. Ensure Enter is send.
```

### After this step:
- Review the CSS and HTML changes that Copilot generates
- Run the Flask application to verify the interface updates are applied correctly
- Test the responsiveness by resizing your browser window
- Confirm that pressing Enter sends messages

## Step 3: Real-Time Chat with Azure OpenAI

GitHub Copilot offers multiple models for assisting with code generation. Each has its own strengths for different tasks.

Click on the Copilot model selector to explore the different models available:

![Github Copilot Models](../media/Copilot-Models.png)

For this next part, switch to `Claude 3.7 Sonnet` for optimal results, and use the following prompt:

**Prompt:**
```prompt
Integrate real-time chat functionality into the existing Flask application using Azure OpenAI's GPT-4o.
Utilize the latest openai Python package to interact with Azure OpenAI. 
Ensure the integration supports streaming responses for a seamless user experience. 
Handle authentication using Azure OpenAI credentials and manage API requests appropriately.
```

### Setting up Azure OpenAI integration:

1. Locate the `.env` file created in the root directory
2. Replace the placeholder values with your actual Azure OpenAI details:
   - Azure OpenAI API key
   - Azure OpenAI endpoint
   - Deployment name 
   - API version

> **Important:** Ensure the deployment name matches your Azure OpenAI deployment and that you're using the correct API version.

3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the application and test the integration with GPT-4o

When implemented correctly, your application will feature streaming responses like this:

<div align="center">
    <img src="../media/chat_vid.gif" alt="Chat" width="600"/>
</div>

## Troubleshooting Tips

- If you encounter authentication errors, double-check your Azure OpenAI credentials
- Ensure your Azure OpenAI deployment is properly set up with the GPT-4o model
- Check your Python environment has all required dependencies installed
- Review browser console logs for any JavaScript errors affecting the chat interface

## Next Steps in Our Journey

Now that you've successfully built your chat application with Azure OpenAI integration, you're ready to move on to the next exciting part of this masterclass!

In the next module, we'll explore how to create a robust MCP server that will enhance your application's capabilities.

**Continue your learning:**
- [Creating MCP Server →](../docs/03-creating-mcp-server.md)
- [← Back to Home Page](../README.md)
- [← Learn About GitHub Copilot](../docs/01-explore-github-copilot.md)

