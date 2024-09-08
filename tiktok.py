# pip install yt-dlp

import os
from yt_dlp import YoutubeDL

def download_tiktok_videos(user_id, download_path='downloads'):
    # Tạo thư mục lưu video nếu chưa tồn tại
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Định nghĩa cấu hình cho yt-dlp
    ydl_opts = {
        # Đổi tên file tải về theo định dạng user_id + số thứ tự
        'outtmpl': os.path.join(download_path, f'{user_id}_%(autonumber)04d.%(ext)s'),
        'format': 'best',  # Tải chất lượng tốt nhất
        'ignoreerrors': True,  # Bỏ qua lỗi nếu có
    }

    # URL của tài khoản TikTok
    user_url = f'https://www.tiktok.com/@{user_id}'

    # Tải video với yt-dlp
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([user_url])

if __name__ == "__main__":
    user_id = input("Nhập ID tài khoản TikTok: ")
    download_tiktok_videos(user_id)

