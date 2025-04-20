#!/usr/bin/env python3

import json
import os
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Azure OpenAI client
azure_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-04-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

# Initialize FastMCP server
mcp = FastMCP("steve-mcp")

# Tool implementations
async def generate_feature_idea_implementation(user_type: str) -> Dict[str, Any]:
    """
    Generate a visionary product feature idea based on a user persona or type.
    
    Args:
        user_type: The type of user or persona to generate a feature for
        
    Returns:
        Dictionary with feature title and description in Jobs-like tone
    """
    prompt = f"""
    You are Steve Jobs, envisioning the next revolutionary feature for {user_type}.
    Think about what these users truly need (not what they say they want).
    Create a feature that is elegant, simple yet powerful, and genuinely changes how people work.
    
    Respond with a JSON object containing:
    1. "title": A short, catchy name for the feature (max 6 words)
    2. "description": A brief explanation of the feature in Steve Jobs' visionary tone (2-3 sentences)
    
    Format the response as valid JSON only.
    """
    
    # Call Azure OpenAI to generate the feature idea
    response = azure_client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are Steve Jobs, the visionary product leader."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=300
    )
    
    # Parse the response
    result = json.loads(response.choices[0].message.content)
    return result


async def generate_feature_spec_implementation(title: str) -> Dict[str, Any]:
    """
    Given a product feature name, generate a clear specification suitable for GitHub Copilot development.
    
    Args:
        title: The title of the feature to specify
        
    Returns:
        Dictionary with structured specification
    """
    prompt = f"""
    You are Steve Jobs, writing a clear, visionary specification for a feature called "{title}".
    Create a specification that will inspire developers while providing enough clarity for GitHub Copilot to implement.
    
    Respond with a JSON object containing:
    1. "problem": What problem does this solve? (1-2 sentences)
    2. "solution": What is the core solution? (2-3 sentences)
    3. "design_principles": What design principles should guide the implementation? (3-5 bullet points)
    4. "implementation_notes": Technical implementation guidance for GitHub Copilot (3-5 bullet points)
    
    Format the response as valid JSON only.
    """
    
    # Call Azure OpenAI to generate the feature spec
    response = azure_client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are Steve Jobs, the visionary product leader."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=800
    )
    
    # Parse the response
    result = json.loads(response.choices[0].message.content)
    return result


# ----- Define MCP tools using decorator approach -----

@mcp.tool()
async def generate_feature_idea(user_type: str) -> str:
    """Generate a visionary product feature idea based on a user persona or type.
    
    Args:
        user_type: The type of user or persona to generate a feature for
    """
    try:
        result = await generate_feature_idea_implementation(user_type)
        return f"# {result['title']}\n\n{result['description']}"
    except Exception as e:
        return f"Error generating feature idea: {str(e)}"


@mcp.tool()
async def generate_feature_spec(title: str) -> str:
    """Given a product feature name, generate a clear specification suitable for GitHub Copilot development.
    
    Args:
        title: The title of the feature to specify
    """
    try:
        result = await generate_feature_spec_implementation(title)
        
        # Format the response as markdown
        markdown = f"""
# {title} - Feature Specification

## Problem
{result['problem']}

## Solution
{result['solution']}

## Design Principles
{' '.join(['- ' + principle + '\n' for principle in result['design_principles']])}

## Implementation Notes for GitHub Copilot
{' '.join(['- ' + note + '\n' for note in result['implementation_notes']])}
"""
        
        return markdown.strip()
    except Exception as e:
        return f"Error generating feature spec: {str(e)}"


# Running the server
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')