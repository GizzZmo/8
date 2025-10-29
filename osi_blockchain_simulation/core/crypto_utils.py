def simple_xor_encrypt(data, key=42):
    return ''.join(chr(ord(c) ^ key) for c in data)

def simple_xor_decrypt(data, key=42):
    return ''.join(chr(ord(c) ^ key) for c in data)
