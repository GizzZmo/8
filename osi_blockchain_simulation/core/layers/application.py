from core.pdu import PDU

class ApplicationLayer:
    def encapsulate(self, data):
        print(f"[L7 - Application] Encapsulating: {data!r}")
        return PDU(payload=data, header={"type": "application"})

    def decapsulate(self, pdu):
        print(f"[L7 - Application] Final Data Received: {pdu.payload!r}")
        return pdu.payload
