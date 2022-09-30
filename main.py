import copy

class Tensor:

    def __init__(self, A: [], b: [], B: [], T: [], Q: [], W: []):
        if A: self.__A = copy.deepcopy(A)
        if b: self.__b = copy.deepcopy(b)
        if B: self.__B = copy.deepcopy(B)
        if T: self.__T = copy.deepcopy(T)
        if Q: self.__Q = copy.deepcopy(Q)
        if W: self.__W = copy.deepcopy(W)



    def first(self) -> [] or str:
        res = []
        lineres = []
        if None in (self.__A, self.__b):
            return "Не введен A или b"
        for row in self.__A:
            i = 0
            for item in row:
                lineres.append(float(item) * float(self.__b[i]))
                i += 1
                if i == 3:
                    i = 0
            res.append(lineres)
            lineres = []
        return lineres

    def second(self) -> [] or str:
        res = []
        lineres = []
        for i in range(self.__A):
            for j in range(self.__B):
                lineres.append(float(self.__A[i][j]) + float(self.__B[i][j]))
            res.append(lineres)
            lineres = []

    def third(self) -> [] or str:
        res = []
        lineres = []
        for i in range

    def forth(self) -> [] or str:
        pass