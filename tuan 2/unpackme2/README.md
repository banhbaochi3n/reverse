# unpackme2

![info](image.png)
Chương trình được pack bằng Petite v2.X

Thả chương trình vào x32dbg
![dbg](image-1.png)
Bấm vào nút mũi tên hướng về bên phải để chạy chương trình, chương trình sẽ tự động nhảy về entry point.
![button](image-2.png)
![entry_point](image-3.png)

F7 cho tới khi chạy qua `pushad`.

Ta nhìn qua phần register, click vào address thanh ghi ESP, chọn `Follow in dump`.
![follow_dump](image-4.png)

Đỉnh stack sẽ luôn bắt đầu với `9F 91`.
![stack](image-5.png)
Chọn 4 byte đầu, chuột phải chọn `Breakpoint` -> `Hardware, Access` -> `Dword`.
![breakpoint](image-6.png)

Run chương trình 1 lần nữa, ta sẽ nhảy qua `popad` tại lệnh `lea`.
![popad](image-7.png)

F8 liên tục cho tới khi dừng tại đây.
![mov](image-8.png)

Run thêm 1 lần nữa.
![push](image-9.png)

Và F7 liên tục cho tới khi được như hình dưới đây là đã gặp được entry point của chương trình(**CHÚ Ý**: nên spam F7 từ tốn, nếu chạy lố sẽ không quay lại được và phải quay lại từ đầu :">).
![OEP](image-10.png)

Giờ cần sửa IAT, `Ctrl + I` để mở Scylla.
![scylla](image-11.png)
Chọn `IAT Autosearch` -> `Get Imports`.

Chuột trái chọn các thunk có dấu X và delete.
![thunk](image-12.png)

Sau đó vào `File` -> `Dump Section`.
![section](image-13.png)

Chọn `Dump`. Sau khi lưu section ra file khác, ta chọn `Fix Dump` để sửa lại.
![fix](image-14.png)

Tuy nhiên file vẫn chưa chạy được ngay, giờ cần sửa quyển cho section `petite` để có thể thực thi.
Load file dump vào `CFF Explorer`, sửa `Characteristics` thành `E0000060` và save lại.
![execute_perm](image-15.png)

Chương trình đã có thể chạy được.
![runnable](image-16.png)

![succ](image-17.png)
Unpack thành công.