class PDU:
    def __init__(self, payload, header=None, trailer=None):
        self.header = header or {}
        self.payload = payload
        self.trailer = trailer or {}

    def __repr__(self):
        return f"PDU(header={self.header!r}, payload={self.payload!r}, trailer={self.trailer!r})"
