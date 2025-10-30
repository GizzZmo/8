#!/usr/bin/env python3
import argparse
from core.layers.application import ApplicationLayer
from core.layers.presentation import PresentationLayer
from core.layers.session import SessionLayer
from core.layers.transport import TransportLayer
from core.layers.network import NetworkLayer
from core.layers.datalink import DataLinkLayer
from core.layers.physical import PhysicalLayer
from blockchain_module.transaction import Transaction

def simulate_flow(args):
    # Application layer
    if args.blockchain:
        tx = Transaction(sender="Alice", receiver="Bob", amount=10)
        app_data = tx.to_dict()
    else:
        app_data = args.data

    print("-" * 40)
    print(f"[L7 - Application] Original Data: {app_data!r}")
    app_layer = ApplicationLayer()
    data = app_layer.encapsulate(app_data)
    print("[L7 -> L6] Passing data to Presentation Layer.")
    print("-" * 40)

    # Presentation layer
    pres_layer = PresentationLayer(encrypt=args.encrypt, sign=args.sign)
    data = pres_layer.encapsulate(data)
    print("[L6 -> L5] Passing PDU to Session Layer.")
    print("-" * 40)

    # Session layer
    session_layer = SessionLayer()
    data = session_layer.encapsulate(data)
    print("[L5 -> L4] Passing PDU to Transport Layer.")
    print("-" * 40)

    # Transport layer
    transport_layer = TransportLayer(dest_port=args.port)
    data = transport_layer.encapsulate(data)
    print("[L4 -> L3] Passing Segment to Network Layer.")
    print("-" * 40)

    # Network layer
    network_layer = NetworkLayer(dest_ip=args.dest_ip)
    data = network_layer.encapsulate(data)
    print("[L3 -> L2] Passing Packet to Data Link Layer.")
    print("-" * 40)

    # Data Link layer
    datalink_layer = DataLinkLayer(dest_mac=args.dest_mac)
    data = datalink_layer.encapsulate(data)
    print("[L2 -> L1] Passing Frame to Physical Layer.")
    print("-" * 40)

    # Physical layer
    physical_layer = PhysicalLayer()
    bits = physical_layer.encapsulate(data)
    print("-" * 40)
    print("SIMULATING TRANSMISSION MEDIUM...")
    print("-" * 40)
    print("RECEIVER SIDE:")

    # Decapsulation (reverse)
    rec_data = physical_layer.decapsulate(bits)
    rec_data = datalink_layer.decapsulate(rec_data)
    rec_data = network_layer.decapsulate(rec_data)
    rec_data = transport_layer.decapsulate(rec_data)
    rec_data = session_layer.decapsulate(rec_data)
    rec_data = pres_layer.decapsulate(rec_data)
    rec_data = app_layer.decapsulate(rec_data)
    print(f"[L7 - Application] Decapsulated Data Received: {rec_data!r}")
    print("-" * 40)
    print("SIMULATION COMPLETE.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSI Model Data Flow Simulation")
    parser.add_argument('--data', type=str, default="Hello OSI World", help="Application data")
    parser.add_argument('--dest_ip', type=str, default="192.168.1.100")
    parser.add_argument('--dest_mac', type=str, default="00:1A:2B:3C:4D:5E")
    parser.add_argument('--port', type=int, default=80)
    parser.add_argument('--encrypt', action='store_true')
    parser.add_argument('--sign', action='store_true')
    parser.add_argument('--blockchain', action='store_true', help="Simulate blockchain transaction as data")
    args = parser.parse_args()
    simulate_flow(args)
