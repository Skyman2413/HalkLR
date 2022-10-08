class Tensor:

    def __init__(self, data):
        self.__A = [list(map(int, data[0].split())) for i in range(3)]
        print(self.__A)
        self.__b = [list(map(int, data[1].split())) for i in range(3)]
        self.__B = [list(map(int, data[2].split())) for i in range(3)]
        self.__T = [list(map(int, data[3].split())) for i in range(3)]
        self.__Q = [list(map(int, data[4].split())) for i in range(3)]
        self.__W = [list(map(int, data[5].split())) for i in range(3)]
        self.__Kr = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]]

    def first(self) -> [] or str:
        res = []
        lineres = []
        if None in (self.__A, self.__b):
            return "Не введен A или b"
        for row in self.__A:
            i = 0
            for item in row:
                lineres.append(float(item) * float(self.__b[0][i]))
                i += 1
                if i == 3:
                    i = 0
            res.append(lineres)
            lineres = []
        return res

    def second(self) -> [] or str:
        res = []
        lineres = []
        for i in range(3):
            for j in range(9):
                lineres.append(float(self.__A[i][j]) + float(self.__B[i][j]))
            res.append(lineres)
            lineres = []
        return res

    def third(self) -> [] or str:
        return [[self.__T[0][0] + self.__T[1][3] + self.__T[2][6]],
                [self.__T[0][1] + self.__T[1][4] + self.__T[2][7]],
                [self.__T[0][2] + self.__T[1][5] + self.__T[2][8]]]

    def forth(self) -> [] or str:
        A = []
        for i in range(0, 9, 3):
            sum = 0
            for j in range(3):
                sum += self.__T[j][j + i]
            A.append(sum)

        B = []
        for i in range(0, 9, 3):
            sum = 0
            for j in range(3):
                sum += self.__Q[j][j + i] * self.__W[j][j]
            B.append(sum)

        res = []
        for i in range(len(A)):
            res.append([A[i] + B[i]])
        return res


if __name__=="__main__":
    with open("input.txt", "r") as f:
        raw_data = f.readlines()
    data = []
    j = 0
    line = ""
    for i in range(len(raw_data)):
        raw_data[i] = str(raw_data[i]).strip("\n")
        line += raw_data[i]
        j += 1
        if j == 3:
            j = 0
            data.append(line)
            line = ""
        else:
            line += " "
    tens = Tensor(data)
    print("Ab")
    for row in tens.first():
        print(row)
    print()
    print("AB")
    for row in tens.second():
        print(row)
    print()
    print("T")
    for row in tens.third():
        print(row)
    print()
    print("Tkr + QW")
    for row in tens.forth():
        print(row)
