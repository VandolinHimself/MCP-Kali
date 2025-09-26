"""Subdomain enumeration tools for Kali MCP Server."""

from typing import Dict, List, Optional, Any
from .base import OSINTTool, ToolExecutionError

class TheHarvesterTool(OSINTTool):
    """Email, subdomain and people names harvester."""
    
    def __init__(self):
        super().__init__("theHarvester", "Email, subdomain and people names harvester")
    
    async def harvest_emails(self, domain: str, sources: str = "all", limit: int = 500) -> Dict[str, Any]:
        """Harvest emails from various sources."""
        args = ["-d", domain, "-b", sources, "-l", str(limit)]
        return await self.execute_command(args, timeout=1800)
    
    async def harvest_subdomains(self, domain: str, sources: str = "all") -> Dict[str, Any]:
        """Harvest subdomains from various sources."""
        args = ["-d", domain, "-b", sources, "-f", "subdomains"]
        return await self.execute_command(args, timeout=1800)

class Sublist3rTool(OSINTTool):
    """Subdomain enumeration tool."""
    
    def __init__(self):
        super().__init__("sublist3r", "Subdomain enumeration tool")
    
    async def enumerate_subdomains(self, domain: str, bruteforce: bool = False, threads: int = 40) -> Dict[str, Any]:
        """Enumerate subdomains using OSINT."""
        args = ["-d", domain, "-t", str(threads)]
        if bruteforce:
            args.append("-b")
        return await self.execute_command(args, timeout=1800)

class AmassTool(OSINTTool):
    """In-depth attack surface mapping and asset discovery."""
    
    def __init__(self):
        super().__init__("amass", "Attack surface mapping and asset discovery")
    
    async def enum_subdomains(self, domain: str, passive: bool = False, active: bool = False) -> Dict[str, Any]:
        """Enumerate subdomains using amass."""
        if passive:
            args = ["enum", "-passive", "-d", domain]
        elif active:
            args = ["enum", "-active", "-d", domain]
        else:
            args = ["enum", "-d", domain]
        return await self.execute_command(args, timeout=3600)
    
    async def intel_gathering(self, domain: str) -> Dict[str, Any]:
        """Gather intelligence on the target domain."""
        args = ["intel", "-d", domain]
        return await self.execute_command(args, timeout=1800)






