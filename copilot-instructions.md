# GitHub Copilot Custom Instructions

## Application Context
You are assisting developers in building high-quality Python Flask web applications. Your goal is to improve code readability, maintainability, and security while following modern web development best practices.

## Guidelines
- Follow Flask best practices and use a clean project structure (e.g., separate files for routes, services, templates, static assets).
- Use `python-dotenv` to manage environment variables securely.
- Ensure proper input validation and error handling throughout the application.
- Implement logging for both success and failure paths using Python's built-in `logging` module.
- Write modular, reusable helper functions for repeated logic.
- When applicable, use Flask Blueprints to organize large applications.
- Write docstrings for all routes and custom functions to improve clarity and developer experience.

## Preferred Patterns
- Use `@app.route()` with appropriate HTTP methods and clear route names.
- Handle request data using `request.get_json()` and validate input before processing.
- Return consistent, structured JSON responses with appropriate status codes.
- Use `try/except` blocks with specific exception handling and meaningful log messages.
- Use `render_template()` for returning HTML from the server and keep Jinja templates clean and accessible.

## requirements.txt Management
- Always check if the used libraries are listed in `requirements.txt`.
- If a new package (like `flask`, `openai`, `python-dotenv`, etc.) is used and not listed, add it.
- If a version of a library is referenced in the code or via import, prefer pinning a compatible version in `requirements.txt` (e.g., `flask>=2.2.0`).
- Keep the `requirements.txt` file alphabetically sorted for readability.

## Troubleshooting Tips
- If Flask routes aren’t working, double-check route decorators, method declarations, and function names.
- Log errors with `logging.error()` instead of using print statements.
- If a module import fails, suggest checking if it’s installed and listed in `requirements.txt`.
- Remind developers to restart the Flask server after major code or environment changes.