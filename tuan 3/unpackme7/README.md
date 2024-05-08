# unpackme7

Chương trình chạy trên Windows XP, pack bằng Yoda's Protector. Sau một hồi tìm hiểu thì biết được loại packer này còn bao gồm anti-debug.
![info](image.png)

Tại setting, chọn `Break on new module`, sau đó F9.

![start](image-1.png)

F9 2 lần cho tới khi xuất hiện `User32.dll` như hình.

![user32](image-2.png)

Chuột phải vào `User32.dll`, chọn `View code`, ta được như trên.

`Ctrl + G` tìm `BlockInput`.

![block](image-3.png)

![nop](image-4.png)

Chuột phải vào đoạn asm của `BlockInput`, chuột phải chọn `Binary` -> `Fill with NOPs`.

Tương tự trên, tìm `IsDebuggerPresent`.

![s](image-5.png)

![nop](image-6.png)

Fill NOP.

![haha](image-7.png)

Ghi 0 vào `eax` để disable debugger detection.

![ss](image-8.png)

Cuối cùng là tìm `GetCurrentProcessId`.

![nop](image-9.png)

Fill NOP.

Tiếp theo tìm PID của OllyDbg, ta sẽ cần PID để set cho `eax`.

![634](image-10.png)

![axc](image-11.png)

Click nút `M` trên menu bar để vào memory map, set breakpoint tại phần `Code`, sau đó F9.

![b4_oep](image-12.png)

![oep](image-13.png)

Đã tới được OEP.

Dùng plugin để dump.

![dump](image-14.png)

Sau đó scylla fix dump là hoàn thành.

![fix](image-15.png)

Delete các thunk không hợp lệ.

![del](image-16.png)

![done](image-17.png)