class NoCustomerFound(Exception):
    def __repr__(self):
        return f"No Customer Found"
