# unpackme6

Chương trình được pack bởi VMProtect.
![info](image.png)


Ý tưởng là sẽ đặt breakpoint tại VirtualProtect.
![orig](image-1.png)

F9 để nhảy tới entry point.
![fake_ep](image-2.png)

Tại đây, đặt breakpoint tại VirtualProtect bằng command `bp VirtualProtect`.
![command](image-3.png)

Vào tab `Memory Map`, chuột phải vào `.text` chọn `Follow in Dump`.
![dump](image-4.png)

Hiện tại dump chưa có data gì, F9 cho tới khi dump có data.
![dump_none](image-5.png)

![dump_data](image-6.png)

Quay lại tab `Memory Map`, đặt `Memory Breakpoint` -> `Access` -> `Restore`. Section `.text` hiện đang có quyền Write, ta F9 cho tới khi mất quyền Write. Trước đó xoá breakpoint cũ tại `VirtualProtect`.

![delet_bp](image-8.png)

![mem_bp](image-7.png)

Tiếp tục run cho tới khi gặp OEP tại `AC13088`.
![ril_oep](image-9.png)

Tương tự các câu trước, dùng scylla search IAT, xoá các thunk không hợp lệ, dump và fix dump.

Load file dump vừa fix vào CFF Explorer, vào tab `Section Headers`, xoá section `.vcs0` và `.vcs1`.

![sec0](image-10.png)

![sec1](image-11.png)

Vào tab `Rebuilder`, chọn `Rebuild`.
![rebuild](image-12.png)

Chọn `File -> Save As`.
![save](image-13.png)

Hoàn thành unpack.
![done](image-14.png)

**P/s**: Nhưng vì một vài lí do gì đó mà file unpack không chạy được, dù theo lý thuyết đã dump đúng tại OEP của chương trình :">