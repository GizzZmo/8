from core.pdu import PDU
import pickle
import base64

class PhysicalLayer:
    def encapsulate(self, pdu):
        # Serialize the PDU object to bytes, then to base64, then to bits
        serialized = pickle.dumps(pdu)
        # Convert bytes to binary string
        bits = ''.join(format(byte, '08b') for byte in serialized)
        print(f"[L1 - Physical] Transmitting bits: {bits[:40]}... (truncated)")
        return bits

    def decapsulate(self, bits):
        # Convert bits back to bytes
        n = 8
        byte_array = bytearray()
        for i in range(0, len(bits), n):
            byte_array.append(int(bits[i:i + n], 2))
        
        print(f"[L1 - Physical] Received bits: {bits[:40]}... (truncated)")
        # Deserialize bytes back to PDU object
        pdu = pickle.loads(bytes(byte_array))
        return pdu
