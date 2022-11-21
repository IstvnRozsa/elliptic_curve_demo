from curve import Curve

class Account:
    def __init__(self, name:str, secret_key:int, ecurve:Curve):
        self.name = name
        self.secret_key = secret_key
        self.public_key = ecurve.double_and_add(self.secret_key, ecurve.generator)

    def __str__(self) -> str:
        return "Name: " + self.name + ", Secret key: " + str(self.secret_key) + " Public key: " + str(self.public_key)