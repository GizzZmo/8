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
        
        # Verify signature BEFORE decryption (signature was computed on encrypted data)
        if header.get("signature"):
            if verify(str(payload), header["signature"], self.secret):
                print(f"[L6 - Presentation] Signature verified.")
            else:
                print(f"[L6 - Presentation] Signature verification failed.")
        
        # Then decrypt if needed
        if header.get("encryption"):
            print(f"[L6 - Presentation] Decrypting data.")
            payload = simple_xor_decrypt(payload, self.key)
            print(f"[L6 - Presentation] Original Data: {payload!r}")
        
        return PDU(payload=payload)
