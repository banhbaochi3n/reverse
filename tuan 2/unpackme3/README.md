# unpackme3

Chương trình được pack bởi ASPack.
![info](image.png)

Load chương trình vào x32dbg, chạy chương trình để vào entry point(click vào `Run` hoặc gõ `g` tại `Command`).
![start](image-1.png)
![fake_oep](image-2.png)

F7 1 lần, ta thấy thay đổi trên ESP, sử dụng phương pháp giống như unpack petite, chuột phải vào địa chỉ ESP chọn `Follow in dump`, select 4 byte đầu của dump và đặt breakpoint.
![bp](image-3.png)

Chạy chương trình 1 lần, và F8 cho đến khi được kết quả như hình.
![ril_oep](image-4.png)
Đã tìm được đúng OEP của chương trình.

Dùng Scylla dump và fix dump.

Xoá thunk bị sai và dump.
![fix](image-5.png)

Fix dump và hoàn thành.
![done](image-6.png)