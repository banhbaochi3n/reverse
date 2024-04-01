# anti_debug1

Chương trình yêu cầu chạy dưới quyền administrator, giao diện như dưới đây:
![ui](image.png)

Có vẻ như chương trình nhận 1 string đầu vào, và nếu check đúng thì chúng ta sẽ có flag hay gì đấy :D
![error_messge_box](image-1.png)

Trước khi reverse, ta kiểm tra các thuộc tính của chương trình trước, sử dụng CFF Explorer.
![file_info](image-2.png)
Chương trình viết bằng C++, không có packer, hoàn toàn là chương trình C++ điển hình.

Tiến hành reverse chương trình, kiểm tra trong tab `Import`:
![debugger_present](image-3.png)
Chương trình có sử dụng `IsDebuggerPresent`.

Ta cùng xem hàm `main`.

