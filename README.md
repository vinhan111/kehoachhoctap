# Kế Hoạch Học Tập Caissa Chess School

Xin chào!

Đây là một ứng dụng web Flask đơn giản được thiết kế để giúp giáo viên tại Caissa Chess School dễ dàng tạo ra kế hoạch học tập phù hợp với học sinh dựa trên yêu cầu ELO và trình độ test đầu vào của họ.

## Tính Năng

- **Tạo Kế Hoạch Học Tập**: Giáo viên có thể tạo và quản lý kế hoạch học tập cho từng học sinh.
- **Đánh Giá Học Sinh**: Hệ thống cho phép đánh giá trình độ của học sinh thông qua các bài kiểm tra đầu vào.
- **Tùy Chỉnh Theo Yêu Cầu**: Kế hoạch học tập có thể được tùy chỉnh dựa trên yêu cầu ELO của học sinh.

## Công Nghệ Sử Dụng

- **Flask**: Framework web cho Python.
- **Flask-RESTful**: Để xây dựng API RESTful.
- **Flask-SQLAlchemy**: Để quản lý cơ sở dữ liệu.
- **Flask-Migrate**: Để thực hiện các thao tác di chuyển cơ sở dữ liệu.
- **Marshmallow**: Để tuần tự hóa và xác thực dữ liệu.
- **Flask-JWT-Extended**: Để xử lý xác thực JWT.

## Cài Đặt

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. **Cài Đặt Các Gói Cần Thiết**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy Ứng Dụng**:
   ```bash
   flask run
   ```

## Sử Dụng

- Truy cập vào `http://localhost:5001` để sử dụng ứng dụng.
- Đăng nhập với tài khoản giáo viên để bắt đầu tạo kế hoạch học tập.

## Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng. Vui lòng tạo một pull request hoặc mở issue nếu bạn gặp vấn đề.

## Giấy Phép

Ứng dụng này được phát hành dưới giấy phép MIT. Vui lòng xem tệp LICENSE để biết thêm chi tiết.

## Liên Hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với tôi qua email: phamvinhan@gmail.com.
