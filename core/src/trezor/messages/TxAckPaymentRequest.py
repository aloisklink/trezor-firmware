# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .PaymentRequestMemo import PaymentRequestMemo

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckPaymentRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 37

    def __init__(
        self,
        *,
        recipient_name: str,
        signature: bytes,
        memos: List[PaymentRequestMemo] = None,
        nonce: bytes = None,
    ) -> None:
        self.memos = memos if memos is not None else []
        self.recipient_name = recipient_name
        self.signature = signature
        self.nonce = nonce

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_name', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('memos', PaymentRequestMemo, p.FLAG_REPEATED),
            3: ('nonce', p.BytesType, None),
            4: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
