# Personal-finance-management
web quản lí tiền bạc đơn giản có trợ lí ảo gợi ý thông minh
Hướng Dẫn Chạy Ứng Dụng & Lấy API Key
Chào bạn, file hướng dẫn này sẽ giúp bạn giải quyết 2 vấn đề quan trọng:
Lấy API Key để sử dụng tính năng phân tích tài chính thông minh của Gemini AI.
Chạy ứng dụng đúng cách trên máy tính của bạn để tất cả các tính năng hoạt động.
1. Hướng Dẫn Lấy Gemini API Key (Quan Trọng)
Để sử dụng tính năng "Phân Tích Thông Minh", bạn cần có một "chìa khóa" API của riêng mình. Google cung cấp miễn phí và cách lấy rất đơn giản.
Bước 1: Truy cập Google AI Studio
Mở trình duyệt web và truy cập vào địa chỉ: https://aistudio.google.com/
Bước 2: Lấy API Key
Sau khi đăng nhập bằng tài khoản Google, bạn sẽ thấy giao diện chính. Hãy nhấn vào nút "Get API key" ở menu bên trái.
Bước 3: Tạo API Key mới
Một cửa sổ sẽ hiện ra, hãy nhấn vào nút "+ Create API key in new project".
Bước 4: Sao chép (Copy) API Key
Hệ thống sẽ ngay lập tức tạo ra một chuỗi ký tự dài, đó chính là API Key của bạn. Hãy nhấn vào biểu tượng hai hình chữ nhật để sao chép nó.
Bước 5: Dán Key vào Ứng Dụng
Quay trở lại ứng dụng, vào mục "Phân tích" và dán key bạn vừa sao chép vào ô "Gemini API Key của bạn". Ứng dụng sẽ tự động lưu lại key này cho những lần sử dụng sau.
2. Tại Sao Cần Chạy Ứng Dụng Trên Máy Chủ Cục Bộ?
Khi bạn mở một file .html trực tiếp từ máy tính (với đường dẫn file:///...), trình duyệt sẽ áp dụng một chính sách bảo mật gọi là CORS (Cross-Origin Resource Sharing). Chính sách này ngăn không cho mã JavaScript trong file của bạn gửi yêu cầu đến các máy chủ bên ngoài, ví dụ như API của Google Gemini.
Để ứng dụng có thể gọi được API Gemini, bạn cần chạy nó thông qua một máy chủ web cục bộ (local web server). Cách làm rất đơn giản ở mục dưới đây.
3. Cách Chạy Ứng Dụng Trên Máy Tính
Yêu Cầu:
Máy tính của bạn đã cài đặt Python. (Hầu hết các máy Mac và Linux đã có sẵn. Người dùng Windows có thể tải từ python.org).
Các Bước Thực Hiện:
Bước 1: Lưu các file vào cùng một thư mục
Đảm bảo 2 file tro-ly-tai-chinh-final.html và server.py nằm chung trong một thư mục (folder).
Bước 2: Mở Terminal (Command Prompt)
Windows: Nhấn Win + R, gõ cmd và nhấn Enter.
Mac/Linux: Mở ứng dụng "Terminal".
Bước 3: Di chuyển đến thư mục chứa file
Sử dụng lệnh cd để đi đến thư mục bạn vừa lưu file.
Ví dụ: Nếu bạn lưu ở Desktop\TaiChinh, bạn gõ: cd Desktop\TaiChinh
Bước 4: Chạy máy chủ
Gõ lệnh sau vào Terminal và nhấn Enter:
python -m http.server 8000

(Nếu lệnh trên không hoạt động, thử lệnh python3 -m http.server 8000 hoặc python -m SimpleHTTPServer 8000)
Bước 5: Mở ứng dụng trên trình duyệt
Mở trình duyệt web của bạn (Chrome, Firefox,...) và truy cập vào địa chỉ sau:
http://localhost:8000/tro-ly-tai-chinh-final.html
Bây giờ, ứng dụng của bạn sẽ chạy hoàn hảo với đầy đủ các tính năng!
