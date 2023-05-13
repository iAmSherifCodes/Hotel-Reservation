class AppUtils:

    def __init__(self):
        pass
        
    @staticmethod
    def generate_id() -> int:
        last_generated_id = 1
        return last_generated_id + 1
