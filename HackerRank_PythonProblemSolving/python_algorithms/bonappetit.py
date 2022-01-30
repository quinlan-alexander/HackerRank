def bonappetit(ar, k, b):
    annaCharge = int((sum(ar) - ar[k])/2)
    if b == annaCharge:
        return "Bon Appetit"
    else:
        return b - annaCharge


if __name__ == '__main__':
    firstLine = input().split()
    ar = list(range(int(firstLine[0])))
    k = int(firstLine[1])

    secondLine = input().split()
    ar = list(map(int, secondLine))

    thirdLine = input()
    b = int(thirdLine)

    print(bonappetit(ar, k, b))