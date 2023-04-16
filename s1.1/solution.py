
def statistics(text):
    # this func can be used to count the number of each letter
    arr = [0 for i in range(26)]
    for i in text:
        index = ord(i) - ord('A')
        # print(i,index)
        arr[index] = arr[index] + 1
    return arr

def coincidence_index(text):
    n = len(text)
    if n == 0:
        return 0
    if n == 1:
        return 0
    N = statistics(text)
    return sum(Ni*(Ni-1) for Ni in N)/(n*(n-1))

def key_length(text):
    min_diff = float("inf")
    best_length = None
    arr = None
    for length in range(1, len(text)):
        # [start_index :: step]
        groups = [text[i::length] for i in range(length)]
        # print(groups)
        ci_list = [coincidence_index(g) for g in groups]
        fluctuations = [(abs(ci - 0.065))**2 for ci in ci_list]
        avg_fluctuation = sum(fluctuations) / length

        avg_ci = sum(ci_list) / length
        # print(length, ci_list)
        # print(avg_fluctuation)
        diff = avg_fluctuation
        if diff < min_diff:
            min_diff = diff
            best_length = length
            arr = ci_list
    return best_length,arr


# i = 'b'
# print(ord(i) - ord('a'))
# 1.21 (c)仿射密码密文
text = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZOEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEOPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDEKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"
ciphertext = "KCCPKBGUEDPHOTYAVINRRTMVGRKDNBVEDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCOKYVXCHKETPONCOORHJVAJUWETMCMSPKODYHJVDAHCTRLSVSKCGCZOODZXGSERLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZONRWXCVYCGAONWDDKACKAWBBIKETIOVKCGGHJVLNHIFFSOESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFOIYCWHJVLNHI0IBIKHJVNPIST"
t = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBJJCHRTKDNVRZCHRCLQOHPWOAIIWXNRMGWOIIFKEE"
# print(coincidence_index(text))


txt = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"


length, arr = key_length(text)

print(length)

code = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
print(len(code))

