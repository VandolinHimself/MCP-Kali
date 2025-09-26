"""SSL/TLS and network tools for Kali MCP Server."""

from typing import Dict, List, Optional, Any
from .base import NetworkReconTool, ToolExecutionError

class SslscanTool(NetworkReconTool):
    """SSL/TLS scanner."""
    
    def __init__(self):
        super().__init__("sslscan", "SSL/TLS scanner")
    
    async def scan_ssl(self, target: str, port: int = 443, show_certificate: bool = False) -> Dict[str, Any]:
        """Scan SSL/TLS configuration."""
        args = [f"{target}:{port}"]
        if show_certificate:
            args.append("--show-certificate")
        return await self.execute_command(args, timeout=300)

class SslyzeTool(NetworkReconTool):
    """Fast and powerful SSL/TLS scanner."""
    
    def __init__(self):
        super().__init__("sslyze", "Fast and powerful SSL/TLS scanner")
    
    async def scan_ssl(self, target: str, port: int = 443, scan_commands: Optional[List[str]] = None) -> Dict[str, Any]:
        """Scan SSL/TLS configuration with sslyze."""
        args = [f"{target}:{port}"]
        if scan_commands:
            for cmd in scan_commands:
                args.append(f"--{cmd}")
        else:
            args.extend(["--regular"])
        return await self.execute_command(args, timeout=300)

class NetcatTool(NetworkReconTool):
    """Network utility for reading/writing network connections."""
    
    def __init__(self):
        super().__init__("nc", "Network utility for reading/writing network connections")
    
    async def port_scan(self, target: str, port_range: str, timeout: int = 5) -> Dict[str, Any]:
        """Scan ports using netcat."""
        args = ["-z", "-v", "-w", str(timeout), target, port_range]
        return await self.execute_command(args, timeout=300)
    
    async def banner_grab(self, target: str, port: int, timeout: int = 5) -> Dict[str, Any]:
        """Grab banner from service."""
        args = ["-v", "-w", str(timeout), target, str(port)]
        return await self.execute_command(args, timeout=60)
    
    async def listen_port(self, port: int, verbose: bool = True) -> Dict[str, Any]:
        """Listen on a specific port."""
        args = ["-l"]
        if verbose:
            args.append("-v")
        args.extend(["-p", str(port)])
        return await self.execute_command(args, timeout=3600)

class CurlTool(NetworkReconTool):
    """Command line tool for transferring data."""
    
    def __init__(self):
        super().__init__("curl", "Command line tool for transferring data")
    
    async def http_request(self, url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None, 
                          data: Optional[str] = None, follow_redirects: bool = True) -> Dict[str, Any]:
        """Make HTTP request."""
        args = ["-i"]  # Include headers in output
        if follow_redirects:
            args.append("-L")
        args.extend(["-X", method])
        
        if headers:
            for key, value in headers.items():
                args.extend(["-H", f"{key}: {value}"])
        
        if data and method in ["POST", "PUT", "PATCH"]:
            args.extend(["-d", data])
        
        args.append(url)
        return await self.execute_command(args, timeout=300)
    
    async def check_ssl_cert(self, url: str) -> Dict[str, Any]:
        """Check SSL certificate information."""
        args = ["-I", "--cert-status", url]
        return await self.execute_command(args, timeout=60)

class WgetTool(NetworkReconTool):
    """Network downloader."""
    
    def __init__(self):
        super().__init__("wget", "Network downloader")
    
    async def download_file(self, url: str, output_dir: Optional[str] = None, user_agent: Optional[str] = None) -> Dict[str, Any]:
        """Download file from URL."""
        args = ["--no-check-certificate"]
        if output_dir:
            args.extend(["-P", output_dir])
        if user_agent:
            args.extend(["--user-agent", user_agent])
        args.append(url)
        return await self.execute_command(args, timeout=1800)
    
    async def spider_website(self, url: str, max_depth: int = 2) -> Dict[str, Any]:
        """Spider website to discover URLs."""
        args = ["--spider", "--recursive", f"--level={max_depth}", "--no-parent", url]
        return await self.execute_command(args, timeout=1800)






