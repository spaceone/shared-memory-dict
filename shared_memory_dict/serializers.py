import json
import pickle
from typing import Final, Protocol

NULL_BYTE: Final = b"\x00"


class SharedMemoryDictSerializer(Protocol):
    def dumps(self, obj: dict) -> bytes:
        ...

    def loads(self, data: bytes) -> dict:
        ...


class JSONSerializer:

    __slots__ = ()

    encoder = json.JSONEncoder
    decoder = json.JSONDecoder

    def dumps(self, obj: dict) -> bytes:
        return json.dumps(obj, cls=self.encoder).encode() + NULL_BYTE

    def loads(self, data: bytes) -> dict:
        data = data.split(NULL_BYTE, 1)[0]
        return json.loads(data, cls=self.decoder)


class PickleSerializer:

    __slots__ = ()

    def dumps(self, obj: dict) -> bytes:
        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)

    def loads(self, data: bytes) -> dict:
        return pickle.loads(data)
