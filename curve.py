import math
import random
from utils import _mod, _mul_inverse, _sqrt, _decimal2binary
from coord import Coord


class Curve:
    def __init__(self, a, b, order, generator_x):
        self.a = a
        self.b = b
        self.order = order
        self.generator = Coord(generator_x, self.get_y(generator_x))

    def get_y(self, x):
        return _sqrt((x**3 + self.a*x + self.b) % self.order, self.order)

    def is_on_curve(self, P:Coord):
        left_side = (P.y ** 2) % self.order
        right_side = (P.x ** 3 + self.a * P.x + self.b) % self.order
        return left_side == right_side

    def rand_k(self):
        return math.ceil(random.random() * (self.order -1))

    def _double(self, P):
        R = Coord();
        s = _mod((3 * (P.x ** 2) + self.a) * (_mul_inverse(2 * P.y, self.order)), self.order)
        R.x = _mod(s ** 2 - 2 * P.x, self.order)
        R.y = _mod(s * (P.x - R.x) - P.y, self.order)
        return R

    def _add(self, P, Q):
        R = Coord()
        s = _mod((Q.y - P.y) * (_mul_inverse(Q.x - P.x, self.order)), self.order)
        R.x = _mod(s ** 2 - P.x - Q.x, self.order)
        R.y = _mod(s * (P.x - R.x) - P.y, self.order)

        return R

    def add(self, P, Q = None):
        if P == None:
            return Q
        if Q == None or (P.x == Q.x and P.y == Q.y):
            return self._double(P)
        else:
            return self._add(P, Q)

    
    def multiply(self, k, P):
        result = None
        for i in range(0, k):
            result = self.add(result, P)
            print('Res: ', result)

        return result

    def double_and_add(self, k, P):
        bin = _decimal2binary(k)[::-1]
        #print(bin)
        result = None
        Q = P
        for i in range(0, len(bin)):
            if bin[i] == "1":
                result = self.add(result, Q)
            #print("R: ", result)
            Q = self.add(Q)
            #print("Q: ", Q, self.is_on_curve(Q))
        
        return result


    