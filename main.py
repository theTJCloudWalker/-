# 密文
ciphertext = "QWERTYUIOPASDFGHJKLZXCVBNM"
# 字母频率表
freq_table = {"A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127,
              "F": 0.022, "G": 0.020, "H": 0.061, "I": 0.070, "J": 0.002,
              "K": 0.008, "L": 0.040, "M": 0.024, "N": 0.067, "O": 0.075,
              "P": 0.019, "Q": 0.001, "R": 0.060, "S": 0.063, "T": 0.091,
              "U": 0.028,"V" : 0.010,"W" : 0.023,"X" : 0.001,"Y" : .020,"Z" : .001}

# 计算重合指数
def coincidence_index(text):
    n = len(text)
    if n==0:
        return 0
    if n==1:
        return 0
    count = {}
    for c in text:
        count[c] = count.get(c ,1) +1
    total = sum([v * (v -1) for v in count.values()])
    return total / (n * (n -1))

# 计算拟重合指数
def expected_coincidence_index(text ,shift):
    n = len(text)
    total = sum([freq_table[c] * freq_table[text[(i + shift) % n]] for i ,c in enumerate(text)])
    return total

# 确定密钥长度
def find_key_length(ciphertext):
    min_diff = float("inf")
    best_length = None
    for length in range(1 ,len(ciphertext)):
        groups = [ciphertext[i::length] for i in range(length)]
        ci_list = [coincidence_index(g) for g in groups]
        avg_ci = sum(ci_list) / length
        diff = abs(avg_ci - .065)
        if diff < min_diff:
            min_diff = diff
            best_length = length
    return best_length

# 确定位移量
def find_shifts(ciphertext ,key_length):
    shifts = []
    for i in range(key_length):
        group = ciphertext[i::key_length]
        max_eci= float("-inf")
        best_shift= None
        for shift in range(26):
            eci= expected_coincidence_index(group ,shift)
            if eci > max_eci:
                max_eci= eci
                best_shift= shift
        shifts.append(best_shift)
    return shifts

# 解密明文
def decrypt(ciphertext ,shifts):
    plaintext= ""
    key_length= len(shifts)
    for i ,c in enumerate(ciphertext):
        shift= shifts[i % key_length]
        p= chr((ord(c) - ord("A") - shift) %26 + ord("A"))
        plaintext += p
    return plaintext

# 测试

key_length = find_key_length(ciphertext)
print("Key length:", key_length)
shifts = find_shifts(ciphertext,key_length)
print("Shifts:", shifts)
plaintext = decrypt(ciphertext,shifts)
print("Plaintext:", plaintext)