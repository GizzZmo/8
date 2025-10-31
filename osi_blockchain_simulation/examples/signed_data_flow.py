#!/usr/bin/env python3
import sys
import os
import argparse

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_simulation import simulate_flow

# Create an args object similar to what argparse would create
args = argparse.Namespace(
    data="Signed Message",
    dest_ip="192.168.1.100",
    dest_mac="00:1A:2B:3C:4D:5E",
    port=80,
    encrypt=False,
    sign=True,
    blockchain=False
)

simulate_flow(args)
