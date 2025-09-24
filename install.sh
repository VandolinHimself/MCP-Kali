#!/bin/bash
# Installation script for Kali MCP Server

set -e

echo "🔧 Installing Kali MCP Server..."

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ This server is designed for Linux systems (preferably Kali Linux)"
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "✅ Python $python_version detected"
else
    echo "❌ Python 3.8 or higher required. Found: $python_version"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Install the package in development mode
echo "🔧 Installing Kali MCP Server in development mode..."
pip3 install -e .

# Check tool availability
echo "🔍 Checking tool availability..."

tools=("whois" "dig" "nmap" "curl" "wget" "netcat" "sslscan" "whatweb" "gobuster" "nikto" "sublist3r")
missing_tools=()

for tool in "${tools[@]}"; do
    if command -v "$tool" &> /dev/null; then
        echo "✅ $tool found"
    else
        echo "⚠️  $tool not found"
        missing_tools+=("$tool")
    fi
done

# Install missing tools (Debian/Ubuntu/Kali)
if [ ${#missing_tools[@]} -gt 0 ]; then
    echo "📦 Installing missing tools..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        for tool in "${missing_tools[@]}"; do
            case $tool in
                "whatweb")
                    sudo apt-get install -y whatweb
                    ;;
                "gobuster")
                    sudo apt-get install -y gobuster
                    ;;
                "nikto")
                    sudo apt-get install -y nikto
                    ;;
                "sublist3r")
                    sudo apt-get install -y sublist3r
                    ;;
                "sslscan")
                    sudo apt-get install -y sslscan
                    ;;
                *)
                    echo "⚠️  Please manually install: $tool"
                    ;;
            esac
        done
    else
        echo "⚠️  Please manually install missing tools: ${missing_tools[*]}"
    fi
fi

echo "✅ Installation complete!"
echo ""
echo "🚀 To start the server:"
echo "   kali-mcp-server"
echo ""
echo "📖 For more information, see README.md"

