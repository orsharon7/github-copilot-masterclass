# Module 1: Exploring GitHub Copilot in Visual Studio Code

## ✨ Introduction to GitHub Copilot

GitHub Copilot is an AI-powered coding assistant developed by GitHub and OpenAI. It integrates seamlessly with Visual Studio Code (VS Code) to provide real-time code suggestions, generate functions, write tests, and even explain code snippets. By leveraging machine learning models trained on vast amounts of public code, Copilot aims to enhance developer productivity and streamline the coding process.

---

## 🛠️ Installing GitHub Copilot in VS Code

1. **Open VS Code**: Launch your Visual Studio Code editor.
2. **Access Extensions**: Click on the Extensions icon in the Activity Bar on the side of the window.
3. **Search for Copilot**: In the Extensions view search bar, type `GitHub Copilot`.
4. **Install the Extension**: Find the official GitHub Copilot extension and click **Install**.
5. **Sign In to GitHub**: After installation, you'll be prompted to sign in to your GitHub account to authenticate and activate Copilot.
6. **Configure Settings**: Adjust Copilot settings as needed by navigating to `Preferences > Settings > Extensions > GitHub Copilot`.

---

## ✨ Key Features of GitHub Copilot

### 1. **Code Suggestions as You Type**

Copilot provides real-time code completions based on the context of the current file. As you type, it suggests entire lines or blocks of code, helping to speed up development.

### 2. **Copilot Chat Integration**

Engage in a conversational interface with Copilot directly within VS Code. You can ask questions, request code explanations, or generate code snippets.

- **Opening Copilot Chat**:
  - Click on the Copilot icon in the Activity Bar.
  - Alternatively, use the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select `GitHub Copilot: Chat`.

- **Using Copilot Chat**:
  - Type your query in natural language, such as:
    - "Explain the function `calculateTotal`."
    - "Generate a Python function to sort a list."

### 3. **Prompt Engineering for Better Results**

To get the most out of Copilot, structure your prompts effectively:

- **Start General, Then Get Specific**:
  - Begin with a broad description, then add specific requirements.

  **Example**:
  > "Write a function that checks if a number is prime.
  > The function should take an integer and return true if the number is prime.
  > It should raise an error if the input is not a positive integer."

This approach helps Copilot understand the context and generate more accurate code.

### 4. **Utilizing Slash Commands in Copilot Chat**

Copilot Chat supports slash commands to perform specific actions quickly:

- `/explain`: Provides an explanation for the selected code.
- `/fix`: Suggests fixes for the selected code.
- `/tests`: Generates unit tests for the selected code.
- `/optimize`: Suggests performance improvements.
- `/help`: Offers assistance with Copilot features.

To use a slash command, type `/` followed by the command name in the Copilot Chat input box.

### 5. **Chat Participants**

Chat participants are specialized assistants that can provide context-specific help. You can invoke them by typing `@` followed by the participant's name. To see all available participants, type `@` in the chat prompt box. For example, `@github` can assist with GitHub-specific queries.

### 6. **Modes in Copilot Chat**

Copilot Chat offers different modes to tailor the interaction:

- **Edit Mode**: Allows you to make changes to your codebase by providing natural language instructions. Copilot will suggest edits which you can review and apply.
- **Ask Mode**: Enables you to ask questions or request explanations without making changes to the code.
- **Agent Mode**: Provides a more autonomous assistant that can perform tasks like running commands or making broader changes across your project.

You can switch between these modes using the dropdown menu at the bottom of the Copilot Chat panel.

### 7. **AI Model Selection**

Copilot Chat supports multiple AI models, allowing you to choose the one that best fits your needs:

- **GPT-4o**: A versatile, multimodal model suitable for a wide range of tasks.
- **Claude 3.5 Sonnet**: Known for its reasoning capabilities.
- **Claude 3.7 Sonnet**: An updated version with improved performance.
- **Gemini 2.0 Flash**: Offers fast response times.
- **o1**, **o3**, **o3-mini**, **o4-mini**: Various models with different performance characteristics.

To change the AI model in Copilot Chat:

1. Open the Copilot Chat panel.
2. Click on the model name at the bottom right corner.
3. Select your preferred model.

## Next Modules
2. [Jump Directly to the Workshop](02-application-setup.md)
3. [Creating MCP Server](03-creating-mcp-server.md)

---

## 📃 Additional Resources

- [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)
- [Asking GitHub Copilot Questions in Your IDE](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/asking-github-copilot-questions-in-your-ide)
- [Prompt Engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)
- [GitHub Copilot Chat Cheat Sheet](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet)
- [Changing the AI Model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat)
- [Copilot Support for MCP Server](https://modelcontextprotocol.io/llms-full.txt)

