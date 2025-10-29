from core.pdu import PDU

class SessionLayer:
    def encapsulate(self, pdu):
        header = {"session_id": 12345}
        print(f"[L5 - Session] Adding Session Header: {header}")
        return PDU(payload=pdu, header=header)

    def decapsulate(self, pdu):
        print(f"[L5 - Session] Session validated. Stripping L5 Header.")
        return pdu.payload
