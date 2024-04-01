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
    array3 = [0] *len(data)
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

key = fromhex("a0-d3-57-17-e2-17-98-82-ae-42-0b-df-2a-80-ec-d0-1b-f2-2e-62-67-96-f3-ba")
b = b''

for i in key:
    b += bytes.fromhex(i)

print("".join([chr(int(i, 16)) for i in encode(b, "c-sharp".encode())]))