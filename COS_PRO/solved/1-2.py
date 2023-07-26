def func_a(bstr, bstr_len):
    padZero = ""
    padSize = bstr_len - len(bstr)
    for i in range(padSize):
        padZero += "0"
    return padZero + bstr

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    if max_length > len(binaryA):
        binaryA = func_a(binaryA, max_length)
    if max_length > len(binaryB):
        binaryB = fucn_a(binaryB, max_length)
    
    hamming_distance = 0
    for i in range(max_length):
        if binaryA[i] != binaryB[i]:
            hamming_distance += 1
    return hamming_distance