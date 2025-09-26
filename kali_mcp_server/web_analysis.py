"""Web analysis and directory enumeration tools for Kali MCP Server."""

from typing import Dict, List, Optional, Any
from .base import WebAnalysisTool, ToolExecutionError

class WhatwebTool(WebAnalysisTool):
    """Web application fingerprinting tool."""
    
    def __init__(self):
        super().__init__("whatweb", "Web application fingerprinting tool")
    
    async def analyze_website(self, url: str, aggression: int = 1, format_output: str = "brief") -> Dict[str, Any]:
        """Analyze website technology stack."""
        args = ["-a", str(aggression), "--format", format_output, url]
        return await self.execute_command(args, timeout=300)

class Wafw00fTool(WebAnalysisTool):
    """Web Application Firewall detection tool."""
    
    def __init__(self):
        super().__init__("wafw00f", "Web Application Firewall detection tool")
    
    async def detect_waf(self, url: str) -> Dict[str, Any]:
        """Detect Web Application Firewall."""
        args = [url]
        return await self.execute_command(args, timeout=300)

class DirbTool(WebAnalysisTool):
    """Web Content Scanner."""
    
    def __init__(self):
        super().__init__("dirb", "Web Content Scanner")
    
    async def directory_scan(self, url: str, wordlist: Optional[str] = None, extensions: Optional[str] = None) -> Dict[str, Any]:
        """Scan for directories and files."""
        args = [url]
        if wordlist:
            args.append(wordlist)
        else:
            args.append("/usr/share/dirb/wordlists/common.txt")
        if extensions:
            args.extend(["-X", extensions])
        return await self.execute_command(args, timeout=1800)

class GobusterTool(WebAnalysisTool):
    """Directory/File, DNS and VHost busting tool."""
    
    def __init__(self):
        super().__init__("gobuster", "Directory/File, DNS and VHost busting tool")
    
    async def directory_scan(self, url: str, wordlist: Optional[str] = None, extensions: Optional[str] = None, threads: int = 10) -> Dict[str, Any]:
        """Scan for directories and files."""
        args = ["dir", "-u", url, "-t", str(threads)]
        if wordlist:
            args.extend(["-w", wordlist])
        else:
            args.extend(["-w", "/usr/share/wordlists/dirb/common.txt"])
        if extensions:
            args.extend(["-x", extensions])
        return await self.execute_command(args, timeout=1800)
    
    async def dns_scan(self, domain: str, wordlist: Optional[str] = None, threads: int = 10) -> Dict[str, Any]:
        """Scan for subdomains."""
        args = ["dns", "-d", domain, "-t", str(threads)]
        if wordlist:
            args.extend(["-w", wordlist])
        else:
            args.extend(["-w", "/usr/share/wordlists/dirb/common.txt"])
        return await self.execute_command(args, timeout=1800)
    
    async def vhost_scan(self, url: str, wordlist: Optional[str] = None, threads: int = 10) -> Dict[str, Any]:
        """Scan for virtual hosts."""
        args = ["vhost", "-u", url, "-t", str(threads)]
        if wordlist:
            args.extend(["-w", wordlist])
        else:
            args.extend(["-w", "/usr/share/wordlists/dirb/common.txt"])
        return await self.execute_command(args, timeout=1800)

class FeroxbusterTool(WebAnalysisTool):
    """Fast, simple, recursive content discovery tool."""
    
    def __init__(self):
        super().__init__("feroxbuster", "Fast, simple, recursive content discovery tool")
    
    async def directory_scan(self, url: str, wordlist: Optional[str] = None, extensions: Optional[str] = None, threads: int = 50) -> Dict[str, Any]:
        """Scan for directories and files recursively."""
        args = ["-u", url, "-t", str(threads)]
        if wordlist:
            args.extend(["-w", wordlist])
        if extensions:
            args.extend(["-x", extensions])
        return await self.execute_command(args, timeout=1800)

class NiktoTool(WebAnalysisTool):
    """Web server scanner."""
    
    def __init__(self):
        super().__init__("nikto", "Web server scanner")
    
    async def scan_website(self, host: str, port: Optional[int] = None, ssl: bool = False) -> Dict[str, Any]:
        """Scan website for vulnerabilities."""
        args = ["-h", host]
        if port:
            args.extend(["-p", str(port)])
        if ssl:
            args.append("-ssl")
        return await self.execute_command(args, timeout=1800)

class WfuzzTool(WebAnalysisTool):
    """Web application fuzzer."""
    
    def __init__(self):
        super().__init__("wfuzz", "Web application fuzzer")
    
    async def fuzz_directories(self, url: str, wordlist: Optional[str] = None, hide_codes: Optional[str] = None) -> Dict[str, Any]:
        """Fuzz directories in URL."""
        args = ["-c"]
        if hide_codes:
            args.extend(["--hc", hide_codes])
        if wordlist:
            args.extend(["-w", wordlist])
        else:
            args.extend(["-w", "/usr/share/wordlists/dirb/common.txt"])
        args.append(url.replace("FUZZ", "FUZZ") if "FUZZ" in url else f"{url}/FUZZ")
        return await self.execute_command(args, timeout=1800)
    
    async def fuzz_parameters(self, url: str, wordlist: Optional[str] = None, method: str = "GET") -> Dict[str, Any]:
        """Fuzz parameters in URL."""
        args = ["-c", "-X", method]
        if wordlist:
            args.extend(["-w", wordlist])
        else:
            args.extend(["-w", "/usr/share/wordlists/dirb/common.txt"])
        args.append(url)
        return await self.execute_command(args, timeout=1800)

class ArachniTool(WebAnalysisTool):
    """Web Application Security Scanner Framework."""
    
    def __init__(self):
        super().__init__("arachni", "Web Application Security Scanner Framework")
    
    async def scan_website(self, url: str, scope_include: Optional[str] = None, scope_exclude: Optional[str] = None) -> Dict[str, Any]:
        """Perform comprehensive web application security scan."""
        args = [url]
        if scope_include:
            args.extend(["--scope-include-pattern", scope_include])
        if scope_exclude:
            args.extend(["--scope-exclude-pattern", scope_exclude])
        return await self.execute_command(args, timeout=3600)






