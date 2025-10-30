class PhysicalLayer:
    def encapsulate(self, pdu):
        bits = ''.join(format(ord(c), '08b') for c in str(pdu))
        print(f"[L1 - Physical] Transmitting bits: {bits[:40]}... (truncated)")
        return bits

    def decapsulate(self, bits):
        n = 8
        chars = [chr(int(bits[i:i + n], 2)) for i in range(0, len(bits), n)]
        data = ''.join(chars)
        print(f"[L1 - Physical] Received bits: {bits[:40]}... (truncated)")
        # Return the reconstructed data/PDU structure
        # In a real implementation, this would deserialize back to PDU
        # For simplicity, we'll reconstruct by parsing the string representation
        return eval(data)
