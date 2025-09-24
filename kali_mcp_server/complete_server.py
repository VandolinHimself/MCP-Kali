"""Complete MCP server implementation with all tool handlers."""

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

class CompletKaliMCPServer:
    """Complete MCP Server for Kali Linux penetration testing tools."""
    
    def __init__(self):
        self.server = Server("kali-mcp-server")
        self.tools = self._initialize_tools()
        self._register_all_tools()
    
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
    
    def _register_all_tools(self):
        """Register all tools with the MCP server."""
        self._register_network_recon_tools()
        self._register_subdomain_enum_tools()
        self._register_web_analysis_tools()
        self._register_enumeration_tools()
        self._register_ssl_network_tools()
        self._register_wireless_tools()
        self._register_osint_tools()
    
    def _register_network_recon_tools(self):
        """Register network reconnaissance tools."""
        
        @self.server.call_tool()
        async def whois_lookup(domain: str) -> Sequence[TextContent]:
            """Perform WHOIS lookup on a domain."""
            try:
                result = await self.tools["whois"].lookup_domain(domain)
                return [TextContent(type="text", text=f"WHOIS Result for {domain}:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing WHOIS lookup: {str(e)}")]
        
        @self.server.call_tool()
        async def dig_dns_lookup(domain: str, record_type: str = "A", dns_server: str = None) -> Sequence[TextContent]:
            """Perform DNS lookup using dig."""
            try:
                result = await self.tools["dig"].dns_lookup(domain, record_type, dns_server)
                return [TextContent(type="text", text=f"DIG DNS Lookup Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing DNS lookup: {str(e)}")]
        
        @self.server.call_tool()
        async def dig_reverse_lookup(ip: str) -> Sequence[TextContent]:
            """Perform reverse DNS lookup using dig."""
            try:
                result = await self.tools["dig"].reverse_lookup(ip)
                return [TextContent(type="text", text=f"Reverse DNS Lookup Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing reverse DNS lookup: {str(e)}")]
        
        @self.server.call_tool()
        async def nmap_port_scan(target: str, ports: str = None, scan_type: str = "-sS") -> Sequence[TextContent]:
            """Perform port scan using nmap."""
            try:
                result = await self.tools["nmap"].port_scan(target, ports, scan_type)
                return [TextContent(type="text", text=f"NMAP Port Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing port scan: {str(e)}")]
        
        @self.server.call_tool()
        async def nmap_service_scan(target: str, ports: str = None) -> Sequence[TextContent]:
            """Perform service version detection using nmap."""
            try:
                result = await self.tools["nmap"].service_scan(target, ports)
                return [TextContent(type="text", text=f"NMAP Service Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing service scan: {str(e)}")]
    
    def _register_web_analysis_tools(self):
        """Register web analysis tools."""
        
        @self.server.call_tool()
        async def whatweb_analyze(url: str, aggression: int = 1) -> Sequence[TextContent]:
            """Analyze website technology stack using whatweb."""
            try:
                result = await self.tools["whatweb"].analyze_website(url, aggression)
                return [TextContent(type="text", text=f"WhatWeb Analysis Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error analyzing website: {str(e)}")]
        
        @self.server.call_tool()
        async def gobuster_dir_scan(url: str, wordlist: str = None, extensions: str = None, threads: int = 10) -> Sequence[TextContent]:
            """Perform directory scanning using gobuster."""
            try:
                result = await self.tools["gobuster"].directory_scan(url, wordlist, extensions, threads)
                return [TextContent(type="text", text=f"Gobuster Directory Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing directory scan: {str(e)}")]
        
        @self.server.call_tool()
        async def nikto_scan(host: str, port: int = None, ssl: bool = False) -> Sequence[TextContent]:
            """Perform web vulnerability scan using nikto."""
            try:
                result = await self.tools["nikto"].scan_website(host, port, ssl)
                return [TextContent(type="text", text=f"Nikto Scan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing Nikto scan: {str(e)}")]
    
    def _register_subdomain_enum_tools(self):
        """Register subdomain enumeration tools."""
        
        @self.server.call_tool()
        async def sublist3r_enumerate(domain: str, bruteforce: bool = False, threads: int = 40) -> Sequence[TextContent]:
            """Enumerate subdomains using sublist3r."""
            try:
                result = await self.tools["sublist3r"].enumerate_subdomains(domain, bruteforce, threads)
                return [TextContent(type="text", text=f"Sublist3r Enumeration Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error enumerating subdomains: {str(e)}")]
        
        @self.server.call_tool()
        async def amass_enum_subdomains(domain: str, passive: bool = False, active: bool = False) -> Sequence[TextContent]:
            """Enumerate subdomains using amass."""
            try:
                result = await self.tools["amass"].enum_subdomains(domain, passive, active)
                return [TextContent(type="text", text=f"Amass Subdomain Enumeration Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error enumerating subdomains with Amass: {str(e)}")]
    
    def _register_enumeration_tools(self):
        """Register enumeration tools."""
        
        @self.server.call_tool()
        async def enum4linux_scan(target: str, username: str = None, password: str = None) -> Sequence[TextContent]:
            """Perform SMB enumeration using enum4linux."""
            try:
                result = await self.tools["enum4linux"].enumerate_smb(target, username, password)
                return [TextContent(type="text", text=f"Enum4linux SMB Enumeration Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing SMB enumeration: {str(e)}")]
    
    def _register_ssl_network_tools(self):
        """Register SSL/network tools."""
        
        @self.server.call_tool()
        async def sslscan_scan(target: str, port: int = 443, show_certificate: bool = False) -> Sequence[TextContent]:
            """Perform SSL/TLS scan using sslscan."""
            try:
                result = await self.tools["sslscan"].scan_ssl(target, port, show_certificate)
                return [TextContent(type="text", text=f"SSLScan Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error performing SSL scan: {str(e)}")]
    
    def _register_wireless_tools(self):
        """Register wireless tools."""
        
        @self.server.call_tool()
        async def airmon_start_monitor(interface: str) -> Sequence[TextContent]:
            """Start monitor mode on wireless interface."""
            try:
                result = await self.tools["airmon-ng"].start_monitor(interface)
                return [TextContent(type="text", text=f"Airmon-ng Start Monitor Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error starting monitor mode: {str(e)}")]
    
    def _register_osint_tools(self):
        """Register OSINT tools."""
        
        @self.server.call_tool()
        async def shodan_search(query: str, limit: int = 100) -> Sequence[TextContent]:
            """Search Shodan for Internet-connected devices."""
            try:
                result = await self.tools["shodan"].search_hosts(query, limit)
                return [TextContent(type="text", text=f"Shodan Search Result:\n{result['stdout']}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error searching Shodan: {str(e)}")]
    
    async def run(self, transport_type: str = "stdio"):
        """Run the MCP server."""
        if transport_type == "stdio":
            from mcp.server.stdio import stdio_server
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(read_stream, write_stream, self.server.create_initialization_options())
        else:
            raise ValueError(f"Unsupported transport type: {transport_type}")

async def main():
    """Main entry point for the complete server."""
    server = CompletKaliMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
