"""
path-resolver - Resolve file paths and handle cross-platform issues

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import PathResolver, resolve, process, main

__all__ = ["PathResolver", "resolve", "process", "main"]
