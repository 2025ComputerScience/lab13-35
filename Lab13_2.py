import pytesseract
from PIL import Image
import cv2 

#設定圖片路徑 
img_path = "thrity_five.jpg" 

#開啟圖片 
try:
    image = Image.open(img_path)
except FileNotFoundError:
    print(f"錯誤：找不到圖片 {img_path}，請確認檔名是否正確。")
    exit()

#執行 OCR 辨識
try:
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 10')
    
    print("OCR 辨識結果:")
    print("-" * 40)
    print(text)
    print("-" * 40)

except pytesseract.TesseractError as e:
    print("Tesseract 錯誤：可能缺少語言包或 Tesseract 未安裝。")
    print(f"系統訊息: {e}")