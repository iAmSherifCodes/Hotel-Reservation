import uuid
from uuid import UUID


class AppUtils:

    def __init__(self):
        pass

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())

