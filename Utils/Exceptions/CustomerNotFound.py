class CustomerNotFound(Exception):
    def __repr__(self):
        return "Customer Not Found"
