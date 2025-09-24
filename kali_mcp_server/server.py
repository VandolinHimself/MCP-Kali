"""Main MCP server implementation for Kali Linux penetration testing tools."""

import asyncio
import logging
from typing import Any, Sequence
from mcp.server import Server
from mcp.types import Tool, TextContent

# Import all tool classes
from .network_recon import (
    WhoisTool, DigTool, DnsenumTool, DnsreconTool, 
    NmapTool, MasscanTool, UnicornscanTool, ZmapTool, IkeScanTool
)
from .subdomain_enum import TheHarvesterTool, Sublist3rTool, AmassTool
from .web_analysis import (
    WhatwebTool, Wafw00fTool, DirbTool, GobusterTool, 
    FeroxbusterTool, NiktoTool, WfuzzTool, ArachniTool
)
from .enumeration import (
    Enum4linuxTool, Enum4linuxNgTool, SmbmapTool, 
    RpcclientTool, SnmpwalkTool, LdapsearchTool
)
from .ssl_network import SslscanTool, SslyzeTool, NetcatTool, CurlTool, WgetTool
from .wireless import AirmonNgTool, AirodumpNgTool, WashTool, KismetTool, BettercapTool
from .osint import ShodanTool, ReconNgTool, MetagoofiltTool, MaltegoTool

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KaliMCPServer:
    """MCP Server for Kali Linux penetration testing tools."""
    
    def __init__(self):
        self.server = Server("kali-mcp-server")
        self.tools = self._initialize_tools()
        self._register_tools()
    
    def _initialize_tools(self):
        """Initialize all available tools."""
        return {
            # Network Reconnaissance
            "whois": WhoisTool(),
            "dig": DigTool(),
            "dnsenum": DnsenumTool(),
            "dnsrecon": DnsreconTool(),
            "nmap": NmapTool(),
            "masscan": MasscanTool(),
            "unicornscan": UnicornscanTool(),
            "zmap": ZmapTool(),
            "ike-scan": IkeScanTool(),
            
            # Subdomain Enumeration
            "theharvester": TheHarvesterTool(),
            "sublist3r": Sublist3rTool(),
            "amass": AmassTool(),
            
            # Web Analysis
            "whatweb": WhatwebTool(),
            "wafw00f": Wafw00fTool(),
            "dirb": DirbTool(),
            "gobuster": GobusterTool(),
            "feroxbuster": FeroxbusterTool(),
            "nikto": NiktoTool(),
            "wfuzz": WfuzzTool(),
            "arachni": ArachniTool(),
            
            # Enumeration
            "enum4linux": Enum4linuxTool(),
            "enum4linux-ng": Enum4linuxNgTool(),
            "smbmap": SmbmapTool(),
            "rpcclient": RpcclientTool(),
            "snmpwalk": SnmpwalkTool(),
            "ldapsearch": LdapsearchTool(),
            
            # SSL/Network Tools
            "sslscan": SslscanTool(),
            "sslyze": SslyzeTool(),
            "netcat": NetcatTool(),
            "curl": CurlTool(),
            "wget": WgetTool(),
            
            # Wireless Tools
            "airmon-ng": AirmonNgTool(),
            "airodump-ng": AirodumpNgTool(),
            "wash": WashTool(),
            "kismet": KismetTool(),
            "bettercap": BettercapTool(),
            
            # OSINT Tools
            "shodan": ShodanTool(),
            "recon-ng": ReconNgTool(),
            "metagoofil": MetagoofiltTool(),
            "maltego": MaltegoTool(),
        }
    
    def _register_tools(self):
        """Register all tools with the MCP server."""
        
        # WHOIS Tool
        @self.server.call_tool()
        async def whois_lookup(domain: str) -> Sequence[TextContent]:
            """Perform WHOIS lookup on a domain."""
            try:
                result = await self.tools["whois"].lookup_domain(domain)
                return [TextContent(type="text", text=f"WHOIS Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        # DIG Tool
        @self.server.call_tool()
        async def dig_lookup(domain: str, record_type: str = "A", dns_server: str = None) -> Sequence[TextContent]:
            """Perform DNS lookup using dig."""
            try:
                result = await self.tools["dig"].dns_lookup(domain, record_type, dns_server)
                return [TextContent(type="text", text=f"DIG Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        @self.server.call_tool()
        async def dig_reverse_lookup(ip: str) -> Sequence[TextContent]:
            """Perform reverse DNS lookup using dig."""
            try:
                result = await self.tools["dig"].reverse_lookup(ip)
                return [TextContent(type="text", text=f"Reverse DNS Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        # DNSENUM Tool
        @self.server.call_tool()
        async def dnsenum_scan(domain: str, wordlist: str = None, threads: int = 5) -> Sequence[TextContent]:
            """Perform DNS enumeration using dnsenum."""
            try:
                result = await self.tools["dnsenum"].enumerate_dns(domain, wordlist, threads)
                return [TextContent(type="text", text=f"DNSENUM Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        # DNSRECON Tool
        @self.server.call_tool()
        async def dnsrecon_scan(domain: str, scan_type: str = "std", wordlist: str = None) -> Sequence[TextContent]:
            """Perform DNS reconnaissance using dnsrecon."""
            try:
                result = await self.tools["dnsrecon"].dns_recon(domain, scan_type, wordlist)
                return [TextContent(type="text", text=f"DNSRECON Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        # NMAP Tools
        @self.server.call_tool()
        async def nmap_port_scan(target: str, ports: str = None, scan_type: str = "-sS") -> Sequence[TextContent]:
            """Perform port scan using nmap."""
            try:
                result = await self.tools["nmap"].port_scan(target, ports, scan_type)
                return [TextContent(type="text", text=f"NMAP Port Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        @self.server.call_tool()
        async def nmap_service_scan(target: str, ports: str = None) -> Sequence[TextContent]:
            """Perform service version detection using nmap."""
            try:
                result = await self.tools["nmap"].service_scan(target, ports)
                return [TextContent(type="text", text=f"NMAP Service Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        @self.server.call_tool()
        async def nmap_os_detection(target: str) -> Sequence[TextContent]:
            """Perform OS detection using nmap."""
            try:
                result = await self.tools["nmap"].os_detection(target)
                return [TextContent(type="text", text=f"NMAP OS Detection Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        @self.server.call_tool()
        async def nmap_vuln_scan(target: str, ports: str = None) -> Sequence[TextContent]:
            """Perform vulnerability scan using nmap NSE scripts."""
            try:
                result = await self.tools["nmap"].vuln_scan(target, ports)
                return [TextContent(type="text", text=f"NMAP Vulnerability Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]
        
        # Continue with more tool registrations...
        # (The pattern continues for all other tools)
        
    async def run(self, transport_type: str = "stdio"):
        """Run the MCP server."""
        if transport_type == "stdio":
            from mcp.server.stdio import stdio_server
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(read_stream, write_stream, self.server.create_initialization_options())
        else:
            raise ValueError(f"Unsupported transport type: {transport_type}")

async def main():
    """Main entry point for the server."""
    server = KaliMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
