"""OSINT (Open Source Intelligence) tools for Kali MCP Server."""

from typing import Dict, List, Optional, Any
from .base import OSINTTool, ToolExecutionError
import json

class ShodanTool(OSINTTool):
    """Shodan search engine for Internet-connected devices."""
    
    def __init__(self):
        super().__init__("shodan", "Shodan search engine for Internet-connected devices")
    
    async def search_hosts(self, query: str, limit: int = 100) -> Dict[str, Any]:
        """Search for hosts using Shodan."""
        args = ["search", "--limit", str(limit), query]
        return await self.execute_command(args, timeout=300)
    
    async def host_info(self, ip: str) -> Dict[str, Any]:
        """Get information about a specific host."""
        args = ["host", ip]
        return await self.execute_command(args, timeout=60)
    
    async def count_results(self, query: str) -> Dict[str, Any]:
        """Count search results for a query."""
        args = ["count", query]
        return await self.execute_command(args, timeout=60)

class ReconNgTool(OSINTTool):
    """Full-featured reconnaissance framework."""
    
    def __init__(self):
        super().__init__("recon-ng", "Full-featured reconnaissance framework")
    
    async def run_module(self, module: str, options: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Run a specific recon-ng module."""
        commands = [f"modules load {module}"]
        
        if options:
            for key, value in options.items():
                commands.append(f"options set {key} {value}")
        
        commands.append("run")
        
        # Create command file for recon-ng
        command_script = "; ".join(commands)
        args = ["-x", command_script]
        return await self.execute_command(args, timeout=600)
    
    async def list_modules(self) -> Dict[str, Any]:
        """List available modules."""
        args = ["-x", "modules search"]
        return await self.execute_command(args, timeout=60)

class MetagoofiltTool(OSINTTool):
    """Metadata extraction tool."""
    
    def __init__(self):
        super().__init__("metagoofil", "Metadata extraction tool")
    
    async def extract_metadata(self, domain: str, file_types: str = "pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx", 
                              limit: int = 100, download_dir: str = "/tmp/metagoofil") -> Dict[str, Any]:
        """Extract metadata from documents found online."""
        args = ["-d", domain, "-t", file_types, "-l", str(limit), "-o", download_dir, "-f", "results.html"]
        return await self.execute_command(args, timeout=1800)

class MaltegoTool(OSINTTool):
    """Link analysis and data mining application."""
    
    def __init__(self):
        super().__init__("maltego", "Link analysis and data mining application")
    
    async def run_transform(self, transform_name: str, entity_value: str, entity_type: str = "maltego.Domain") -> Dict[str, Any]:
        """Run a Maltego transform (requires Maltego CE or Commercial)."""
        # Note: This is a simplified example. Actual Maltego automation would require
        # the Maltego API or command-line interface setup
        args = ["--transform", transform_name, "--entity", entity_value, "--type", entity_type]
        return await self.execute_command(args, timeout=300)
    
    async def export_graph(self, graph_file: str, output_format: str = "csv") -> Dict[str, Any]:
        """Export Maltego graph to specified format."""
        args = ["--export", graph_file, "--format", output_format]
        return await self.execute_command(args, timeout=120)
