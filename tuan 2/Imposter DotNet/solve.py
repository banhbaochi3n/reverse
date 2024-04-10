import string
import itertools
import hashlib

def gen_hash(A_0):
    md5 = hashlib.md5()
    md5.update(A_0.encode('ascii'))
    result = md5.hexdigest()
    return result

def encode(data, key):
    array = [i for i in range(256)]
    array2 = [0] * 256

    if len(key) == 256:
        array2 = key[:]
    else:
        for j in range(256):
            array2[j] = key[j % len(key)]

    num = 0
    k = 0
    for k in range(256):
        num = (num + array[k] + array2[k]) % 256
        array[k], array[num] = array[num], array[k]

    num = k = 0
    array3 = [0] * len(data)
    for l in range(len(data)):
        k = (k + 1) % 256
        num = (num + array[k]) % 256
        array[k], array[num] = array[num], array[k]
        num4 = array[(array[k] + array[num]) % 256]
        array3[l] = bytes([data[l] ^ num4]).hex()

    return array3

def fromhex(A_0):
    A_0 = A_0.replace("-", "")
    array = [0] * (len(A_0)//2)
    for i in range(len(array)):
        array[i] = bytes([int(A_0[i * 2:i * 2 + 2], 16)]).hex()
    return array

possible_char = string.ascii_letters + string.digits 
password_length = 2
all = []    # Array of results

# Brute force lmao :P
for combination in itertools.product(possible_char, repeat=password_length):
    attempt = ''.join(combination)
    a = gen_hash(attempt)
    b = a.encode('utf-8')
    c = "among-us".encode('utf-8')
    check = "".join(encode(b, c))[:2]
    # Check ìf first byte is 40, cuz hex string's first byte is 40
    if check == "40":
        all.append(attempt)
        # print(attempt)
        # break        

print(all)