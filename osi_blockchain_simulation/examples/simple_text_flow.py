#!/usr/bin/env python3
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_simulation import simulate_flow

simulate_flow(data="Hello OSI World")
