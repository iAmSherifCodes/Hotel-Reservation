import uuid
from uuid import UUID


class AppUtils:

    def __init__(self):
        pass

    @staticmethod
    def generate_id() -> UUID:
        # generate_uuid =
        return uuid.uuid4()


# print(type(AppUtils.generate_id()))
