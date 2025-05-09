# Steve Jobs MCP Server

A Model Context Protocol (MCP) server that embodies Steve Jobs as a product manager persona to help users brainstorm revolutionary product features and generate clear specifications for GitHub Copilot to implement.

## Features

This MCP server provides:

1. **Tools**:
   - `generate_feature_idea`: Creates a visionary product feature idea for a specific user persona
   - `generate_feature_spec`: Generates a detailed specification for a feature, suitable for GitHub Copilot development

2. **Prompts**:
   - `ask_steve_to_invent`: Simulates Steve Jobs' thinking to invent a feature and create a spec for a specific type of user

## Setup

### Prerequisites

- Python 3.12 or higher
- An Azure OpenAI API key and endpoint with access to GPT-4o

### Installation

1. Clone this repository
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -e .
   ```

### Configuration

1. Copy the `.env.template` file to `.env`
2. Edit the `.env` file with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_API_KEY=your-api-key
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2024-04-01-preview
   AZURE_OPENAI_DEPLOYMENT=your-gpt4o-deployment-name
   ```

## Usage

### Running the Server

Execute the server:
```
python main.py
```

The server uses stdio for communication, making it compatible with MCP clients like Claude Desktop, VS Code GitHub Copilot, and others.

### Connecting from VS Code GitHub Copilot

1. Install the GitHub Copilot extension in VS Code
2. Add the following configuration to your `.vscode/settings.json`:
   ```json
   {
     "github.copilot.chat.mcp": {
       "servers": [
         {
           "name": "Steve Jobs",
           "path": "python",
           "args": ["path/to/steve-mcp.py"]
         }
       ]
     }
   }
   ```

### Connecting from Claude Desktop

1. Open Claude Desktop settings
2. Navigate to the "Tools" section
3. Add a new tool with the path to the `steve-mcp.py` script

## Example Interactions

### Generate Feature Idea

Ask the MCP server to generate a feature idea for designers:

```
User: Can you help me brainstorm a feature for designers?
Steve: Let me generate a feature idea for designers...

# Smart Layout Snap

A revolutionary design tool that intelligently anticipates designer intent, automatically suggesting optimal layout arrangements while preserving creative freedom. This isn't just alignment guides—it's a design partner that learns from your style and helps you achieve pixel-perfect layouts in half the time.
```

### Generate Feature Specification

Ask the MCP server to create a detailed specification for a feature:

```
User: Can you create a spec for a "Smart Layout Snap" feature?
Steve: Here's a specification for Smart Layout Snap...

# Smart Layout Snap - Feature Specification

## Problem
Designers waste countless hours manually aligning elements and ensuring consistent spacing across their designs, reducing creative time and increasing frustration.

## Solution
Smart Layout Snap uses machine learning to understand design patterns and intent, automatically suggesting optimal alignment and spacing while adapting to the designer's personal style and project requirements.

## Design Principles
- Design should feel magical, not mechanical
- Preserve creative freedom at all costs
- Learn from user behavior without requiring explicit training
- Focus on the 80% case to keep the interface simple
- Performance must be instantaneous

## Implementation Notes for GitHub Copilot
- Implement a prediction engine using a combination of rule-based heuristics and ML model
- Store design patterns as vector embeddings for fast similarity matching
- Use subtle visual cues that appear and disappear smoothly
- Include an override mechanism with a simple modifier key
- Create an adaptive learning system that improves with designer usage
```

### Using the Prompt

Use the `ask_steve_to_invent` prompt to have Steve generate both an idea and spec for a specific user type:

```
User: /ask_steve_to_invent user_type="mobile developers"
Steve: [Responds with a complete feature idea and specification targeted at mobile developers]
```

## Development

### Adding New Tools

To add new tools to the server, add new functions decorated with `@app.register_tool()` in `steve-mcp.py`.

### Modifying Prompts

To modify or add prompts, update the `list_prompts()` and `get_prompt()` functions in `steve-mcp.py`.

## License

MIT