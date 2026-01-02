#!/usr/bin/env python3
"""
Interactive CLI Todo Application with arrow-key navigation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cli.menu import Menu


def main():
    """Main entry point"""
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()