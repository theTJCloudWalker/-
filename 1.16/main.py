import math

def is_prime4(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    code = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
    list = [19, 6, 4, 4, 12, 13, 4, 11, 13, 13, 19, 3, 17, 14, 4, 14, 0, 0, 7, 3, 14, 4, 19, 2, 18, 7, 0, 4, 8, 17, 11, 12]
    # for i in code:
    #     list.append(ord(i)-ord('A'))
    for i in range(2,10):
        arr = []
        for j in range(0, len(code),i):
            arr.append(code[j:j+i])
            #                   print(code[j:j+i])

        print(arr)
