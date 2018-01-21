import numpy as np

T = 'T'
M = 'M'
TAKEN = 'X'
MAX_R = 5
MAX_C = 5

class Slice:

    def __init__(self, r, c, h, w):
        self.r1 = r
        self.c1 = c
        self.r2 = r + w
        self.c2 = c + h

    def __len__(self):
        return (self.r2 - self.r1 + 1) * (self.c2 - self.c1 + 1)

    def __str__(self):
        return str(self.r1) + " " + str(self.c1) + " " + str(self.r2) + " " + str(self.c2)


def parse(input):
    return [line.rstrip('\n') for line in open(input)]


def is_legal(arr, L, H):
    if TAKEN in arr:
        return False
    T_counter = len(np.where(arr == T)[0])
    M_counter = len(np.where(arr == M)[0])
    return T_counter <= H and T_counter >= L and M_counter <= H and M_counter >= L


if __name__ == "__main__":
    arr = parse("small.in")
    numbers = arr[0].split(' ')
    arr = arr[1:]
    pizza = []
    for e in arr:
        pizza.append(list(e))
    R = int(numbers[0])
    C = int(numbers[1])
    L = int(numbers[2])
    H = int(numbers[3])
    pizza = np.array(pizza)

    slices = []
    indexes = np.zeros((R, C), dtype=np.bool)
    r, c = 0, 0
    indexes[0][0] = True
    while True:
        helper = np.zeros((MAX_R, MAX_C))
        for i in range(R):
            for j in range(C):
                if r + i < R and c + j < C and is_legal(pizza[r + i:c + j], L, H):
                    helper[i][j] = (i + 1) * (j + 1)
        if not np.all(helper == 0):
            maxi = 0, 0
            maxe = 0
            for i in range(MAX_R):
                for j in range(MAX_C):
                    if helper[i][j] > maxe:
                        maxi = i, j
                        maxe = helper[i][j]
            slices.append(Slice(r, c, maxi[0], maxi[1]))
            indexes[r + maxi[0]:c + maxi[1]] = True
            pizza[r + maxi[0]:c + maxi[1]] = TAKEN


        indexes[r][c] = True
        if False not in indexes:
            break
        # next r and c:
        left = np.where(indexes == False)
        rand = np.random.choice(len(left[0]), 1)[0]
        r = left[0][rand]
        c = left[1][rand]

    summation = 0
    for slice in slices:
        summation += len(slice)
        print(slice)
    print(summation)