#!/usr/bin/env python3

import asyncio
import importlib.util
import sys

def main():
    print("Running Steve Jobs MCP Server...")
    # Import the steve-mcp module directly from the file
    spec = importlib.util.spec_from_file_location("steve_mcp", "steve-mcp.py")
    steve_mcp = importlib.util.module_from_spec(spec)
    sys.modules["steve_mcp"] = steve_mcp
    spec.loader.exec_module(steve_mcp)
    
    # Run the main function from the steve-mcp module
    asyncio.run(steve_mcp.main())


if __name__ == "__main__":
    main()
