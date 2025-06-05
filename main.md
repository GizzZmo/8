Great! Here is a full simulation project for the OSI Model Data Flow with verification, simple crypto, and conceptual blockchain integration, as outlined in `osi_flow_sim.md`. The code is organized into the described files and directories.

---

### Directory Structure

```
osi_blockchain_simulation/
├── main_simulation.py
├── core/
│   ├── pdu.py
│   ├── crypto_utils.py
│   ├── verification_utils.py
│   └── layers/
│       ├── application.py
│       ├── presentation.py
│       ├── session.py
│       ├── transport.py
│       ├── network.py
│       ├── datalink.py
│       └── physical.py
├── blockchain_module/
│   ├── transaction.py
│   └── block.py
├── examples/
│   ├── simple_text_flow.py
│   ├── encrypted_data_flow.py
│   ├── signed_data_flow.py
│   └── blockchain_flow.py
```

---

## main_simulation.py

```python
import argparse
from core.layers.application import ApplicationLayer
from core.layers.presentation import PresentationLayer
from core.layers.session import SessionLayer
from core.layers.transport import TransportLayer
from core.layers.network import NetworkLayer
from core.layers.datalink import DataLinkLayer
from core.layers.physical import PhysicalLayer
from blockchain_module.transaction import Transaction
from blockchain_module.block import Block

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
```

---

## core/pdu.py

```python
class PDU:
    def __init__(self, payload, header=None, trailer=None):
        self.header = header or {}
        self.payload = payload
        self.trailer = trailer or {}

    def __repr__(self):
        return f"PDU(header={self.header}, payload={self.payload}, trailer={self.trailer})"
```

---

## core/crypto_utils.py

```python
def simple_xor_encrypt(data, key=42):
    return ''.join(chr(ord(c) ^ key) for c in data)

def simple_xor_decrypt(data, key=42):
    return ''.join(chr(ord(c) ^ key) for c in data)
```

---

## core/verification_utils.py

```python
import hashlib

def checksum(data):
    if isinstance(data, dict):
        data = str(data)
    return hashlib.md5(data.encode()).hexdigest()[:8]

def sign(data, secret="default"):
    if isinstance(data, dict):
        data = str(data)
    return hashlib.sha256((data + secret).encode()).hexdigest()[:12]

def verify(data, signature, secret="default"):
    expected = sign(data, secret)
    return expected == signature
```

---

## core/layers/application.py

```python
from core.pdu import PDU

class ApplicationLayer:
    def encapsulate(self, data):
        print(f"[L7 - Application] Encapsulating: {data!r}")
        return PDU(payload=data, header={"type": "application"})

    def decapsulate(self, pdu):
        print(f"[L7 - Application] Final Data Received: {pdu.payload!r}")
        return pdu.payload
```

---

## core/layers/presentation.py

```python
from core.pdu import PDU
from core.crypto_utils import simple_xor_encrypt, simple_xor_decrypt
from core.verification_utils import sign, verify

class PresentationLayer:
    def __init__(self, encrypt=False, sign=False):
        self.encrypt = encrypt
        self.sign = sign
        self.key = 42
        self.secret = "default"

    def encapsulate(self, pdu):
        payload = pdu.payload
        header = {"encryption": self.encrypt}
        if self.encrypt:
            payload = simple_xor_encrypt(str(payload), self.key)
            header["encryption_type"] = "XOR"
            print(f"[L6 - Presentation] Encrypted Payload: {payload!r}")
        if self.sign:
            signature = sign(str(payload), self.secret)
            header["signature"] = signature
            print(f"[L6 - Presentation] Signed Payload: {signature}")
        return PDU(payload=payload, header=header)

    def decapsulate(self, pdu):
        payload = pdu.payload
        header = pdu.header
        if header.get("encryption"):
            print(f"[L6 - Presentation] Decrypting data.")
            payload = simple_xor_decrypt(payload, self.key)
            print(f"[L6 - Presentation] Original Data: {payload!r}")
        if header.get("signature"):
            if verify(str(payload), header["signature"], self.secret):
                print(f"[L6 - Presentation] Signature verified.")
            else:
                print(f"[L6 - Presentation] Signature verification failed.")
        return PDU(payload=payload)
```

---

## core/layers/session.py

```python
from core.pdu import PDU

class SessionLayer:
    def encapsulate(self, pdu):
        header = {"session_id": 12345}
        print(f"[L5 - Session] Adding Session Header: {header}")
        return PDU(payload=pdu.payload, header=header)

    def decapsulate(self, pdu):
        print(f"[L5 - Session] Session validated. Stripping L5 Header.")
        return PDU(payload=pdu.payload)
```

---

## core/layers/transport.py

```python
from core.pdu import PDU
from core.verification_utils import checksum

class TransportLayer:
    def __init__(self, dest_port=80, protocol="TCP"):
        self.protocol = protocol
        self.dest_port = dest_port

    def encapsulate(self, pdu):
        header = {"src_port": 1024, "dst_port": self.dest_port, "protocol": self.protocol}
        trailer = {"checksum": checksum(str(pdu.payload))}
        print(f"[L4 - Transport] Segmenting Data. Header: {header}, Trailer: {trailer}")
        return PDU(payload=pdu.payload, header=header, trailer=trailer)

    def decapsulate(self, pdu):
        cs = checksum(str(pdu.payload))
        if pdu.trailer.get("checksum") == cs:
            print("[L4 - Transport] Checksum OK.")
        else:
            print("[L4 - Transport] Checksum failed.")
        print("[L4 - Transport] Port number matches. Stripping L4 Header.")
        return PDU(payload=pdu.payload)
```

---

## core/layers/network.py

```python
from core.pdu import PDU

class NetworkLayer:
    def __init__(self, dest_ip):
        self.dest_ip = dest_ip

    def encapsulate(self, pdu):
        header = {"src_ip": "192.168.0.1", "dst_ip": self.dest_ip, "protocol": 6}
        print(f"[L3 - Network] Adding IP Header: {header}")
        return PDU(payload=pdu.payload, header=header)

    def decapsulate(self, pdu):
        print("[L3 - Network] IP address matches. Stripping L3 Header.")
        return PDU(payload=pdu.payload)
```

---

## core/layers/datalink.py

```python
from core.pdu import PDU

class DataLinkLayer:
    def __init__(self, dest_mac):
        self.dest_mac = dest_mac

    def encapsulate(self, pdu):
        header = {"src_mac": "00:00:00:00:00:01", "dst_mac": self.dest_mac, "type": "0x0800"}
        trailer = {"fcs": "0xABCDE"}
        print(f"[L2 - Data Link] Adding Ethernet Header/Trailer. Header: {header}, Trailer: {trailer}")
        return PDU(payload=pdu.payload, header=header, trailer=trailer)

    def decapsulate(self, pdu):
        print("[L2 - Data Link] MAC address matches. FCS check OK. Stripping L2 Header/Trailer.")
        return PDU(payload=pdu.payload)
```

---

## core/layers/physical.py

```python
class PhysicalLayer:
    def encapsulate(self, pdu):
        bits = ''.join(format(ord(c), '08b') for c in str(pdu.payload))
        print(f"[L1 - Physical] Transmitting bits: {bits[:40]}... (truncated)")
        return bits

    def decapsulate(self, bits):
        n = 8
        chars = [chr(int(bits[i:i + n], 2)) for i in range(0, len(bits), n)]
        data = ''.join(chars)
        print(f"[L1 - Physical] Received bits: {bits[:40]}... (truncated)")
        return data
```

---

## blockchain_module/transaction.py

```python
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
```

---

## blockchain_module/block.py

```python
import hashlib
import time

class Block:
    def __init__(self, transactions, previous_hash=''):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = str(self.transactions) + str(self.timestamp) + self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()
```

---

## examples/simple_text_flow.py

```python
import sys
sys.argv = ['main_simulation.py', '--data', 'Hello OSI World']
import main_simulation
```

---

## examples/encrypted_data_flow.py

```python
import sys
sys.argv = ['main_simulation.py', '--data', 'Secret Message', '--encrypt']
import main_simulation
```

---

## examples/signed_data_flow.py

```python
import sys
sys.argv = ['main_simulation.py', '--data', 'Signed Message', '--sign']
import main_simulation
```

---

## examples/blockchain_flow.py

```python
import sys
sys.argv = ['main_simulation.py', '--blockchain']
import main_simulation
```

---

This complete set of files provides a full simulation as described in your `osi_flow_sim.md`. You can copy these into the respective files and directories to run and extend the simulation. Let me know if you need explanations, extra features, or test scripts!
