B1: TẢI TESSERACT

Youtube: https://www.youtube.com/watch?v=Tj-u1JDhpog&t=202s

Vào link https://github.com/UB-Mannheim/tesseract/wiki chọn dòng: tesseract-ocr-w64-setup-5.4.0.20240606.exe (64 bit) nhấn vào tải xuống và cài đặt. Copy đường dẫn đến thư mục Tesseract.

- bấm windows + R gõ: rundll32.exe sysdm.cpl, EditEnvironmentVariables, sau đó chọn Path cái bảng ở trên. Chọn nút Edit ở dưới. Sau đó chọn nút New. Dán đường dẫn tới thư mục và và nhấn OK -> OK.

B2: TẢI POPPLER

- Vào link : https://github.com/oschwartz10612/poppler-windows/releases tải file Release-24.02.0-0.zip sau đó giải nén, vào cái đã giải nén mở thư mục libary sau đó chọn thư mục bin và copy đường dẫn tới thư mục bin. Ví dụ: D:\Download\Release-24.02.0-0\poppler-24.02.0\Library\bin

- bấm windows + R gõ: rundll32.exe sysdm.cpl, EditEnvironmentVariables, sau đó chọn Path cái bảng ở trên. Chọn nút Edit ở dưới. Sau đó chọn nút New. Dán đường dẫn tới thư mục bin và và nhấn OK -> OK.

B3: CHẠY DỰ ÁN TRÊN VSCODE

- Tải Python bản 3.12.3 tại link: https://www.python.org/downloads/release/python-3123/ chọn cái: Windows installer (64-bit). Cài đặt python vào máy nhớ ấn: Add pyhon.exe to PATH.

- Cài xong mở dự án trên VSCODE lên bấm: ctrl + shift + P chọn Python: Select Interpreter -> thư mục dự án -> Create Virtual Environment... -> Venv -> thư mục dự án -> python 3.12.3 -> tích vào requirements.txt -> nhấn OK

- Sau khi chờ nó cài xong chuột phải vào thư mục dự án chọn Open In integrated Terminal
gõ: 
.\.venv\Scripts\activate (kích hoạt máy ảo)
sau đó: python app.py (để chạy)
