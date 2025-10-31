#!/usr/bin/env python3
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.argv = ['main_simulation.py', '--data', 'Hello OSI World']
import main_simulation
main_simulation.main()
