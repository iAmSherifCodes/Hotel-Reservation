class EmailErrorException(Exception):

    def __repr__(self):
        return "Invalid Email"

