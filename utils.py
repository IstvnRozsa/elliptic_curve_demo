def _mod(n,m):
    return ((n%m) + m) % m

def _mul_inverse(num, order):
    for i in range(1, order):
        if _mod((num * i), order) == 1:
            return i
    return None

def _decimal2binary(number):
    return bin(number).replace("0b", "")


# y kiszamitasahoz
def _sqrt(num, order):
    for i in range(0, order):
        if (i**2) % order == num:
            return i

if __name__=="__main__":
    print(_mod(100, 3))
    print(100%3)
    print(((100%3)+ 3) % 3)