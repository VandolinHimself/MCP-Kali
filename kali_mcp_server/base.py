"""Base classes and utilities for Kali MCP Server tools."""

import asyncio
import subprocess
import json
import logging
from typing import Dict, List, Optional, Any, Union
from pathlib import Path

logger = logging.getLogger(__name__)

class ToolExecutionError(Exception):
    """Exception raised when a tool execution fails."""
    pass

class BaseKaliTool:
    """Base class for all Kali Linux tools."""
    
    def __init__(self, name: str, description: str, binary_path: Optional[str] = None):
        self.name = name
        self.description = description
        self.binary_path = binary_path or name
        
    async def check_tool_availability(self) -> bool:
        """Check if the tool is available on the system."""
        try:
            result = await asyncio.create_subprocess_exec(
                'which', self.binary_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await result.communicate()
            return result.returncode == 0
        except Exception:
            return False
    
    async def execute_command(self, args: List[str], timeout: int = 300) -> Dict[str, Any]:
        """Execute a command with the given arguments."""
        if not await self.check_tool_availability():
            raise ToolExecutionError(f"Tool '{self.binary_path}' is not available on this system")
        
        full_command = [self.binary_path] + args
        logger.info(f"Executing command: {' '.join(full_command)}")
        
        try:
            process = await asyncio.create_subprocess_exec(
                *full_command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(
                process.communicate(), 
                timeout=timeout
            )
            
            return {
                "command": " ".join(full_command),
                "returncode": process.returncode,
                "stdout": stdout.decode('utf-8', errors='ignore'),
                "stderr": stderr.decode('utf-8', errors='ignore'),
                "success": process.returncode == 0
            }
            
        except asyncio.TimeoutError:
            raise ToolExecutionError(f"Command timed out after {timeout} seconds")
        except Exception as e:
            raise ToolExecutionError(f"Failed to execute command: {str(e)}")

class NetworkReconTool(BaseKaliTool):
    """Base class for network reconnaissance tools."""
    pass

class WebAnalysisTool(BaseKaliTool):
    """Base class for web analysis tools."""
    pass

class EnumerationTool(BaseKaliTool):
    """Base class for enumeration tools."""
    pass

class WirelessTool(BaseKaliTool):
    """Base class for wireless tools."""
    pass

class OSINTTool(BaseKaliTool):
    """Base class for OSINT tools."""
    pass

