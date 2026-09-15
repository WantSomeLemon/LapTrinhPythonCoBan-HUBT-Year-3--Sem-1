## Yêu cầu:
**Python:** 3.14.5

**Pygame:** pygame-ce 2.5.8 (Phiên bản cộng đồng Pygame Community Edition)

## Hướng dẫn thiết lập môi trường ảo và cài đặt Pygame từ đầu

### **Bước 1:** Mở Terminal tại thư mục dự án
- Mở thư mục chứa dự án game của bạn bằng PyCharm hoặc VS Code, sau đó mở cửa sổ dòng lệnh Terminal ở bên trong phần mềm đó.

### **Bước 2:** Tạo môi trường ảo (.venv)
- Chạy lệnh sau trong Terminal để tạo thư mục môi trường ảo tên là .venv:
- ```terminaloutput
    python -m venv .venv
  ```
(Lệnh này sẽ tạo ra một thư mục ẩn tên là .venv chứa phiên bản Python riêng cho dự án của bạn).

### **Bước 3:** Kích hoạt môi trường ảo (Activate)
- Trước khi cài đặt thư viện, bạn phải kích hoạt môi trường ảo để hệ thống biết sử dụng .venv này:
  - Nếu bạn dùng PowerShell (mặc định trên Windows 11):
    - ```terminaloutput
      .\.venv\Scripts\Activate.ps1
      ```
    (Nếu gặp lỗi chặn quyền script, bạn chạy lệnh Set-ExecutionPolicy Unrestricted -Scope Process trước, rồi chạy lại lệnh kích hoạt trên).

  - Nếu bạn dùng Command Prompt (CMD):
    - ```terminaloutput
      .\.venv\Scripts\activate.bat
      ```
    Sau khi kích hoạt thành công, bạn sẽ thấy chữ (.venv) xuất hiện ở đầu dòng lệnh trong Terminal.

### **Bước 4:** Cài đặt pygame-ce
- Vì bạn đang dùng Python 3.14.5, gói pygame gốc cũ sẽ bị lỗi biên dịch. Hãy dùng pygame-ce (phiên bản cộng đồng chuẩn xác nhất):
- ```terminaloutput
  pip install pygame-ce
  ```
- Đợi vài giây để pip tải và cài đặt xong vào môi trường .venv.

### **Bước 5:** Kiểm tra lại
- Bạn có thể kiểm tra xem thư viện đã nằm trong .venv chưa bằng lệnh:
- ```terminaloutput
    pip list
  ```
- Nếu thấy tên pygame-ce xuất hiện trong danh sách là bạn đã hoàn tất thiết lập môi trường và sẵn sàng viết code game!