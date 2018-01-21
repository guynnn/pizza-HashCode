import numpy as np

T = 'T'
M = 'M'
TAKEN = 'X'


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


def is_enough(arr, L):
    T_counter = 0
    M_counter = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == T:
                T_counter += 1
            elif arr[i][j] == M:
                M_counter += 1
            else:
                return True
    return T_counter >= L and M_counter >= L


if __name__ == "__main__":
    arr = parse("example.in")
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
    current = Slice(0, 0, pizza)
    print("cur", current)
    slices = [current]
    loops = 0
    while loops < 100:
        loops += 1
        current = Slice(current.next()[0], current.next()[1], pizza)
        while current.r1 == -1:
            if loops > 100:
                break
            loops += 1
            guess1 = int(np.random.uniform(0, Slice.R + 1))
            guess2 = int(np.random.uniform(0, Slice.C + 1))
            current = Slice(guess1, guess2, pizza)
        slices.append(current)
    summation = 0
    for slice in slices:
        if slice.r1 != -1:
            summation += len(slice)
    print('L:', Slice.L, '\nH:', Slice.H)
    print(summation)
    for e in slices:
        print(e)
    print(pizza)
