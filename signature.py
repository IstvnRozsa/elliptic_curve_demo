from utils import _mod, _mul_inverse


class Signature:
    def __init__(self, hash, account, ec):
        k = ec.rand_k() # user pre message secret number
        R = ec.double_and_add(k, ec.generator)
        self.r = R.x # r = (g**k mod p) mod p

        k_mul_inverse = _mul_inverse(k, ec.order)
        self.s = _mod(k_mul_inverse * (hash + account.secret_key * self.r), ec.order) # s = [k**-1(H(M) +xr)] mod q

    def __str__(self):
        return "3. Signature: r:" + str(self.r) +" s: "+ str(self.s) 