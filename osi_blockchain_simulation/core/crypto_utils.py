def simple_xor_encrypt(data, key=42):
    """
    WARNING: This function implements a simple XOR-based encryption for educational purposes only.
    It is NOT cryptographically secure and MUST NOT be used for real encryption needs.
    """
    return ''.join(chr(ord(c) ^ key) for c in data)

def simple_xor_decrypt(data, key=42):
    return ''.join(chr(ord(c) ^ key) for c in data)
