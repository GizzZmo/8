# OSI Model Data Flow Simulation

## Overview
This is a Python-based simulation of data flow through the seven layers of the OSI (Open Systems Interconnection) model. It demonstrates:

- **Layered Architecture**: The distinct roles and functions of each OSI layer
- **Encapsulation**: How data from an upper layer is wrapped with headers/trailers
- **Decapsulation**: The reverse process of unwrapping data
- **Protocol Data Units (PDUs)**: Named data units at each layer
- **Verification**: Basic data integrity checks and digital signature verification
- **Cryptography**: Simplified encryption/decryption at the Presentation Layer
- **Blockchain Integration**: Conceptual handling of blockchain transactions as application data

## Features

- **Seven-Layer Simulation**: Models Application, Presentation, Session, Transport, Network, Data Link, and Physical layers
- **PDU Transformation**: Shows creation and modification of PDUs at each layer
- **Configurable Scenarios**: Allows users to define input data and network parameters
- **Text-Based Visualization**: Detailed logs of encapsulation/decapsulation processes
- **Verification Mechanisms**: Checksums and digital signatures for data integrity
- **Cryptographic Operations**: Simple XOR encryption/decryption at L6
- **Blockchain Module**: Simplified Transaction and Block structures

## Project Structure

```
osi_blockchain_simulation/
├── main_simulation.py          # Main executable script
├── core/                       # Core OSI simulation logic
│   ├── pdu.py                 # PDU class definitions
│   ├── crypto_utils.py        # Cryptographic utilities
│   ├── verification_utils.py  # Verification utilities
│   └── layers/                # OSI layer implementations
│       ├── application.py     # L7: Application Layer
│       ├── presentation.py    # L6: Presentation Layer
│       ├── session.py         # L5: Session Layer
│       ├── transport.py       # L4: Transport Layer
│       ├── network.py         # L3: Network Layer
│       ├── datalink.py        # L2: Data Link Layer
│       └── physical.py        # L1: Physical Layer
├── blockchain_module/         # Blockchain components
│   ├── transaction.py         # Transaction class
│   └── block.py              # Block class
└── examples/                  # Example scenarios
    ├── simple_text_flow.py    # Basic text transfer
    ├── encrypted_data_flow.py # Encrypted data transfer
    ├── signed_data_flow.py    # Signed data transfer
    └── blockchain_flow.py     # Blockchain transaction flow
```

## Prerequisites

- Python 3.8+

## Installation

1. Navigate to the simulation directory:
   ```bash
   cd osi_blockchain_simulation
   ```

## Usage

### Running the Main Simulation

```bash
python main_simulation.py --data "Hello World"
```

### Command-Line Options

- `--data <string>`: Application data to send (default: "Hello OSI World")
- `--dest_ip <ip>`: Destination IP address (default: "192.168.1.100")
- `--dest_mac <mac>`: Destination MAC address (default: "00:1A:2B:3C:4D:5E")
- `--port <number>`: Destination port (default: 80)
- `--encrypt`: Enable Presentation Layer encryption
- `--sign`: Enable digital signing
- `--blockchain`: Simulate blockchain transaction as data

### Example Commands

1. **Simple text transmission:**
   ```bash
   python main_simulation.py --data "Hello OSI World"
   ```

2. **Encrypted transmission:**
   ```bash
   python main_simulation.py --data "Secret Message" --encrypt
   ```

3. **Signed transmission:**
   ```bash
   python main_simulation.py --data "Important Data" --sign
   ```

4. **Blockchain transaction:**
   ```bash
   python main_simulation.py --blockchain
   ```

5. **Combined encryption and signing:**
   ```bash
   python main_simulation.py --data "Secure Data" --encrypt --sign
   ```

### Running Example Scenarios

```bash
python examples/simple_text_flow.py
python examples/encrypted_data_flow.py
python examples/signed_data_flow.py
python examples/blockchain_flow.py
```

## Understanding the Output

The simulation displays detailed logs showing:

1. **Sender Side**: Data encapsulation through layers L7→L1
2. **Transmission**: Simulated medium transfer
3. **Receiver Side**: Data decapsulation through layers L1→L7

Each layer shows:
- Layer name and number
- Headers/trailers added or removed
- Data transformation (encryption, encoding, etc.)
- Verification results (checksums, signatures)

## Example Output

```
----------------------------------------
[L7 - Application] Original Data: 'Hello OSI World'
[L7 -> L6] Passing data to Presentation Layer.
----------------------------------------
[L6 - Presentation] ...
[L6 -> L5] Passing PDU to Session Layer.
----------------------------------------
...
SIMULATING TRANSMISSION MEDIUM...
----------------------------------------
RECEIVER SIDE:
[L1 - Physical] Received bits: ...
...
[L7 - Application] Final Data Received: 'Hello OSI World'
----------------------------------------
SIMULATION COMPLETE.
```

## License

This project is part of the repository and follows its license terms.

## Acknowledgements

- Inspired by the OSI model framework
- Educational tool for understanding network protocols
- Demonstrates layered architecture principles
