class AppUtils:

    def __init__(self):
        self._last_generated_id = 0
        
    @staticmethod
    def generate_id(self) -> int:
        self._last_generated_id += 1
        return self._last_generated_id
