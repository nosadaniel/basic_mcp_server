# Basic MCP Example - Weather Service

This is a basic example demonstrating how to implement an MCP (Multi-Cloud Protocol) server using FastMCP. The example implements a simple weather service that showcases the three main MCP components: tools, resources, and prompts.

## Purpose

This project serves as a learning example to demonstrate:
- How to create an MCP server using FastMCP
- How to implement MCP tools, resources, and prompts
- Basic MCP server structure and implementation

## Implementation Details

The server implements three MCP components to demonstrate different interaction patterns:

1. **Tool**: `get_weather(location: str)`
   - Example of a simple MCP tool
   - Shows how to define a tool with parameters
   - Demonstrates tool return values

2. **Resource**: `weather://{location}`
   - Example of MCP resource usage
   - Shows resource URL pattern matching
   - Demonstrates resource parameter handling

3. **Prompt**: `weather_report(location: str)`
   - Example of MCP prompt implementation
   - Shows how to create formatted prompts
   - Demonstrates prompt parameter usage

## Running the Example

To run this example:
1. Install FastMCP library
2. Run `server.py` directly

## Requirements

- Python 3.13 or higher
- MCP library with CLI support (`mcp[cli]`)

## Project Structure

- `server.py`: MCP server implementation
- `main.py`: Entry point that runs the server
- `pyproject.toml`: Project configuration
- `.gitignore`: Git ignore rules

## Running the Example

To run this example:
1. Install the required dependencies from `pyproject.toml`
2. Run `python main.py` to start the server
3. The server will run on port 8080 using SSE transport

## Note

This is a basic example that returns static data. In a real application, you would:
- Connect to actual data sources
- Implement proper error handling
- Add authentication and authorization
- Implement proper logging
- Add comprehensive documentation
- Configure different transport methods beyond SSE
- Add proper server configuration options
- Implement production-ready error handling
- Add monitoring and metrics
- Configure proper port management
- Add environment variable support
- Handle edge cases and validation

This example is intentionally kept simple to focus on MCP concepts rather than production considerations.