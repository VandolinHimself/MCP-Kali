# Kali Linux MCP Server

A comprehensive Model Context Protocol (MCP) server that provides access to popular Kali Linux penetration testing tools through a standardized interface. This server enables AI assistants and other applications to interact with security testing tools in a structured and safe manner.

## Features

### Network Reconnaissance
- **whois**: Domain registration information lookup
- **dig**: DNS lookup utility with support for various record types
- **dnsenum**: DNS enumeration tool
- **dnsrecon**: DNS reconnaissance tool
- **nmap**: Network discovery and security auditing (port scanning, service detection, OS fingerprinting, vulnerability scanning)
- **masscan**: Mass IP port scanner
- **unicornscan**: Asynchronous network stimulus delivery engine
- **zmap**: Fast Internet-wide network scanner
- **ike-scan**: IKE/IPsec VPN scanner

### Subdomain Enumeration & OSINT
- **theHarvester**: Email, subdomain and people names harvester
- **sublist3r**: Subdomain enumeration tool
- **amass**: In-depth attack surface mapping and asset discovery
- **shodan**: Search engine for Internet-connected devices
- **recon-ng**: Full-featured reconnaissance framework
- **metagoofil**: Metadata extraction tool
- **maltego**: Link analysis and data mining application

### Web Application Analysis
- **whatweb**: Web application fingerprinting
- **wafw00f**: Web Application Firewall detection
- **dirb**: Web content scanner
- **gobuster**: Directory/File, DNS and VHost busting tool
- **feroxbuster**: Fast, simple, recursive content discovery
- **nikto**: Web server scanner
- **wfuzz**: Web application fuzzer
- **arachni**: Web application security scanner framework

### Service Enumeration
- **enum4linux**: SMB enumeration tool
- **enum4linux-ng**: Next generation SMB enumeration tool
- **smbmap**: SMB enumeration tool
- **rpcclient**: RPC client for SMB enumeration
- **snmpwalk**: SNMP enumeration tool
- **ldapsearch**: LDAP search tool

### SSL/TLS & Network Tools
- **sslscan**: SSL/TLS scanner
- **sslyze**: Fast and powerful SSL/TLS scanner
- **netcat**: Network utility for reading/writing network connections
- **curl**: Command line tool for transferring data
- **wget**: Network downloader

### Wireless Security Tools
- **airmon-ng**: Wireless interface monitor mode enabler
- **airodump-ng**: Wireless packet capture tool
- **wash**: WPS scanner
- **kismet**: Wireless network detector and intrusion detection system
- **bettercap**: Network attack and monitoring framework

## Installation

### Prerequisites
- Python 3.8 or higher
- Kali Linux (recommended) or any Linux distribution with penetration testing tools installed
- Required penetration testing tools (most come pre-installed on Kali Linux)

### Install from Source
```bash
git clone <repository-url>
cd kali-mcp-server
pip install -e .
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server
```bash
# Start the MCP server with default settings
kali-mcp-server

# Start with debug logging
kali-mcp-server --log-level DEBUG
```

### Tool Examples

#### Network Reconnaissance
```python
# WHOIS lookup
whois_lookup(domain="example.com")

# DNS lookup
dig_lookup(domain="example.com", record_type="A")
dig_reverse_lookup(ip="8.8.8.8")

# NMAP port scan
nmap_port_scan(target="192.168.1.1", ports="1-1000")
nmap_service_scan(target="192.168.1.1")
nmap_os_detection(target="192.168.1.1")
nmap_vuln_scan(target="192.168.1.1")
```

#### Web Analysis
```python
# Web fingerprinting
whatweb_analyze(url="https://example.com")

# WAF detection
wafw00f_detect(url="https://example.com")

# Directory scanning
gobuster_dir_scan(url="https://example.com")
nikto_scan(host="example.com")
```

#### Subdomain Enumeration
```python
# Subdomain discovery
sublist3r_enumerate(domain="example.com")
amass_enum_subdomains(domain="example.com", passive=True)
theharvester_subdomains(domain="example.com", sources="all")
```

## Configuration

### Tool Availability Check
The server automatically checks if tools are available on the system before execution. If a tool is not found, an appropriate error message will be returned.

### Timeouts
Different tools have different default timeouts:
- Quick scans: 60-300 seconds
- Port scans: 1800 seconds (30 minutes)
- Comprehensive scans: 3600 seconds (1 hour)

### Output Handling
All tool outputs are captured and returned in a structured format including:
- Command executed
- Return code
- Standard output
- Standard error
- Success status

## Security Considerations

⚠️ **Important Security Notes:**

1. **Authorized Use Only**: Only use this server against systems you own or have explicit permission to test
2. **Network Impact**: Some tools can generate significant network traffic
3. **System Resources**: Resource-intensive scans may impact system performance
4. **Legal Compliance**: Ensure compliance with local laws and regulations
5. **Access Control**: Implement proper access controls when deploying the server

## Development

### Project Structure
```
kali_mcp_server/
├── __init__.py
├── base.py              # Base classes and utilities
├── network_recon.py     # Network reconnaissance tools
├── subdomain_enum.py    # Subdomain enumeration tools
├── web_analysis.py      # Web analysis tools
├── enumeration.py       # Service enumeration tools
├── ssl_network.py       # SSL/TLS and network tools
├── wireless.py          # Wireless security tools
├── osint.py            # OSINT tools
├── server.py           # Main MCP server implementation
└── main.py             # CLI entry point
```

### Adding New Tools
1. Create a tool class inheriting from the appropriate base class
2. Implement the required methods
3. Register the tool in `server.py`
4. Add appropriate MCP tool handlers

### Testing
```bash
# Run basic functionality tests
python -m pytest tests/

# Test specific tool availability
python -c "from kali_mcp_server.network_recon import NmapTool; import asyncio; tool = NmapTool(); print(asyncio.run(tool.check_tool_availability()))"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This tool is for educational and authorized security testing purposes only. The developers are not responsible for any misuse or damage caused by this software. Users are solely responsible for ensuring they have proper authorization before using these tools against any systems.

## Support

For issues, feature requests, or questions:
- Open an issue on GitHub
- Check the documentation
- Review existing issues for solutions

## Changelog

### Version 1.0.0
- Initial release with support for 40+ penetration testing tools
- Comprehensive MCP server implementation
- Structured tool output and error handling
- Automatic tool availability checking
