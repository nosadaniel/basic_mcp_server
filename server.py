from mcp.server.fastmcp import FastMCP

#create an mcp server
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather for a location"""
    return f"The weather in {location} is sunny, 76 degrees Fahrenheit"

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"The weather data for {location} is sunny, 76 degrees Fahrenheit"

@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Provide a weather report for {location}."""
    