# Tra cứu phạt nguội tự động bằng Python

Project này sử dụng Selenium và Tesseract OCR để tự động tra cứu phạt nguội phương tiện giao thông trên trang(https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html). Kết quả sẽ được in ra màn hình. Chương trình có thể chạy tự động theo lịch định sẵn.

## Cài đặt

### 1. Cài đặt Python packages
Chạy lệnh sau trong thư mục project:
pip install selenium pillow pytesseract schedule requests

### 2. Cài đặt Google Chrome và ChromeDriver
- Tải và cài đặt [Google Chrome](https://www.google.com/chrome/)
- Tải [ChromeDriver](https://chromedriver.chromium.org/downloads) đúng với phiên bản Chrome bạn đang dùng.
- Giải nén và đặt `chromedriver.exe` vào thư mục chứa mã nguồn hoặc thêm vào PATH hệ thống.

### 3. Cài đặt Tesseract OCR
- Tải và cài đặt [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Mặc định, đường dẫn Tesseract trong code là:
  C:\Program Files\Tesseract-OCR\tesseract.exe
  Nếu bạn cài ở vị trí khác, hãy sửa lại biến sau trong file `baiTap_Lon.py`:
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' (ĐƯỜNG_DẪN_TỚI_TESSERACT.EXE)

## Sử dụng
1. Mở file `baiTap_Lon.py` và chỉnh sửa biến `bienSo` và `loaiXe` cho phù hợp với phương tiện bạn muốn tra cứu.
2. Chạy chương trình: python baiTap_Lon.py
3. Kết quả sẽ được in ra màn hình khi đến thời gian đã lên lịch trong code.

## Lưu ý
- Bạn có thể chỉnh sửa thời gian tra cứu tự động bằng cách thay đổi các dòng:
  schedule.every().day.at("17:48").do(tra_cuu_phat_nguoi)
  schedule.every().day.at("17:04").do(tra_cuu_phat_nguoi)

## Mô tả về ý tưởng code 
Đúng giờ thì
-B1: Sẽ vào trang web 
-B2:+Dùng while True để chạy nhập biển số,chọn loại xe tự động
    +Sau khi nhập xong thì tìm tới ảnh captchas chụp lại , sau đó xử lý ảnh chuyển xám và tăng đồ tương phản anh lên
    +Xong dùng thư viện pytesseract lấy chữ số trong cap cha ra và bỏ khoảng trắng đầu và cuối
    +Chuyển sang nhận theo kiểu a-z0-9 ,và lấy 6 ký tự đầu 
    +Nhập 6 ký tự đầu  đó và ô text captchas và bấm tra cứu
B3: Nếu nhập và tra cứu đúng thì hiển thị : thời gian,hành vi và trạng thái, ngược lại nếu sai captchas thì refect sau đó chạy lại bước 2: đến khi nào đúng.
    


## Liên hệ
Nếu có thắc mắc hoặc cần hỗ trợ, vui lòng tạo issue trên GitHub repo này.