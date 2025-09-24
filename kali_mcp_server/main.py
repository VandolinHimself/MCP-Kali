"""Main entry point for the Kali MCP Server."""

import asyncio
import argparse
import logging
from .server import main

def cli():
    """Command line interface for the Kali MCP Server."""
    parser = argparse.ArgumentParser(description="Kali Linux MCP Server - Penetration Testing Tools Interface")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                       help="Set the logging level")
    parser.add_argument("--transport", default="stdio", choices=["stdio"],
                       help="Transport type for MCP communication")
    
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run the server
    asyncio.run(main())

if __name__ == "__main__":
    cli()
