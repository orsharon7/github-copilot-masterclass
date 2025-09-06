# GitHub Copilot Masterclass Repository

Always reference these instructions first before searching or running bash commands. Only fallback to additional exploration when the information here is incomplete or conflicts with what you observe.

## Working Effectively

**CRITICAL**: Always follow these exact setup steps in order. All commands and timings have been validated.

### Python Environment Setup
- Use Python 3.12+ (available in environment)
- Use pip3 for package management
- All installations use user directory (--user flag automatic due to permissions)

### Bootstrap the Flask Chat Application
```bash
cd /path/to/repo/chat-sample
pip3 install -r requirements.txt
```
**TIMING**: Installation takes ~10 seconds. NEVER CANCEL - set timeout to 30+ seconds.

### Bootstrap the MCP Server
```bash
cd /path/to/repo/chat-sample/steve-mcp
pip3 install -e .
```
**TIMING**: Installation takes ~8 seconds. NEVER CANCEL - set timeout to 30+ seconds.

### Environment Configuration
**CRITICAL**: Both applications require Azure OpenAI credentials to function fully.

#### Flask App Environment Setup:
```bash
cd /path/to/repo/chat-sample
cp .env.sample .env
# Edit .env with these EXACT variable names:
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com"
AZURE_OPENAI_DEPLOYMENT="gpt-4o"
```

#### MCP Server Environment Setup:
```bash
cd /path/to/repo/chat-sample/steve-mcp
# Create .env file with these EXACT variable names:
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com"
AZURE_OPENAI_API_VERSION="2024-04-01-preview"
AZURE_OPENAI_DEPLOYMENT="gpt-4o"
```

**WARNING**: The `.env.sample` file uses incorrect variable names (`AZURE_OPENAI_GPT4O_*`). Always use the exact names shown above.

### Run the Applications

#### Start Flask Chat Application:
```bash
cd /path/to/repo/chat-sample
python3 app.py
```
- **TIMING**: Starts in ~2 seconds. NEVER CANCEL.
- **Access**: Application runs on http://127.0.0.1:5001
- **Behavior**: Serves homepage even without valid credentials
- **Error Handling**: Returns graceful error message for chat without credentials

#### Start MCP Server:
```bash
cd /path/to/repo/chat-sample/steve-mcp
python3 steve-mcp.py
```
- **TIMING**: Starts in ~1 second. NEVER CANCEL.
- **Transport**: Uses stdio (Standard Input/Output)
- **Behavior**: Starts without errors even without valid credentials

**CRITICAL**: DO NOT use `python3 main.py` for MCP server - it has import errors. Always use `python3 steve-mcp.py`.

## Validation and Testing

### Manual Validation Steps
Always run these validation steps after making changes:

1. **Test Flask App Startup and Homepage**:
   ```bash
   # In background or separate terminal
   cd /path/to/repo/chat-sample && python3 app.py &
   # Test homepage loads
   curl -s http://127.0.0.1:5001/ | head -5
   # Test chat endpoint (expect graceful error without credentials)
   curl -X POST http://127.0.0.1:5001/chat -H "Content-Type: application/json" -d '{"message": "test", "stream": false}'
   ```

2. **Test MCP Server Startup**:
   ```bash
   cd /path/to/repo/chat-sample/steve-mcp
   timeout 5s python3 steve-mcp.py
   # Should start without errors and exit after timeout
   ```

3. **Test Dependencies Installation**:
   ```bash
   # Test Flask dependencies
   cd /path/to/repo/chat-sample && pip3 install -r requirements.txt
   # Test MCP dependencies  
   cd /path/to/repo/chat-sample/steve-mcp && pip3 install -e .
   ```

### Linting and Code Quality
```bash
# Install flake8 if not available
pip3 install flake8

# Lint Flask application
cd /path/to/repo/chat-sample
~/.local/bin/flake8 app.py --max-line-length=120

# Lint MCP server
cd /path/to/repo/chat-sample/steve-mcp
~/.local/bin/flake8 steve-mcp.py --max-line-length=120
```
**TIMING**: Linting takes ~1-2 seconds per file. NEVER CANCEL.

## Repository Structure and Key Files

### Root Directory
```
/repo-root/
├── .gitignore
├── README.md              # Workshop overview and setup
├── chat.png              # Reference image for UI
├── chat-sample/          # Main Flask application
├── docs/                 # Workshop documentation
└── media/                # Images and assets
```

### Flask Application (`/chat-sample/`)
```
/chat-sample/
├── app.py                # Main Flask application (port 5001)
├── requirements.txt      # Flask dependencies
├── .env.sample          # Environment variable template (WRONG NAMES)
├── templates/
│   └── index.html       # Chat interface with themes and reactions
├── static/
│   ├── steve.png        # Steve Jobs avatar
│   └── user.png         # User avatar
└── steve-mcp/          # MCP server subdirectory
```

### MCP Server (`/chat-sample/steve-mcp/`)
```
/steve-mcp/
├── steve-mcp.py         # Main MCP server (USE THIS)
├── main.py             # Broken entry point (DO NOT USE)
├── pyproject.toml      # Dependencies and project config
├── README.md           # MCP server documentation
└── uv.lock            # UV package manager lock file
```

## Common Tasks and Troubleshooting

### Environment Variable Issues
- **Problem**: Chat returns "trouble connecting" error
- **Solution**: Verify `.env` file exists with correct variable names (not GPT4O variants)
- **Validation**: Check `os.getenv()` calls in app.py and steve-mcp.py match your .env

### Port Conflicts
- **Problem**: "Address already in use" on port 5001
- **Solution**: `pkill -f "python3 app.py"` then restart
- **Prevention**: Always stop previous Flask instances before starting new ones

### MCP Server Won't Start
- **Problem**: AttributeError about missing 'main' function
- **Solution**: Use `python3 steve-mcp.py` NOT `python3 main.py`
- **Explanation**: main.py has import issues, steve-mcp.py is the correct entry point

### Dependency Installation Fails
- **Problem**: Permission errors during pip install
- **Solution**: Commands automatically use --user flag due to environment setup
- **Validation**: Check packages install to ~/.local/lib/python3.12/site-packages

## Workshop Components

### Documentation Files
- `docs/01-explore-github-copilot.md`: Copilot features and setup
- `docs/02-application-setup.md`: Flask app building guide
- `docs/03-creating-mcp-server.md`: MCP server creation guide
- `docs/copilot-instructions.md`: Existing project-specific guidance

### Key Features
- **Flask App**: Chat interface with Steve Jobs AI, multiple themes, reaction system
- **MCP Server**: Product management tools in Steve Jobs style for GitHub Copilot
- **Azure OpenAI Integration**: GPT-4o model with streaming support
- **FastMCP Framework**: Modern MCP server implementation

## Development Workflow

1. **Always run bootstrap steps first** (dependencies installation)
2. **Always create proper .env files** with correct variable names
3. **Always validate applications start correctly** after changes
4. **Always run linting** before committing changes
5. **Always test both Flask app and MCP server** after modifications
6. **NEVER use main.py for MCP server** - it's broken

## Performance Expectations

- **Total setup time**: Under 20 seconds for both applications
- **Flask app ready**: ~2 seconds after `python3 app.py`
- **MCP server ready**: ~1 second after `python3 steve-mcp.py`
- **No long builds or complex compilation required**
- **All operations complete quickly** - extended timeouts not needed except for safety

This repository is designed for rapid development and teaching GitHub Copilot concepts. The setup is intentionally simple and fast.