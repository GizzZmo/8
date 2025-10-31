from core.pdu import PDU
import pickle

class PhysicalLayer:
    def encapsulate(self, pdu):
        # Serialize the PDU object to bytes, then to bits
        serialized = pickle.dumps(pdu)
        # Convert bytes to binary string
        bits = ''.join(format(byte, '08b') for byte in serialized)
        print(f"[L1 - Physical] Transmitting bits: {bits[:40]}... (truncated)")
        return bits

    def decapsulate(self, bits):
        # Convert bits back to bytes
        n = 8
        byte_array = bytes(int(bits[i:i + n], 2) for i in range(0, len(bits), n))
        
        print(f"[L1 - Physical] Received bits: {bits[:40]}... (truncated)")
        # Deserialize bytes back to PDU object
        pdu = pickle.loads(byte_array)
        return pdu
