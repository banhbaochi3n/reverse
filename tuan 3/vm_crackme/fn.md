```
1. fn_22
esi + 4 = esi
Gán eax = 1.
2. fn_23
esi + 8 = esi
Gán eax = 1.
3. fn_24
esi + 0xC = esi
Gán eax = 1.
4. fn_18
Gán eax = esi + 24 = 3
Gán esi2 = esi + 136 = địa chỉ vùng nhớ 2 ecx
Gán ecx = eax + 5 = 8
Gán edx = eax + esi2 + 1 = 0xC
esi + 20 (0x3FC) += 0xFFFFFFFC 
Gán eax = esi+20 = 0x3F8
Gán esi + 24 = ecx = 8
Gán eax + esi2 = ecx = 8
esi + 24 += edx = 0x14
Gán eax = 0
5. fn_13
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2 ecx
Gán eax = eax + ecx = 8
Gán esi + 8 = eax = 8
Gán eax = ecx + 4 = 0x3FC
Gán esi + 20 = eax = 0x3FC
Gán eax = 1
6. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi +24 = 0x15
Gán eax = eax + ecx + 1 = 0xC
Gán esi + 4 = eax = 0xC
Gán eax = 5
7. fn_9
esi + 20 (0x3FC) += 0xFFFFFFFC
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0xC
Gán edx + ecx = eax = 0xC
Gán eax = 1
8. fn_14
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = eax + ecx = 0xC
Gán esi + 12 = eax = 0xC
Gán esi + 20 = ecx + 4 = 0x3FC
Gán eax = 1
9. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x1C
Gán eax = eax + ecx + 1 = 3
Gán esi + 4 = eax = 3
Gán eax = 5
10. fn_20
Hàm switch dựa vào giá trị ở esi + 4
Case 3:
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán ecx = địa chỉ của số lượng byte đã đọc
eax += esi + 8 = địa chỉ vùng nhớ 2 + 8
Gọi hàm ReadFile, các kí tự đã đọc ghi vào địa chỉ vùng nhớ 2 + 8
Gán eax = số byte đã đọc được = 0xC
Gán esi + 12 = eax = 0xC
Gán eax = 1
11. fn_11
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 0xC
Gán edx + ecx = eax = 0xC
Gán eax = 1
12. fn_11
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 0xC
Gán edx + ecx = eax = 0xC
Gán eax = 1
13. fn_15
Gán ecx = esi + 20 = 0x3F4
Gán esi2 = ecx + 8 = 0x3FC
So sánh esi2 với esi + 148 (0x400), nhảy nếu lớn hơn
ecx += esi + 136
Gán eax = giá trị ở ecx = 0xC
So sánh eax và ecx + 4, nhảy nếu khác nhau
esi + 16 = esi + 16 or 2 = 2
Gán eax = 1
Gán esi + 20 = esi2= 0x3FC
14. fn_27
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 16 = 2
Gán edx + ecx = eax = 2
Gán eax = 1
15. fn_14
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = eax + ecx = 2
Gán esi + 12 = eax = 2
Gán esi + 20 = ecx + 4 = 0x3FC
Gán eax = 1
16. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x27
Gán eax = eax + ecx + 1 = 0x86
Gán esi + 4 = eax = 0x86
Gán eax = 5
17. fn_9
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x86
Gán edx + ecx = eax = 0x86
Gán eax = 1
18. fn_26
Gán edi = esi + 136 = địa chỉ vùng nhớ 2
Gán edx = esi + 8 = 8
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
edx += edi = địa chỉ vùng nhớ 2 + 8 = Chuỗi input đã nhập 
Gán ebx = esi + 20 = 0x3F4
Gán eax = 1 byte của edx + 2 = kí tự thứ 3 của chuỗi input
Thực hiện lệnh rol al, 2 để dịch bit thanh ghi al sang trái, phần trái nhất đem về bên phải (VD: 0x63 = 0110 0011, sau khi rol 2 là 0x8D = 1000 1101) (Mã hóa kí tự thứ 3)
Gán esi = al 
Gán eax = 1 byte của edx = kí tự đầu tiên của chuỗi input
al += 0x12 (Mã hóa kí tự đầu tiên)
Gán ecx = al 
Gán eax = 1 byte của edx + 1 = kí tự thứ 2 của chuỗi input
al -= 0x78 (Mã hóa kí tự thứ 2)
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
ecx = ecx or eax (Tạo thành cặp kí tự thứ nhất, thứ hai)
Gán eax = 1 byte của edx + 3 = kí tự thứ 4 của chuỗi input
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
esi = esi or ecx (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba)
Thực hiện lệnh ror al, 4 để dịch bit thanh ghi al sang phải, phần phải nhất đem về bên trái (VD: 0x64 = 0110 0100, sau khi ror 4 là 0x46 = 0100 0110) (Mã hóa kí tự thứ 4)
Dịch trái esi 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
esi = esi or eax (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba, thứ tư)
Gán eax = 1
Gán edi + ebx = esi (Lưu chuỗi 4 kí tự đầu đã mã hóa vào vùng nhớ thứ hai + 0x3F4)
19. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x2E
Gán eax = eax + ecx + 1 = 0xBABECAFE
Gán esi + 4 = eax = 0xBABECAFE
Gán eax = 5
20. fn_9
esi + 20 (0x3F4) += 0xFFFFFFFC = 0x3F0
Gán edx = esi + 20 = 0x3F0
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0xBABECAFE
Gán edx + ecx = eax = 0xBABECAFE
Gán eax = 1
21. fn_1
Gán ecx = esi + 20 = 0x3F0
Gán eax = ecx + 8 = 0x3F8
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F0
Gán eax = ecx = 0xBABECAFE
ecx + 4 (địa chỉ vùng nhớ 2 + 0x3F4, nơi chứa chuỗi mã hóa 4 kí tự đầu) += eax (0xBABECAFE)
Gán ecx = esi + 20 = 0x3F0
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự đầu sau khi cộng) với 0, nếu khác thì nhảy tới ABCD
ABCD: 
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F4
Gán esi + 20 = eax = 0x3F4
Gán eax = 1
22. fn_7
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán esi2 = eax + ecx = địa chỉ của vùng nhớ 2 + 0x3F4 = địa chỉ chuỗi mã hóa 4 kí tự đầu
Gán al = esi + 4 = 0x86
Gán ecx = al
ecx = ecx and 0xF = 0x6
Gán eax = esi = giá trị chuỗi mã hóa 4 kí tự đầu
Thực hiện rol eax, cl, ở đây cl = 6, ta sẽ dịch bit cho chuỗi mã hóa 4 kí tự đầu
Gán esi2 + 4 = eax = chuỗi mã hóa 4 kí tự đầu đã dịch bit
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự đầu sau khi dịch bit) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
23. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x36
Gán eax = eax + ecx + 1 = 0x13371337
Gán esi + 4 = eax = 0x13371337
Gán eax = 5
24. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x13371337
Gán edx + ecx = eax = 0x13371337
Gán eax = 1
25. fn_2
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0x13371337
eax = eax – ecx + 4 (trừ cho chuỗi 4 kí tự đầu)
Gán ecx + 4 = eax
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự đầu sau khi trừ) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
26. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x3D
Gán eax = eax + ecx + 1 = 0x13371337
Gán esi + 4 = eax = 0x13371337
Gán eax = 5
27. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x13371337
Gán edx + ecx = eax = 0x13371337
Gán eax = 1
28. fn_3
Gán ecx = esi  + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0x13371337
Xor giá trị tại ecx + 4 (chứa chuỗi mã hóa 4 kí tự) với eax
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự đầu sau khi xor) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
29. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x44
Gán eax = eax + ecx + 1 = 0x2648ED87
Gán esi + 4 = eax = 0x2648ED87
Gán eax = 5
30. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x2648ED87
Gán edx + ecx = eax = 0x2648ED87
Gán eax = 1
31. fn_15
Gán ecx = esi + 20 = 0x3F4
Gán esi2 = ecx + 8 = 0x3FC
So sánh esi2 với esi + 148 (0x400), nhảy nếu lớn hơn
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = giá trị ở ecx = 0x2648ED87
So sánh eax và ecx + 4, nhảy ABCD nếu khác nhau
esi + 16 = esi + 16 or 2 = 2
Gán eax = 1
Gán esi + 20 = esi2= 0x3FC
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán esi + 20 = esi2 = 0x3FC
Gán eax = 1
32. fn_27
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 16 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
33. fn_11
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 2
Gán edx + ecx = eax = 2
Gán eax = 1
34. fn_4
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 2
ecx + 4 = ecx + 4 and eax = 0
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (0) với 0, nếu khác thì nhảy tới ABCD
esi + 16 = esi + 16 or 2 = 2
Gán eax = ecx + 4 = 0x3F8
Gán eax = 1
Gán esi + 20 = eax= 0x3F8
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
35. fn_14
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = eax + ecx = 0
Gán esi + 12 = eax = 0
Gán esi + 20 = ecx + 4 = 0x3FC
Gán eax = 1
36. fn_10
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 8 = 8
Gán edx + ecx = eax = 8
Gán eax = 1
37. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x50
Gán eax = eax + ecx + 1 = 4
Gán esi + 4 = eax = 4
Gán eax = 5
38. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 4
Gán edx + ecx = eax = 4
Gán eax = 1
39. fn_1
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 4
ecx + 4 (8) += eax (4) = 0xC
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (0xC) với 0, nếu khác thì nhảy tới ABCD
ABCD: 
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
40. fn_13
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2 ecx
Gán eax = eax + ecx = 0xC
Gán esi + 8 = eax = 0xC
Gán eax = ecx + 4 = 0x3FC
Gán esi + 20 = eax = 0x3FC
Gán eax = 1
41. fn_26
Gán edi = esi + 136 = địa chỉ vùng nhớ 2
Gán edx = esi + 8 = 0xC
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
edx += edi = địa chỉ vùng nhớ 2 + 0xC = 4 kí tự giữa của chuỗi input đã nhập 
Gán ebx = esi + 20 = 0x3F8
Gán eax = 1 byte của edx + 2 = kí tự thứ 3 của chuỗi 4 kí tự giữa
Thực hiện lệnh rol al, 2 để dịch bit thanh ghi al sang trái, phần trái nhất đem về bên phải (VD: 0x63 = 0110 0011, sau khi rol 2 là 0x8D = 1000 1101) (Mã hóa kí tự thứ 3)
Gán esi = al 
Gán eax = 1 byte của edx = kí tự đầu tiên của chuỗi 4 kí tự giữa
al += 0x12 (Mã hóa kí tự đầu tiên)
Gán ecx = al 
Gán eax = 1 byte của edx + 1 = kí tự thứ 2 của chuỗi 4 kí tự giữa
al -= 0x78 (Mã hóa kí tự thứ 2)
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
ecx = ecx or eax (Tạo thành cặp kí tự thứ nhất, thứ hai)
Gán eax = 1 byte của edx + 3 = kí tự thứ 4 của chuỗi 4 kí tự giữa
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
esi = esi or ecx (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba)
Thực hiện lệnh ror al, 4 để dịch bit thanh ghi al sang phải, phần phải nhất đem về bên trái (VD: 0x64 = 0110 0100, sau khi ror 4 là 0x46 = 0100 0110) (Mã hóa kí tự thứ 4)
Dịch trái esi 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
esi = esi or eax (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba, thứ tư)
Gán eax = 1
Gán edi + ebx = esi (Lưu chuỗi 4 kí tự giữa đã mã hóa vào vùng nhớ thứ hai + 0x3F8)
42. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x59
Gán eax = eax + ecx + 1 = 0xDEADBEEF
Gán esi + 4 = eax = 0xDEADBEEF
Gán eax = 5
43. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0xDEADBEEF
Gán edx + ecx = eax = 0xDEADBEEF
Gán eax = 1
44. fn_2
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0xDEADBEEF
eax = eax – ecx + 4 (trừ cho chuỗi 4 kí tự giữa)
Gán ecx + 4 = eax
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự đầu sau khi trừ) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
45. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x60
Gán eax = eax + ecx + 1 = 0x94C3E659
Gán esi + 4 = eax = 0x94C3E659
Gán eax = 5
46. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x94C3E659
Gán edx + ecx = eax = 0x94C3E659
Gán eax = 1
47. fn_15
Gán ecx = esi + 20 = 0x3F4
Gán esi2 = ecx + 8 = 0x3FC
So sánh esi2 với esi + 148 (0x400), nhảy nếu lớn hơn
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = giá trị ở ecx = 0x94C3E659
So sánh eax và ecx + 4, nhảy ABCD nếu khác nhau
esi + 16 = esi + 16 or 2 = 2
Gán eax = 1
Gán esi + 20 = esi2= 0x3FC
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán esi + 20 = esi2 = 0x3FC
Gán eax = 1
48. fn_27
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 16 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
49. fn_11
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
50. fn_4
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0
ecx + 4 = ecx + 4 and eax = 0
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (0) với 0, nếu khác thì nhảy tới ABCD
esi + 16 = esi + 16 or 2 = 2
Gán eax = ecx + 4 = 0x3F8
Gán eax = 1
Gán esi + 20 = eax= 0x3F8
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
51. fn_14
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = eax + ecx = 0
Gán esi + 12 = eax = 0
Gán esi + 20 = ecx + 4 = 0x3FC
Gán eax = 1
52. fn_10
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 8 = 0xC
Gán edx + ecx = eax = 0xC
Gán eax = 1
53. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x6C
Gán eax = eax + ecx + 1 = 4
Gán esi + 4 = eax = 4
Gán eax = 5
54. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 4
Gán edx + ecx = eax = 4
Gán eax = 1
55. fn_1
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 4
ecx + 4 (0xC) += eax (4) = 0x10
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (0xC) với 0, nếu khác thì nhảy tới ABCD
ABCD: 
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
56. fn_13
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2 ecx
Gán eax = eax + ecx = 0x10
Gán esi + 8 = eax = 0x10
Gán eax = ecx + 4 = 0x3FC
Gán esi + 20 = eax = 0x3FC
Gán eax = 1
57. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x74
Gán eax = eax + ecx + 1 = 4
Gán esi + 4 = eax = 4
Gán eax = 5
58. fn_9
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 4
Gán edx + ecx = eax = 4
Gán eax = 1
59. fn_26
Gán edi = esi + 136 = địa chỉ vùng nhớ 2
Gán edx = esi + 8 = 0x10
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
edx += edi = địa chỉ vùng nhớ 2 + 0x10 = 4 kí tự cuối của chuỗi input đã nhập 
Gán ebx = esi + 20 = 0x3F4
Gán eax = 1 byte của edx + 2 = kí tự thứ 3 của chuỗi 4 kí tự cuối
Thực hiện lệnh rol al, 2 để dịch bit thanh ghi al sang trái, phần trái nhất đem về bên phải (VD: 0x63 = 0110 0011, sau khi rol 2 là 0x8D = 1000 1101) (Mã hóa kí tự thứ 3)
Gán esi = al 
Gán eax = 1 byte của edx = kí tự đầu tiên của chuỗi 4 kí tự cuối
al += 0x12 (Mã hóa kí tự đầu tiên)
Gán ecx = al 
Gán eax = 1 byte của edx + 1 = kí tự thứ 2 của chuỗi 4 kí tự cuối
al -= 0x78 (Mã hóa kí tự thứ 2)
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
ecx = ecx or eax (Tạo thành cặp kí tự thứ nhất, thứ hai)
Gán eax = 1 byte của edx + 3 = kí tự thứ 4 của chuỗi 4 kí tự cuối
Dịch trái ecx 8 bit (VD: 0x73 thành 0x7300)
esi = esi or ecx (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba)
Thực hiện lệnh ror al, 4 để dịch bit thanh ghi al sang phải, phần phải nhất đem về bên trái (VD: 0x64 = 0110 0100, sau khi ror 4 là 0x46 = 0100 0110) (Mã hóa kí tự thứ 4)
Dịch trái esi 8 bit (VD: 0x73 thành 0x7300)
Gán eax = al
esi = esi or eax (Tạo thành cặp kí tự thứ nhất, thứ hai, thứ ba, thứ tư)
Gán eax = 1
Gán edi + ebx = esi (Lưu chuỗi 4 kí tự cuối đã mã hóa vào vùng nhớ thứ hai + 0x3F4)
60. fn_7
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán esi2 = eax + ecx = địa chỉ của vùng nhớ 2 + 0x3F4 = địa chỉ chuỗi mã hóa 4 kí tự cuối
Gán al = esi + 4 = 4
Gán ecx = al
ecx = ecx and 0xF = 4
Gán eax = esi = giá trị chuỗi mã hóa 4 kí tự cuối
Thực hiện ror eax, cl, ở đây cl = 4, ta sẽ dịch bit cho chuỗi mã hóa 4 kí tự cuối
Gán esi2 + 4 = eax = chuỗi mã hóa 4 kí tự cuối đã dịch bit
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự cuối sau khi dịch bit) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
61. fn_6
Gán ecx = esi + 20 = 0x3F8
Gán eax = ecx + 8 = 0x400
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Dùng not ecx + eax (thực hiện đảo bit cho chuỗi 4 kí tự mã hóa cuối)
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 20 = 0x3F8
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự cuối sau khi đảo bit) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = 1
62. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x7D
Gán eax = eax + ecx + 1 = 0xABBAABBA
Gán esi + 4 = eax = 0xABBAABBA
Gán eax = 5
63. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0xABBAABBA
Gán edx + ecx = eax = 0xABBAABBA
Gán eax = 1
64. fn_3
Gán ecx = esi  + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0xABBAABBA
Xor giá trị tại ecx + 4 (chứa chuỗi mã hóa 4 kí tự cuối) với eax
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự cuối sau khi xor) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
65. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x84
Gán eax = eax + ecx + 1 = 0x89ABCDEF
Gán esi + 4 = eax = 0x89ABCDEF
Gán eax = 5
66. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x89ABCDEF
Gán edx + ecx = eax = 0x89ABCDEF
Gán eax = 1
67. fn_1
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0x89ABCDEF
ecx + 4 (chuỗi mã hóa 4 kí tự cuối) += eax (0x89ABCDEF) 
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự cuối sau khi cộng) với 0, nếu khác thì nhảy tới ABCD
ABCD: 
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = ecx + 4 = 0x3F8
Gán esi + 20 = eax = 0x3F8
Gán eax = 1
68. fn_6
Gán ecx = esi + 20 = 0x3F8
Gán eax = ecx + 8 = 0x400
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Dùng not ecx + eax (thực hiện đảo bit cho chuỗi 4 kí tự mã hóa cuối)
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 20 = 0x3F8
So sánh giá trị eax + ecx + 4 (chuỗi mã hóa 4 kí tự cuối sau khi đảo bit) với 0, nếu khác thì nhảy tới ABCD
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán eax = 1
69. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x8C
Gán eax = eax + ecx + 1 = 0x5469A57F
Gán esi + 4 = eax = 0x5469A57F
Gán eax = 5
70. fn_9
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 0x5469A57F
Gán edx + ecx = eax = 0x5469A57F
Gán eax = 1
71. fn_15
Gán ecx = esi + 20 = 0x3F4
Gán esi2 = ecx + 8 = 0x3FC
So sánh esi2 với esi + 148 (0x400), nhảy nếu lớn hơn
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = giá trị ở ecx = 0x5469A57F
So sánh eax và ecx + 4, nhảy ABCD nếu khác nhau
esi + 16 = esi + 16 or 2 = 2
Gán eax = 1
Gán esi + 20 = esi2= 0x3FC
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán esi + 20 = esi2 = 0x3FC
Gán eax = 1
72. fn_27
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 16 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
73. fn_11
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
74. fn_4
Gán ecx = esi + 20 = 0x3F4
Gán eax = ecx + 8 = 0x3FC
So sánh eax với esi + 148 (0x400), nếu lớn hơn thì nhảy
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = ecx = 0
ecx + 4 = ecx + 4 and eax = 0
Gán ecx = esi + 20 = 0x3F4
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
So sánh giá trị eax + ecx + 4 (0) với 0, nếu khác thì nhảy tới ABCD
esi + 16 = esi + 16 or 2 = 2
Gán eax = ecx + 4 = 0x3F8
Gán eax = 1
Gán esi + 20 = eax= 0x3F8
75. fn_14
Gán ecx = esi + 20 = 0x3F8
Gán eax = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = eax + ecx = 0
Gán esi + 12 = eax = 0
Gán esi + 20 = ecx + 4 = 0x3FC
Gán eax = 1
76. fn_8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 24 = 0x97
Gán eax = eax + ecx + 1 = 2
Gán esi + 4 = eax = 2
Gán eax = 5
77. fn_9
esi + 20 (0x3FC) += 0xFFFFFFFC = 0x3F8
Gán edx = esi + 20 = 0x3F8
Gán ecx = esi + 136 = địa chỉ vùng nhớ 2
Gán eax = esi + 4 = 2
Gán edx + ecx = eax = 2
Gán eax = 1
78. fn_11
esi + 20 (0x3F8) += 0xFFFFFFFC = 0x3F4
Gán edx = esi + 20 = 0x3F4
Gán ecx = địa chỉ vùng nhớ 2
Gán eax = esi + 12 = 0
Gán edx + ecx = eax = 0
Gán eax = 1
79. fn_15
Gán ecx = esi + 20 = 0x3F4
Gán esi2 = ecx + 8 = 0x3FC
So sánh esi2 với esi + 148 (0x400), nhảy nếu lớn hơn
ecx += esi + 136 = địa chỉ vùng nhớ 2 + 0x3F4
Gán eax = giá trị ở ecx = 0
So sánh eax và ecx + 4, nhảy ABCD nếu khác nhau
ABCD:
esi + 16 = esi + 16 and 0xFFFFFFFD = 0
Gán esi + 20 = esi2 = 0x3FC
Gán eax = 1
80. fn_16
So sánh esi + 16 với 2, khác nhau thì nhảy tới ABCD
ABCD:
Gán eax = 5
81. fn_21
esi + 16 = esi + 16 or 1
Gán eax = 1
```