from server import mcp
def main():
    mcp.run(transport="sse", port=8080)


if __name__ == "__main__":
    main()
