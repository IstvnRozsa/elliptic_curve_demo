from curve import Curve
from account import Account
from utils import _mod, _mul_inverse
import hashlib

ec = Curve(-2, 15, 23, 4)
print('0. Generator point: ', ec.generator)

Alice = Account(name = "Alice", secret_key = 3, ecurve = ec)
print("1. Account: ", Alice)

'''Message'''
message = "Hello"
z = 2
my_hash = int.from_bytes(hashlib.sha256(message.encode('utf-8')).digest(), 'big')
#my_hash = int(hashlib.sha256(message.encode('utf-8')).hexdigest())
print("2. My hashed messsage: ", my_hash)


'''Sign'''
k = ec.rand_k() # user pre message secret number
R = ec.double_and_add(k, ec.generator)
r = R.x # r = (g**k mod p) mod p

k_mul_inverse = _mul_inverse(k, ec.order)
s = _mod(k_mul_inverse * (my_hash + Alice.secret_key * r), ec.order) # s = [k**-1(H(M) +xr)] mod q
print("3. Signature:", r, s)




'''Verify'''
w = _mul_inverse(s, ec.order) # w=(s**-1)**-1 mod q
u1 = _mod(w * my_hash, ec.order) # u1=[H(M)w] mod q
u2 = _mod(w * r, ec.order) # u2 = w*r mod q
print("4. Help: ", w, u1, u2)

temp1 = ec.double_and_add(u1, ec.generator)
temp2 = ec.double_and_add(u2, Alice.public_key)
print("5. Temps: ", temp1, temp2)


P = ec.add(temp1, temp2)
print("6. Signature is valid: ", P.x == _mod(r, ec.order))


