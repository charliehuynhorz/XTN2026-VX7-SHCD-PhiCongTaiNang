# Jet Rush Controller - Điều khiển trò chơi Jet Rush bằng cử chỉ tay (AI-GENERATED PPROJECT!)

## Giới thiệu

**Jet Rush Controller** là một ứng dụng Python cho phép bạn điều khiển trò chơi **Jet Rush** trên CrazyGames bằng cử chỉ tay thông qua webcam. Ứng dụng sử dụng công nghệ nhận diện tay (Hand Detection) từ MediaPipe để phát hiện và xử lý chuyển động tay, sau đó tự động phát các phím lệnh cho trò chơi.

## Cài đặt game Phi Công Tài Năng:

1. **Tải game Phi Công Tài Năng**
   - [Tải Phi_Cong_Tai_Nang.zip (Google Drive)](https://drive.google.com/file/d/1w-FQGpa2JVAavpHsoKE0iVZ84gd6R4Op/view?usp=drive_link)

## Chức năng chính

### 1. **Điều khiển di chuyển bằng tay**
- **Di chuyển sang trái**: Đưa tay sang bên trái so với vị trí giữa màn hình
- **Di chuyển sang phải**: Đưa tay sang bên phải so với vị trí giữa màn hình
- **Trung tâm**: Tay ở vị trí giữa thì không phát lệnh di chuyển

### 2. **Nhảy bằng cử chỉ ngón tay**
- Nếu chỉ có **một ngón tay duỗi thẳng** (ngón trỏ), ứng dụng sẽ gửi phím `SPACE` để thao tác bắt đầu game

### 3. **Mở game tự động**
- Ứng dụng sẽ tự động mở trò chơi Jet Rush từ CrazyGames trong trình duyệt
- Game window sẽ được đặt ở bên trái màn hình (65% chiều rộng)
- Camera window sẽ được đặt ở bên phải để bạn có thể thấy cử chỉ tay

### 4. **Debug hiển thị trực quan**
- Hiển thị trạng thái hiện tại: `LEFT`, `RIGHT`, `CENTER`
- Hiển thị trạng thái nhảy: `SPACE`
- Vẽ các đường giới hạn (deadzone) để nhận biết vùng hoạt động
- Vẽ vòng tròn cho vị trí hiện tại của tay

## Cấu hình

File `config.py` chứa các thông số cấu hình:

```python
DEADZONE = 40           # Khoảng cách từ tâm để kích hoạt lệnh (pixels)
SMOOTHING = 5           # Số frame để làm mượt chuyển động tay
WEB_RATIO = 0.65        # Tỉ lệ chiều rộng màn hình dành cho game (65%)
WINDOW_TITLE_KEYS = ("Jet Rush", "CrazyGames", "Chrome", "Edge")  # Tên cửa sổ cần tìm
GAME_URL = "https://www.crazygames.com/vn/game/jet-rush"  # URL game
```

## Yêu cầu

- Python 3.7+
- Webcam
- Trình duyệt (Chrome, Edge, Firefox)
- Internet connection

## Cài đặt

### 1. Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

Hoặc cài đặt thủ công:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

### 2. Chạy ứng dụng

```bash
python main.py
```

## Cấu trúc dự án

```
VX7-GAMEIT/
├── main.py                    # File chính, điểm khởi động
├── config.py                  # Cấu hình các thông số
├── camera.py                  # Xử lý camera và vẽ debug
├── hand_control.py            # Xử lý cử chỉ tay, phát phím
├── game_window.py             # Mở game và sắp xếp cửa sổ
├── requirements.txt           # Danh sách thư viện cần thiết
└── README.md                  # Tệp hướng dẫn này
```

## Cách sử dụng

1. **Chạy ứng dụng**:
   ```bash
   python main.py
   ```

2. **Chờ game mở tự động** (khoảng 5 giây):
   - Game window sẽ mở ở bên trái màn hình
   - Camera window sẽ mở ở bên phải

3. **Điều khiển**:
   - Di chuyển tay **sang trái/phải** để điều khiển nhân vật
   - **Giơ một ngón tay** (ngón trỏ) để nhảy
   - Nhấn **ESC** hoặc đóng cửa sổ camera để thoát

4. **Tinh chỉnh**:
   - Nếu độ nhạy không vừa ý, điều chỉnh `DEADZONE` trong `config.py`
   - Nếu chuyển động bị lag, điều chỉnh `SMOOTHING` trong `config.py`