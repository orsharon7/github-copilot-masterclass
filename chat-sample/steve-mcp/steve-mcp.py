#!/usr/bin/env python3

import json
import os
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
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


async def define_product_implementation(product_concept: str, target_audience: str = None) -> Dict[str, Any]:
    """
    Define a complete product specification for a fresh new project.
    
    Args:
        product_concept: The basic concept or idea for the product
        target_audience: The intended users for the product (optional)
        
    Returns:
        Dictionary with comprehensive product definition
    """
    audience_context = f" for {target_audience}" if target_audience else ""
    
    prompt = f"""
    You are Steve Jobs, defining a complete product vision for a revolutionary new product: "{product_concept}"{audience_context}.
    Think about what would truly change people's lives and create something insanely great.
    
    Create a comprehensive product definition that GitHub Copilot can use to develop the entire project.
    
    Respond with a JSON object containing:
    1. "product_name": A memorable, iconic product name (2-4 words)
    2. "vision_statement": A inspiring one-sentence vision (Steve Jobs style)
    3. "target_users": Who will use this product? (2-3 sentences)
    4. "core_problem": What fundamental problem does this solve? (2-3 sentences)
    5. "unique_value": What makes this product revolutionary? (2-3 sentences)
    6. "key_features": Array of 5-7 essential features with brief descriptions
    7. "technical_architecture": Recommended tech stack and architecture (for GitHub Copilot)
    8. "user_experience": How users will interact with the product (2-3 sentences)
    9. "success_metrics": How to measure product success (3-5 metrics)
    10. "development_phases": Array of 3-4 development phases with priorities
    
    Format the response as valid JSON only.
    """
    
    # Call Azure OpenAI to generate the product definition
    response = azure_client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are Steve Jobs, the visionary product leader who creates products that change the world."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.8,
        max_tokens=1500
    )
    
    # Parse the response
    result = json.loads(response.choices[0].message.content)
    return result


async def create_technical_blueprint_implementation(product_concept: str, complexity_level: str = "medium") -> Dict[str, Any]:
    """
    Create a technical implementation blueprint for building a product quickly and efficiently.
    
    Args:
        product_concept: The product concept to create a technical blueprint for
        complexity_level: The desired complexity level - "simple", "medium", or "advanced"
        
    Returns:
        Dictionary with detailed technical implementation strategy
    """
    prompt = f"""
    You are a world-class technical architect who specializes in rapid prototyping and MVP development.
    Create a practical, actionable technical blueprint for building "{product_concept}" with {complexity_level} complexity.
    
    Focus ONLY on development aspects:
    - Speed to development (fastest path to working prototype)
    - Modern, proven development technologies
    - Minimal complexity while maintaining quality
    - Clear step-by-step development approach
    - Specific development tools, frameworks, and libraries to use
    - Local development setup and workflow
    
    Respond with a JSON object containing:
    1. "tech_stack": Object with frontend, backend, database technologies (no deployment info)
    2. "architecture_pattern": Recommended development architecture approach (monolith, microservices, etc.)
    3. "development_setup": Step-by-step approach to set up local development environment (5-7 steps)
    4. "mvp_features": Array of 3-5 core features to build first for MVP
    5. "development_tools": Recommended IDEs, testing tools, debugging tools, package managers
    6. "third_party_libraries": External libraries/packages to integrate for faster development
    7. "estimated_development_timeline": Realistic timeline breakdown by development phases
    8. "local_testing_strategy": How to test and validate locally during development
    9. "development_challenges": Potential development challenges and solutions
    10. "code_organization": How to structure and organize the codebase for maintainability
    
    Format the response as valid JSON only.
    """
    
    # Call Azure OpenAI to generate the technical blueprint
    response = azure_client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a pragmatic technical architect focused on rapid, efficient product development."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.6,
        max_tokens=1800
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


@mcp.tool()
async def define_product(product_concept: str, target_audience: str = None) -> str:
    """Define a complete product specification for a fresh new project that GitHub Copilot can develop.
    
    Args:
        product_concept: The basic concept or idea for the product
        target_audience: The intended users for the product (optional)
    """
    try:
        result = await define_product_implementation(product_concept, target_audience)
        
        # Format the response as comprehensive markdown
        markdown = f"""
# {result['product_name']} - Complete Product Definition

## Vision Statement
*{result['vision_statement']}*

## Target Users
{result['target_users']}

## Core Problem We're Solving
{result['core_problem']}

## Unique Value Proposition
{result['unique_value']}

## Key Features
{chr(10).join(['- ' + str(feature) for feature in result['key_features']])}

## Technical Architecture
{result['technical_architecture']}

## User Experience
{result['user_experience']}

## Success Metrics
{chr(10).join(['- ' + str(metric) for metric in result['success_metrics']])}

## Development Phases
{chr(10).join(['### Phase ' + str(i+1) + ': ' + str(phase) for i, phase in enumerate(result['development_phases'])])}

---
*This product definition is ready for GitHub Copilot to begin development. Start with Phase 1 and build iteratively.*
"""
        
        return markdown.strip()
    except Exception as e:
        return f"Error defining product: {str(e)}"


@mcp.tool()
async def create_technical_blueprint(product_concept: str, complexity_level: str = "medium") -> str:
    """Create a technical implementation blueprint for building a product quickly and efficiently.
    
    Args:
        product_concept: The product concept to create a technical blueprint for
        complexity_level: The desired complexity level - "simple", "medium", or "advanced"
    """
    try:
        result = await create_technical_blueprint_implementation(product_concept, complexity_level)
        
        # Format tech stack nicely
        tech_stack = result['tech_stack']
        tech_stack_md = f"""- **Frontend**: {tech_stack.get('frontend', 'Not specified')}
- **Backend**: {tech_stack.get('backend', 'Not specified')}
- **Database**: {tech_stack.get('database', 'Not specified')}"""
        
        # Format the response as comprehensive markdown
        markdown = f"""
# Development Blueprint: {product_concept.title()}

## Recommended Tech Stack
{tech_stack_md}

## Architecture Pattern
{result['architecture_pattern']}

## Development Environment Setup
{chr(10).join([str(i+1) + '. ' + str(step) for i, step in enumerate(result['development_setup'])])}

## MVP Features (Build These First)
{chr(10).join(['- ' + str(feature) for feature in result['mvp_features']])}

## Development Tools
{result['development_tools']}

## Third-Party Libraries & Packages
{chr(10).join(['- ' + str(library) for library in result['third_party_libraries']])}

## Development Timeline
{result['estimated_development_timeline']}

## Local Testing Strategy
{result['local_testing_strategy']}

## Development Challenges & Solutions
{chr(10).join(['- ' + str(challenge) for challenge in result['development_challenges']])}

## Code Organization
{result['code_organization']}

---
*This development blueprint is optimized for rapid local development. Start with the development setup and build the MVP features iteratively.*
"""
        
        return markdown.strip()
    except Exception as e:
        return f"Error creating technical blueprint: {str(e)}"

@mcp.prompt()
def start_development() -> str:
    """Start developing with a structured approach"""
    return f"Begin development with small, incremental steps. Break the project into micro-tasks and document progress in a dedicated file. At each stage, focus only on the current step—avoid overbuilding or jumping ahead."



# Running the server
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')