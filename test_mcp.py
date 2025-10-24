import asyncio
from fastmcp import Client

async def test_tools():
    """Test MCP tools using FastMCP Client"""
    print("MCP Server Test Suite")
    print("="*60)
    
    # Connect to the HTTP server
    async with Client("http://localhost:8000/mcp") as client:
        print("✅ Connected to MCP server!")
        
        # List available tools
        print("\n" + "="*60)
        print("Available Tools:")
        print("="*60)
        tools = await client.list_tools()
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")
        
        # Test 1: Generate Code
        print("\n" + "="*60)
        print("Test 1: generate_code")
        print("="*60)
        print("Input: Create a Python function to calculate fibonacci")
        
        try:
            result = await client.call_tool(
                "generate_code",
                {"input_data": "Create a Python function to calculate fibonacci numbers"}
            )
            print(f"\n✅ SUCCESS!")
            print(f"Output:\n{result.content[0].text[:300]}...")
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
        
        # Test 2: Review Code
        print("\n" + "="*60)
        print("Test 2: review_code")
        print("="*60)
        code_sample = """def divide(a, b):
    return a / b
"""
        print(f"Input: {code_sample}")
        
        try:
            result = await client.call_tool(
                "review_code",
                {"input_data": code_sample}
            )
            print(f"\n✅ SUCCESS!")
            print(f"Output:\n{result.content[0].text[:300]}...")
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
        
        # Test 3: Explain Code
        print("\n" + "="*60)
        print("Test 3: explain_code")
        print("="*60)
        code_to_explain = "result = [x**2 for x in range(10) if x % 2 == 0]"
        print(f"Input: {code_to_explain}")
        
        try:
            result = await client.call_tool(
                "explain_code",
                {"input_data": code_to_explain}
            )
            print(f"\n✅ SUCCESS!")
            print(f"Output:\n{result.content[0].text}")
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
        
        print("\n" + "="*60)
        print("Testing complete!")
        print("="*60)

if __name__ == "__main__":
    try:
        asyncio.run(test_tools())
    except Exception as e:
        print(f"\n❌ Connection Error: {e}")
        print("\nMake sure:")
        print("1. Your server is running: python server.py")
        print("2. Server is on port 8000")
        print("3. FastMCP is installed: pip install fastmcp")