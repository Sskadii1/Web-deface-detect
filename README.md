# Web-deface-detect
Lấy cảm hứng từ J4FSec, họ đã tạo ra một dạng model detect khá mạnh, tuy nhiên tôi muốn triển khai trên ubuntu CLI.
Trong dự án này, tôi muốn tập trung vào phát hiện website defacement bằng cách kết hợp công nghệ học sâu (Deep Learning) với  trình duyệt Headless Chrome. 

Mục đích dự án 
Nhận diện kịp thời các biến đổi bất thường trong giao diện người dùng của website, nhằm phát hiện sớm các hành vi tấn công thay đổi nội dung (defacement) có chủ đích.
Tự động ghi nhận và lưu trữ nhật ký chi tiết của từng phiên kiểm tra, bao gồm thời gian, địa chỉ URL, kết quả phân tích và mức độ tin cậy, phục vụ công tác phân tích sự kiện và truy vết sự cố.
Dễ dàng tích hợp vào các hệ thống giám sát an ninh hiện hữu, hỗ trợ triển khai linh hoạt trong môi trường thực tế và nâng cao hiệu quả giám sát liên tục.

  Bao gồm:
    Tensorflow
    Numpy
    Pillow
    Requests
    Chrome(headless)
    sequential_3 (Total params: 7,896,869) **https://github.com/J4FSec/Shu**

Cách cài đặt(ubuntu): 
  
  1. Các thư viện Python cần thiết:
     ```pip install tensorflow numpy Pillow requests```
  2. Cài đặt trình duyệt Google Chrome ở trạng thái Headless
     ```sudo apt install google-chrome-stable```

  Thư viện liên quan đến headless rendering
          ```sudo apt install -y fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
          libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 \
          libxcomposite1 libxdamage1 libxrandr2 xdg-utils```

    Trong trường hợp ubuntu của bạn sử dụng ubuntu GUI:
      '''sudo apt install -y python3-dev build-essential libssl-dev libffi-dev \
          libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev \
          libfreetype6-dev libpng-dev'''

      **Nếu Chrome bị block bởi AppArmor hoặc SELinux, bạn cần cấu hình lại security policy**

  3. Kiểm tra môi trường cài 
    Xác minh phiên bản TensorFlow:
    ```python3 -c "import tensorflow as tf; print(tf.__version__)"```
    Xác minh phiên bản Chrome:
    ```google-chrome --version```
    Kiểm tra khả năng hoạt động của Chrome ở chế độ Headless:
    Thực hiện thử nghiệm bằng cách chụp ảnh một trang web cụ thể:
   ``` google-chrome --headless --no-sandbox --disable-gpu \
    --screenshot=screenshot.png --window-size=1280,720 https://www.google.com```

    **size tôi chụp ở đây của tôi là 1280*720, một số trường hợp khác thì thay đổi size chụp**

  4. Cài script và model

  ```wget https://raw.githubusercontent.com/J4FSec/In0ri/main/final_model.h5```
  ```a```



  
