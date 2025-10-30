# Local Deployment Guide for OSI Blockchain Simulation

This guide explains how to deploy the OSI blockchain simulation locally using the provided patch file.

## Prerequisites

- Git installed on your system
- Python 3.8 or higher

## Deployment Methods

### Method 1: Using the Patch File

If you have the `osi-simulation.patch` file, follow these steps:

1. **Clone the repository** (if not already cloned):
   ```bash
   git clone https://github.com/GizzZmo/8.git
   cd 8
   ```

2. **Apply the patch**:
   ```bash
   git apply osi-simulation.patch
   ```

   Or if you want to apply it as a commit:
   ```bash
   git am osi-simulation.patch
   ```

3. **Verify the installation**:
   ```bash
   ls -la osi_blockchain_simulation/
   ```

   You should see the complete directory structure.

### Method 2: Direct Clone from Branch

Alternatively, you can clone the specific branch:

```bash
git clone -b copilot/create-iso-simulation-patch https://github.com/GizzZmo/8.git
cd 8
```

## Running the Simulation

Once deployed, navigate to the simulation directory:

```bash
cd osi_blockchain_simulation
```

### Basic Usage

1. **Simple text transmission**:
   ```bash
   python main_simulation.py --data "Hello World"
   ```

2. **Encrypted transmission**:
   ```bash
   python main_simulation.py --data "Secret Message" --encrypt
   ```

3. **Signed transmission**:
   ```bash
   python main_simulation.py --data "Important Data" --sign
   ```

4. **Blockchain transaction**:
   ```bash
   python main_simulation.py --blockchain
   ```

5. **Combined encryption and signing**:
   ```bash
   python main_simulation.py --data "Secure Data" --encrypt --sign
   ```

### Running Example Scenarios

The `examples/` directory contains pre-configured scenarios:

```bash
python examples/simple_text_flow.py
python examples/encrypted_data_flow.py
python examples/signed_data_flow.py
python examples/blockchain_flow.py
```

## Command-Line Options

- `--data <string>`: Application data to send (default: "Hello OSI World")
- `--dest_ip <ip>`: Destination IP address (default: "192.168.1.100")
- `--dest_mac <mac>`: Destination MAC address (default: "00:1A:2B:3C:4D:5E")
- `--port <number>`: Destination port (default: 80)
- `--encrypt`: Enable Presentation Layer encryption
- `--sign`: Enable digital signing
- `--blockchain`: Simulate blockchain transaction as data

## Understanding the Output

The simulation shows:

1. **Sender Side**: Data flows through layers L7 → L1
   - Each layer adds headers/trailers
   - Shows data transformation (encryption, etc.)

2. **Transmission Medium**: Simulated network transfer

3. **Receiver Side**: Data flows through layers L1 → L7
   - Each layer removes headers/trailers
   - Shows data restoration (decryption, etc.)

## Troubleshooting

### Patch Application Fails

If `git apply` fails:

1. Check if you're in the correct directory (repository root)
2. Ensure your working directory is clean: `git status`
3. Try using `git am` instead of `git apply`

### Import Errors

If you get Python import errors:

1. Make sure you're running from the `osi_blockchain_simulation` directory
2. Or use: `python -m osi_blockchain_simulation.main_simulation` from the repository root

### Permission Errors

If scripts are not executable:

```bash
chmod +x osi_blockchain_simulation/main_simulation.py
chmod +x osi_blockchain_simulation/examples/*.py
```

## Uninstalling

To remove the simulation:

```bash
# From repository root
rm -rf osi_blockchain_simulation/
rm osi-simulation.patch
```

If applied as a commit, you can also:
```bash
git revert HEAD  # if it was the last commit
```

## Additional Information

For more details, see:
- `osi_blockchain_simulation/README.md` - Complete simulation documentation
- `osi_model.md` - OSI model theory
- `osi_flow_sim.md` - Simulation design documentation

## Support

For issues or questions:
1. Check the README.md in the simulation directory
2. Review the example scripts
3. Open an issue on the GitHub repository
