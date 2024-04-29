import string

char_list = string.ascii_lowercase + "{}"
flag = []

for dl in char_list:
    buffer = dl
    dl = ord(dl)
    cl = dl
    dl = dl >> 1
    al = dl
    cl = cl & 0x01
    al = al & 0x01
    buffer += "0" + str(cl)
    buffer += "0" + str(al)
    dl = dl >> 1
    al = dl
    dl = dl >> 1
    al = al & 0x01
    buffer += "0" + str(al)
    al = dl
    al = al & 0x01
    dl = dl >> 1
    buffer += "0" + str(al)
    al = dl
    al = al & 0x01
    dl = dl >> 1
    buffer += "0" + str(al)
    al = dl
    al = al & 0x01
    dl = dl >> 1
    buffer += "0" + str(al)
    al = dl
    al = al & 0x01
    dl = dl >> 1
    buffer += "0" + str(al)
    dl = dl & 0x01
    buffer += "0" + str(dl)
    flag.append(buffer)

print(flag)
