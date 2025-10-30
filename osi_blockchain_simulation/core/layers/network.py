from core.pdu import PDU

class NetworkLayer:
    def __init__(self, dest_ip):
        self.dest_ip = dest_ip

    def encapsulate(self, pdu):
        header = {"src_ip": "192.168.0.1", "dst_ip": self.dest_ip, "protocol": 6}
        print(f"[L3 - Network] Adding IP Header: {header}")
        return PDU(payload=pdu, header=header)

    def decapsulate(self, pdu):
        print("[L3 - Network] IP address matches. Stripping L3 Header.")
        return pdu.payload
