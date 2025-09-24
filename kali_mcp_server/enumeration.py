"""Enumeration tools for SMB, LDAP, SNMP, and other services."""

from typing import Dict, List, Optional, Any
from .base import EnumerationTool, ToolExecutionError

class Enum4linuxTool(EnumerationTool):
    """SMB enumeration tool."""
    
    def __init__(self):
        super().__init__("enum4linux", "SMB enumeration tool")
    
    async def enumerate_smb(self, target: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Enumerate SMB shares and information."""
        args = ["-a", target]
        if username and password:
            args.extend(["-u", username, "-p", password])
        return await self.execute_command(args, timeout=600)

class Enum4linuxNgTool(EnumerationTool):
    """Next generation SMB enumeration tool."""
    
    def __init__(self):
        super().__init__("enum4linux-ng", "Next generation SMB enumeration tool")
    
    async def enumerate_smb(self, target: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Enumerate SMB shares and information with enhanced capabilities."""
        args = ["-A", target]
        if username and password:
            args.extend(["-u", username, "-p", password])
        return await self.execute_command(args, timeout=600)

class SmbmapTool(EnumerationTool):
    """SMB enumeration tool."""
    
    def __init__(self):
        super().__init__("smbmap", "SMB enumeration tool")
    
    async def enumerate_shares(self, host: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Enumerate SMB shares."""
        args = ["-H", host]
        if username:
            args.extend(["-u", username])
        if password:
            args.extend(["-p", password])
        return await self.execute_command(args, timeout=300)
    
    async def list_files(self, host: str, share: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """List files in SMB share."""
        args = ["-H", host, "-s", share, "-R"]
        if username:
            args.extend(["-u", username])
        if password:
            args.extend(["-p", password])
        return await self.execute_command(args, timeout=600)

class RpcclientTool(EnumerationTool):
    """RPC client for SMB enumeration."""
    
    def __init__(self):
        super().__init__("rpcclient", "RPC client for SMB enumeration")
    
    async def enumerate_users(self, target: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Enumerate users via RPC."""
        args = ["-U"]
        if username and password:
            args.append(f"{username}%{password}")
        else:
            args.append("''")
        args.extend(["-c", "enumdomusers", target])
        return await self.execute_command(args, timeout=300)
    
    async def enumerate_groups(self, target: str, username: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Enumerate groups via RPC."""
        args = ["-U"]
        if username and password:
            args.append(f"{username}%{password}")
        else:
            args.append("''")
        args.extend(["-c", "enumdomgroups", target])
        return await self.execute_command(args, timeout=300)

class SnmpwalkTool(EnumerationTool):
    """SNMP enumeration tool."""
    
    def __init__(self):
        super().__init__("snmpwalk", "SNMP enumeration tool")
    
    async def walk_snmp(self, target: str, community: str = "public", version: str = "2c", oid: Optional[str] = None) -> Dict[str, Any]:
        """Walk SNMP tree."""
        args = ["-v", version, "-c", community, target]
        if oid:
            args.append(oid)
        return await self.execute_command(args, timeout=600)

class LdapsearchTool(EnumerationTool):
    """LDAP search tool."""
    
    def __init__(self):
        super().__init__("ldapsearch", "LDAP search tool")
    
    async def search_ldap(self, host: str, base_dn: str, filter_str: str = "(objectClass=*)", 
                         bind_dn: Optional[str] = None, password: Optional[str] = None) -> Dict[str, Any]:
        """Search LDAP directory."""
        args = ["-x", "-H", f"ldap://{host}", "-b", base_dn, filter_str]
        if bind_dn:
            args.extend(["-D", bind_dn])
        if password:
            args.extend(["-w", password])
        return await self.execute_command(args, timeout=600)

