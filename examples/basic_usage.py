#!/usr/bin/env python3
"""
Basic usage examples for the Kali MCP Server.

This script demonstrates how to interact with the MCP server
for various penetration testing tasks.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    """Demonstrate basic usage of the Kali MCP Server."""
    
    # Start the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "kali_mcp_server.main"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # Example 1: WHOIS lookup
            print("=== WHOIS Lookup Example ===")
            result = await session.call_tool("whois_lookup", {"domain": "example.com"})
            print(result.content[0].text)
            
            # Example 2: DNS lookup
            print("\n=== DNS Lookup Example ===")
            result = await session.call_tool("dig_dns_lookup", {
                "domain": "example.com",
                "record_type": "A"
            })
            print(result.content[0].text)
            
            # Example 3: NMAP port scan
            print("\n=== NMAP Port Scan Example ===")
            result = await session.call_tool("nmap_port_scan", {
                "target": "scanme.nmap.org",
                "ports": "22,80,443",
                "scan_type": "-sS"
            })
            print(result.content[0].text)
            
            # Example 4: Web analysis
            print("\n=== Web Analysis Example ===")
            result = await session.call_tool("whatweb_analyze", {
                "url": "https://example.com",
                "aggression": 1
            })
            print(result.content[0].text)
            
            # Example 5: Subdomain enumeration
            print("\n=== Subdomain Enumeration Example ===")
            result = await session.call_tool("sublist3r_enumerate", {
                "domain": "example.com",
                "bruteforce": False,
                "threads": 40
            })
            print(result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
