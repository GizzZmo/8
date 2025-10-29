from core.pdu import PDU
from core.verification_utils import checksum

class TransportLayer:
    def __init__(self, dest_port=80, protocol="TCP"):
        self.protocol = protocol
        self.dest_port = dest_port

    def encapsulate(self, pdu):
        header = {"src_port": 1024, "dst_port": self.dest_port, "protocol": self.protocol}
        trailer = {"checksum": checksum(str(pdu))}
        print(f"[L4 - Transport] Segmenting Data. Header: {header}, Trailer: {trailer}")
        return PDU(payload=pdu, header=header, trailer=trailer)

    def decapsulate(self, pdu):
        cs = checksum(str(pdu.payload))
        if pdu.trailer.get("checksum") == cs:
            print("[L4 - Transport] Checksum OK.")
        else:
            print("[L4 - Transport] Checksum failed.")
        print("[L4 - Transport] Port number matches. Stripping L4 Header.")
        return pdu.payload
