# Quick Start Guide - OSI Blockchain Simulation

## 🚀 Quick Installation

```bash
# Clone the repository
git clone https://github.com/GizzZmo/8.git
cd 8

# Checkout the feature branch
git checkout copilot/create-iso-simulation-patch

# Navigate to simulation
cd osi_blockchain_simulation
```

## 🎯 Quick Usage

### Basic Commands

```bash
# Simple text transmission
python main_simulation.py --data "Hello World"

# Encrypted transmission
python main_simulation.py --data "Secret" --encrypt

# Signed transmission
python main_simulation.py --data "Important" --sign

# Blockchain transaction
python main_simulation.py --blockchain

# Combined (encrypted + signed)
python main_simulation.py --data "Top Secret" --encrypt --sign
```

### Run Examples

```bash
python examples/simple_text_flow.py
python examples/encrypted_data_flow.py
python examples/signed_data_flow.py
python examples/blockchain_flow.py
```

## 📋 Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--data TEXT` | Application data to send | "Hello OSI World" |
| `--dest_ip IP` | Destination IP address | "192.168.1.100" |
| `--dest_mac MAC` | Destination MAC address | "00:1A:2B:3C:4D:5E" |
| `--port NUM` | Destination port | 80 |
| `--encrypt` | Enable encryption | False |
| `--sign` | Enable signing | False |
| `--blockchain` | Use blockchain transaction | False |

## 📁 Project Structure

```
osi_blockchain_simulation/
├── main_simulation.py          # Main script
├── core/                       # Core logic
│   ├── layers/                # 7 OSI layers
│   ├── pdu.py                 # PDU class
│   ├── crypto_utils.py        # Encryption
│   └── verification_utils.py  # Signatures
├── blockchain_module/         # Blockchain
│   ├── transaction.py
│   └── block.py
└── examples/                  # Example scripts
```

## 🔍 Understanding Output

The simulation shows three phases:

1. **SENDER SIDE** (L7→L1)
   - Data encapsulation
   - Headers/trailers added
   - Encryption/signing applied

2. **TRANSMISSION MEDIUM**
   - Simulated network transfer

3. **RECEIVER SIDE** (L1→L7)
   - Data decapsulation
   - Headers/trailers removed
   - Decryption/verification performed

## 📖 Documentation

- **README.md** - Full documentation
- **DEPLOYMENT_GUIDE.md** - Deployment instructions
- **IMPLEMENTATION_COMPLETE.md** - Implementation summary
- **osi_model.md** - OSI theory
- **osi_flow_sim.md** - Design documentation

## 🐛 Troubleshooting

### Import Errors
```bash
# Make sure you're in the right directory
cd osi_blockchain_simulation
python main_simulation.py
```

### Permission Errors
```bash
chmod +x main_simulation.py
chmod +x examples/*.py
```

## 🎓 What You'll Learn

- ✅ OSI 7-layer model
- ✅ Data encapsulation/decapsulation
- ✅ Network protocols (IP, MAC, ports)
- ✅ Encryption concepts
- ✅ Digital signatures
- ✅ Checksums for data integrity
- ✅ Blockchain basics

## 📦 Alternative Installation (Patch File)

```bash
git clone https://github.com/GizzZmo/8.git
cd 8
git apply osi-simulation.patch
```

## 🤝 Support

For issues or questions:
1. Check the README.md
2. Review example scripts
3. Open an issue on GitHub

## ✨ Example Output

```
----------------------------------------
[L7 - Application] Original Data: 'Secret'
[L6 - Presentation] Encrypted Payload: 'yOIXO^'
[L5 - Session] Adding Session Header: {'session_id': 12345}
[L4 - Transport] Segmenting Data...
[L3 - Network] Adding IP Header...
[L2 - Data Link] Adding Ethernet Header/Trailer...
[L1 - Physical] Transmitting bits...
----------------------------------------
SIMULATING TRANSMISSION MEDIUM...
----------------------------------------
RECEIVER SIDE:
[L1 - Physical] Received bits...
[L2 - Data Link] MAC address matches. FCS check OK...
...
[L6 - Presentation] Decrypting data...
[L7 - Application] Final Data Received: 'Secret'
----------------------------------------
SIMULATION COMPLETE.
```

---

**Ready to explore the OSI model?** Start with `python main_simulation.py --help` 🚀
