from curve import Curve
from account import Account
from utils import _mod, _mul_inverse
import hashlib

ec = Curve(-2, 15, 23, 4)
print(ec.generator)

Alice = Account("Alice", 3, ec)
print("1. Account: ", Alice)

'''Message'''
message = "Hello"
#z = 2 # modositani kell
my_hash = int.from_bytes(hashlib.sha256(message.encode('utf-8')).digest(), 'big')
print("2. My hashed messsage: ", my_hash)


'''Sign'''
k = ec.rand_k()
# k = 8 #modositasra szorul
R = ec.double_and_add(k, ec.generator)
r = R.x

k_mul_inverse = _mul_inverse(k, ec.order)
s = _mod(k_mul_inverse * (my_hash + Alice.secret_key * r), ec.order)
print("3. Signature:", r, s)




'''Verify'''
w = _mul_inverse(s, ec.order)
u1 = _mod(w * my_hash, ec.order)
u2 = _mod(w * r, ec.order)
print("4. Helpers: ", w, u1, u2)

temp1 = ec.double_and_add(u1, ec.generator)
temp2 = ec.double_and_add(u2, Alice.public_key)
print("5. Temps: ", temp1, temp2)


P = ec.add(temp1, temp2)
print("6. Signature is valid: ", P.x == _mod(r, ec.order))


