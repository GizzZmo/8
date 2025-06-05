***OSI Model Data Flow Simulation with Verification, Crypto, and Conceptual Blockchain Integration***

This document outlines the project structure, setup, and usage for an advanced OSI model data flow simulation. 
This simulation aims to demonstrate not only the standard encapsulation/decapsulation process through the seven layers but also incorporates concepts of data verification, cryptographic operations (at the Presentation Layer), and a conceptual handling of blockchain-like transactions as application data.1. README.md# OSI Model Data Flow Simulation with Verification, Crypto & Conceptual Blockchain

## Project Overview

This project provides a Python-based simulation of data flow through the seven layers of the OSI (Open Systems Interconnection) model. It aims to be an educational tool to visualize and understand:

* **Layered Architecture:** The distinct roles and functions of each OSI layer.
* **Encapsulation:** How data from an upper layer is wrapped with headers (and trailers) as it descends the stack.
* **Decapsulation:** The reverse process of unwrapping data as it ascends the stack on the receiver side.
* **Protocol Data Units (PDUs):** The named data units at each layer (Data, Segment, Packet, Frame, Bits).
* **Verification:** Basic data integrity checks and conceptual digital signature verification.
* **Cryptography:** Simplified encryption/decryption at the Presentation Layer (L6).
* **Conceptual Blockchain Data Handling:** How data structured as a blockchain transaction can be processed and transported through the OSI stack as application-level data.

**Note:** The blockchain component is highly conceptual and simplified. It does *not* implement a full blockchain network, consensus mechanism, or complex cryptographic primitives typically found in production blockchains. Its purpose is to illustrate how application-specific data, such as a transaction, is handled by the underlying network layers.

This simulation primarily uses Python and draws conceptual inspiration from Scapy for packet structure and manipulation, but aims for a from-scratch implementation of layer logic for clarity.

## Features

* **Seven-Layer Simulation:** Models Application, Presentation, Session, Transport, Network, Data Link, and Physical layers.
* **PDU Transformation:** Shows creation and modification of PDUs at each layer.
* **Configurable Scenarios:** Allows users to define input data and basic network parameters for simulation.
* **Text-Based Visualization:** Outputs detailed logs of encapsulation and decapsulation processes at each layer.
* **Verification Mechanisms:**
    * Checksums for data integrity (e.g., at Transport or Data Link layers).
    * Conceptual digital signature handling (sign at sender, verify at receiver) for data authenticity at the Presentation or Application layer.
* **Cryptographic Operations (Presentation Layer - L6):**
    * Simplified data encryption (e.g., Caesar cipher, XOR cipher, or AES if `cryptography` library is used).
    * Simplified data decryption.
* **Conceptual Blockchain Module:**
    * Define `Transaction` and `Block` (simplified) structures.
    * Simulate a transaction as application data.
    * Show this "blockchain transaction data" being passed through the OSI stack.

## Project Structure

(See `FILELIST_DESCRIPTION.md` or Section 2 of the main project documentation for a detailed file structure.)

Briefly:
* `main_simulation.py`: Main script to run simulations.
* `core/`: Contains PDU definitions and layer logic.
    * `pdu.py`: Base PDU classes.
    * `layers/`: Modules for each OSI layer.
    * `crypto_utils.py`: Cryptographic helper functions.
    * `verification_utils.py`: Verification helper functions.
* `blockchain_module/`: Simplified classes for `Transaction`, `Block`.
* `examples/`: Example scripts demonstrating different simulation scenarios.
* `tests/`: Unit tests for different components.

## Prerequisites

* Python 3.8+
* (Optional but recommended for crypto) `cryptography` library: `pip install cryptography`

## Installation

1.  Clone the repository:
    ```bash
    git clone <your-repository-url>
    cd osi-simulation-advanced
    ```
2.  (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install dependencies (if any beyond standard Python, like `cryptography`):
    ```bash
    pip install -r requirements.txt
    ```
    (`requirements.txt` should list `cryptography` if used).

## Usage

Run simulations using `main_simulation.py` or by executing scripts from the `examples/` directory.

```bash
python main_simulation.py --data "Hello OSI World" --dest_ip "192.168.1.100" --dest_mac "00:1A:2B:3C:4D:5E" --port 80
See HOW_TO_RUN_WIKI.md (or Section 3) for detailed examples and command-line options.Example scenarios in examples/:simple_text_flow.py: Simulates basic text data transfer.encrypted_data_flow.py: Simulates text data with Presentation Layer encryption.signed_data_flow.py: Simulates data with a conceptual digital signature.blockchain_transaction_flow.py: Simulates sending a simplified blockchain transaction as application data.How to ContributeContributions are welcome! Please follow these steps:Fork the repository.Create a new branch (git checkout -b feature/your-feature-name).Make your changes.Write unit tests for your changes.Ensure all tests pass (python -m unittest discover tests).Commit your changes (git commit -m 'Add some feature').Push to the branch (git push origin feature/your-feature-name).Open a Pull Request.Please read CONTRIBUTING.md for more details on coding standards and contribution guidelines.LicenseThis project is licensed under the MIT License - see the LICENSE file for details.AcknowledgementsInspired by the conceptual framework of the OSI model.Utilizes Python for its clear syntax and suitability for educational simulations.
## 2. Filelist Description

This section describes the intended project structure and the purpose of each file/directory.

osi_blockchain_simulation/├── .gitignore                 # Specifies intentionally untracked files that Git should ignore.├── LICENSE                    # Contains the project's license (e.g., MIT License).├── README.md                  # This file: Overview, features, setup, usage.├── HOW_TO_RUN_WIKI.md         # Detailed instructions and examples for running the simulation.├── requirements.txt           # Lists Python package dependencies (e.g., cryptography).│├── main_simulation.py         # Main executable script to run simulations with command-line arguments.│                              # Orchestrates the sending and receiving process.│├── core/                      # Core logic for the OSI simulation.│   ├── init.py            # Makes the 'core' directory a Python package.│   ├── pdu.py                 # Defines base PDU classes and common data structures used across layers.│   │                          # E.g., BaseHeader, BasePDU.│   ├── layers/                # Modules representing each OSI layer.│   │   ├── init.py        # Makes 'layers' a Python package.│   │   ├── physical_layer.py  # L1: Simulates conversion to/from bitstream.│   │   ├── datalink_layer.py  # L2: Simulates framing, MAC addressing, L2 error detection (e.g., dummy FCS).│   │   ├── network_layer.py   # L3: Simulates IP addressing, basic routing concept (e.g., next hop).│   │   ├── transport_layer.py # L4: Simulates TCP/UDP-like segmentation, port numbers, sequence/ack (conceptual).│   │   ├── session_layer.py   # L5: Simulates session establishment/teardown (conceptual, e.g., session ID).│   │   ├── presentation_layer.py # L6: Simulates data formatting, encryption/decryption, compression (conceptual).│   │   │                        # Interacts with crypto_utils.py and verification_utils.py.│   │   └── application_layer.py # L7: Handles initial user data, interface to applications.│   ││   ├── crypto_utils.py        # Utility functions for cryptographic operations.│   │                          # E.g., encrypt_data(), decrypt_data(), generate_hash(), simple_sign(), simple_verify_signature().│   │                          # Might use the 'cryptography' library or implement very simple ciphers.│   ││   └── verification_utils.py  # Utility functions for data verification.│                              # E.g., calculate_checksum(), verify_checksum(), verify_digital_signature_conceptual().│├── blockchain_module/           # Simplified, conceptual blockchain components.│   ├── init.py            # Makes 'blockchain_module' a Python package.│   ├── transaction.py         # Defines a simplified Transaction class (e.g., sender, receiver, value, timestamp).│   ├── block.py               # Defines a simplified Block class (e.g., list of transactions, previous_hash, nonce - conceptual).│   └── ledger.py              # (Optional) A very simple representation of a list of blocks to form a chain.│                              # Not a fully functional ledger, but data structures for simulation.│├── examples/                  # Example scripts demonstrating various simulation scenarios.│   ├── init.py            #│   ├── simple_text_flow.py    # Demonstrates basic data flow without crypto or blockchain elements.│   ├── encrypted_data_flow.py # Demonstrates data flow with Presentation Layer encryption.│   ├── signed_data_flow.py    # Demonstrates data flow with conceptual digital signing/verification.│   └── blockchain_transaction_flow.py # Demonstrates sending a simplified blockchain transaction│                                    # as application data through the OSI stack.│└── tests/                     # Unit tests for various modules.├── init.py            # Makes 'tests' a Python package.├── test_pdu.py            # Tests for PDU structures and manipulations.├── test_layers.py         # Tests for individual layer encapsulation/decapsulation logic.├── test_crypto_utils.py   # Tests for cryptographic functions.├── test_verification_utils.py # Tests for verification functions.└── test_blockchain_module.py # Tests for the simplified blockchain data structures.
## 3. HOW_TO_RUN_WIKI.md

```markdown
# How to Run the OSI Model Simulation

This guide provides detailed instructions on how to set up your environment, run the OSI model simulation, and interpret its output.

## 1. Prerequisites

* **Python 3.8+**: Ensure you have a compatible Python version installed. You can check with `python --version`.
* **Git**: For cloning the repository.
* **(Optional but Recommended for Crypto)** `cryptography` library:
    ```bash
    pip install cryptography
    ```
    If you don't want to use this, the simulation might fall back to simpler, custom crypto functions.

## 2. Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd osi-simulation-advanced
    ```

2.  **(Optional) Create and Activate a Virtual Environment:**
    This is recommended to manage project dependencies separately.
    ```bash
    python -m venv venv
    ```
    * On macOS/Linux: `source venv/bin/activate`
    * On Windows: `venv\Scripts\activate`

3.  **Install Dependencies:**
    If a `requirements.txt` file is provided (it should list `cryptography` if used):
    ```bash
    pip install -r requirements.txt
    ```

## 3. Running Simulations

Simulations can be run either via the main script `main_simulation.py` with command-line arguments or by directly executing pre-configured scenarios from the `examples/` directory.

### 3.1. Using `main_simulation.py`

The `main_simulation.py` script allows for flexible configuration of a single data transmission.

**Command-Line Options (Illustrative):**

* `--data <string>`: The application data to send (e.g., "Hello World"). (Required)
* `--dest_ip <ip_address>`: Destination IP address (e.g., "192.168.1.2"). (Default: "192.168.0.2")
* `--source_ip <ip_address>`: Source IP address (e.g., "192.168.1.1"). (Default: "192.168.0.1")
* `--dest_mac <mac_address>`: Destination MAC address (e.g., "00:AA:BB:CC:DD:EE"). (Default: "00:00:00:00:00:02")
* `--source_mac <mac_address>`: Source MAC address (e.g., "00:11:22:33:44:55"). (Default: "00:00:00:00:00:01")
* `--port <port_number>`: Destination port number for Transport Layer. (Default: 80)
* `--transport_protocol <TCP|UDP>`: Transport layer protocol. (Default: TCP)
* `--encrypt <true|false>`: Enable/disable Presentation Layer encryption. (Default: false)
* `--sign <true|false>`: Enable/disable conceptual data signing. (Default: false)
* `--verbose <true|false>`: Enable verbose output. (Default: true)

**Example Command:**

```bash
python main_simulation.py --data "Secure Message" --dest_ip "10.0.0.99" --port 443 --encrypt true --sign true
3.2. Running Example ScenariosThe examples/ directory contains Python scripts that demonstrate specific simulation flows. To run them, navigate to the project root and execute the desired script:Simple Text Data Flow:Demonstrates basic encapsulation and decapsulation of plain text.python examples/simple_text_flow.py
Encrypted Data Flow:Shows data being encrypted at the Presentation Layer of the sender and decrypted at the receiver.python examples/encrypted_data_flow.py
You might need to provide a simple key or see it hardcoded in the example for simplicity.Signed Data Flow (Conceptual):Illustrates how data could be conceptually signed (e.g., a hash is created and attached) and then verified.python examples/signed_data_flow.py
Blockchain Transaction Data Flow:Simulates sending a simplified blockchain transaction object as application data. This demonstrates how such structured data is handled by the OSI stack, not a functional blockchain operation.python examples/blockchain_transaction_flow.py
3.3. Interpreting the OutputThe simulation will print detailed logs to the console, showing the state of the data at each layer during both encapsulation (sender side) and decapsulation (receiver side).Example Output Snippet (Conceptual):SENDER SIDE:
----------------------------------------
[L7 - Application] Original Data: "Hello"
[L7 -> L6] Passing data to Presentation Layer.
----------------------------------------
[L6 - Presentation] Applying encryption. Header: {encryption_type: AES_mock}
[L6 - Presentation] Encrypted Payload: "XyZ123" (mock)
[L6 -> L5] Passing PDU to Session Layer.
----------------------------------------
[L5 - Session] Adding Session Header. Header: {session_id: 12345}
[L5 -> L4] Passing PDU to Transport Layer.
----------------------------------------
[L4 - Transport] Segmenting Data. Protocol: TCP. Header: {src_port: 1024, dst_port: 80, seq: 0, ack: 0}
[L4 -> L3] Passing Segment to Network Layer.
----------------------------------------
[L3 - Network] Adding IP Header. Header: {src_ip: 192.168.0.1, dst_ip: 192.168.0.2, protocol: 6}
[L3 -> L2] Passing Packet to Data Link Layer.
----------------------------------------
[L2 - Data Link] Adding Ethernet Header/Trailer. Header: {src_mac: 00:00:00:00:00:01, dst_mac: 00:00:00:00:00:02, type: 0x0800}, Trailer: {fcs: 0xABCDE} (mock)
[L2 -> L1] Passing Frame to Physical Layer.
----------------------------------------
[L1 - Physical] Transmitting bits: 0110100001100101011011000110110001101111... (representing the frame)
----------------------------------------

SIMULATING TRANSMISSION MEDIUM...

RECEIVER SIDE:
----------------------------------------
[L1 - Physical] Received bits: 0110100001100101011011000110110001101111...
[L1 -> L2] Passing Frame to Data Link Layer.
----------------------------------------
[L2 - Data Link] Received Frame. Header: {src_mac: ..., dst_mac: ...}, Trailer: {fcs: ...}
[L2 - Data Link] MAC address matches. FCS check OK (conceptual). Stripping L2 Header/Trailer.
[L2 -> L3] Passing Packet to Network Layer.
----------------------------------------
[L3 - Network] Received Packet. Header: {src_ip: ..., dst_ip: ...}
[L3 - Network] IP address matches. Stripping L3 Header.
[L3 -> L4] Passing Segment to Transport Layer.
----------------------------------------
[L4 - Transport] Received Segment. Header: {src_port: ..., dst_port: ...}
[L4 - Transport] Port number matches listening application. Reassembling (if applicable). Stripping L4 Header.
[L4 -> L5] Passing Data to Session Layer.
----------------------------------------
[L5 - Session] Received Session PDU. Header: {session_id: 12345}
[L5 - Session] Session validated. Stripping L5 Header.
[L5 -> L6] Passing Data to Presentation Layer.
----------------------------------------
[L6 - Presentation] Received Presentation PDU. Header: {encryption_type: AES_mock}, Encrypted Payload: "XyZ123"
[L6 - Presentation] Decrypting data.
[L6 - Presentation] Original Data: "Hello"
[L6 -> L7] Passing Data to Application Layer.
----------------------------------------
[L7 - Application] Final Data Received: "Hello"
----------------------------------------
SIMULATION COMPLETE.
Pay attention to:The PDU names (Data, Segment, Packet, Frame) at each layer.The headers added at each layer and their (simplified) contents.The payload at each layer, showing how it's the PDU from the layer above.Specific messages about encryption/decryption or signing/verification if those features are enabled.How blockchain Transaction objects are treated as ApplicationData and passed down.4. TroubleshootingPython Version: Ensure you are using Python 3.8 or newer.Dependencies: Make sure all libraries listed in requirements.txt (especially cryptography) are installed correctly in your active Python environment.File Paths: If running scripts directly, ensure you are in the project's root directory so that module imports work correctly.Verbose Output: If --verbose false is used with main_simulation.py, the detailed layer-by-layer breakdown might be suppressed. Run with verbose mode for debugging.For further issues, please check the project's issue tracker on GitHub or consult the main README.md.
This provides a comprehensive set of documentation to guide the development and usage of the OSI model simulation with the requested advanced features. Remember that the actual implementation of the cryptographic and especially the blockchain components will require careful design to keep them illustrative and manageable within the scope of an OSI educational tool.
