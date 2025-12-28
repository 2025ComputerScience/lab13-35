import pytesseract
from PIL import Image
import os

# 設定圖片路徑
img_path = "christmas.png" 

if not os.path.exists(img_path):
    print(f"錯誤：找不到圖片 {img_path}，請先上傳圖片到 Colab 左側檔案區！")
else:
    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(
            image, 
            lang='chi_tra+eng', #同時載入中,英文庫
            config='--psm 6'
        )
        
        print("OCR 辨識結果 (中英混合):")
        print("-" * 40)
        print(text)
        print("-" * 40)

    except pytesseract.TesseractError as e:
        print("Tesseract 執行錯誤。")
        print(f"詳細訊息: {e}")