#!/usr/bin/env python3
"""Setup script for Kali MCP Server."""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="kali-mcp-server",
    version="1.0.0",
    author="Kali MCP Server Team",
    author_email="admin@example.com",
    description="MCP server for Kali Linux penetration testing tools",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/example/kali-mcp-server",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "kali-mcp-server=kali_mcp_server.main:cli",
        ],
    },
    include_package_data=True,
    package_data={
        "kali_mcp_server": ["*.json"],
    },
    project_urls={
        "Bug Reports": "https://github.com/example/kali-mcp-server/issues",
        "Source": "https://github.com/example/kali-mcp-server",
        "Documentation": "https://github.com/example/kali-mcp-server/blob/main/README.md",
    },
)
