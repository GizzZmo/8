import hashlib

def checksum(data):
    if isinstance(data, dict):
        data = str(data)
    return hashlib.sha256(data.encode()).hexdigest()[:8]

def sign(data, secret):
    if isinstance(data, dict):
        data = str(data)
    return hashlib.sha256((data + secret).encode()).hexdigest()[:12]

def verify(data, signature, secret):
    expected = sign(data, secret)
    return expected == signature
