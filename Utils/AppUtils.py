import uuid
from uuid import UUID


class AppUtils:

    def __init__(self):
        pass

    @staticmethod
    def generate_id() -> str:
        # generate_uuid =
        return str(uuid.uuid4())


# print(type(AppUtils.generate_id()))
