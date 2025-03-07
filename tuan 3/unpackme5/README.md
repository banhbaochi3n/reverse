# unpackme5

Chương trình được pack bỏi MPRESS.
![info](image.png)

Chạy script để tìm OEP: [Script](https://github.com/x64dbg/Scripts/blob/master/Mpress2xx.txt)

```
//start
msg "Mpress 2.xx OEP Finder"
msg "make sure you're at the entry point of the program before you continue"
pause

//clear breakpoints
bc
bphwc

//find jump ret
find cip,"83C47C5B5E5F5DC3E9" //some pattern
cmp $result,0
jnz AllOK
find cip,"8B45F85EC9C20400E9" //another pattern
cmp $result,0
jnz AllOK

jmp error1



AllOK:
log "found: {0}", $result+8
//go to jump
bp $result+8
erun
bc
sti

//find OEP Jump
find cip,"AAB8?E010000AB61E9" //some pattern
log "found: {0}", $result+8
cmp $result,0
je error2

bc
//go to OEP
bp $result+8
erun
bc
sti

cmt cip,"OEP"

//finish script
ret

error1:
msg "didn't find jump"
ret

error2:
msg "didn't find oep jump"
ret
```

Trước khi chạy script, chúng ta chạy chương trình 1 lần để nhảy tới entry point.
![fake_oep](image-1.png)

Qua tab `Script`, gõ phím cách để chạy script.
![script](image-2.png)
![finished](image-3.png)

Sau khi script chạy xong, F8 để nhảy tới OEP đúng.
![done_script](image-4.png)

![ril_oep](image-5.png)

Áp dụng phương pháp như các challenge trước và tiếp tục unpack.

Delete thunk không hợp lệ. <br>
![thunk](image-6.png)

Dump section. <br>
![dump_section](image-7.png)

Fix dump. <br>
![fix_dump](image-8.png)

Chạy được thành công. <br>
![oge](image-9.png)

Một điều mình vẫn chưa hiểu, đó là dù unpack xong nhưng DIE vẫn detect được packer -_-. <r>
![lmao](image-10.png)

Nhưng trong IDA vẫn có thể xem được đầy đủ các function.
![lol](image-11.png)

Các string trong chương trình hiển thị đầy đủ.
![lul](image-12.png)
