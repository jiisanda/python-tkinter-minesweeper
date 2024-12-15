from msgspec import Struct


class RegisteredPlayer(Struct):
    token: str = None
    field : str = None
    is_registered: bool = False
