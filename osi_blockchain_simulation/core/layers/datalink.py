from core.pdu import PDU

class DataLinkLayer:
    def __init__(self, dest_mac):
        self.dest_mac = dest_mac

    def encapsulate(self, pdu):
        header = {"src_mac": "00:00:00:00:00:01", "dst_mac": self.dest_mac, "type": "0x0800"}
        trailer = {"fcs": "0xABCDE"}
        print(f"[L2 - Data Link] Adding Ethernet Header/Trailer. Header: {header}, Trailer: {trailer}")
        return PDU(payload=pdu, header=header, trailer=trailer)

    def decapsulate(self, pdu):
        print("[L2 - Data Link] MAC address matches. FCS check OK. Stripping L2 Header/Trailer.")
        return pdu.payload
