import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image, ImageFilter, ImageOps
import pytesseract
import re
import requests
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

bienSo = "30A12345" 
loaiXe = "1"        

def tra_cuu_phat_nguoi():
    print("bắt đầu kiểm tra: ", bienSo)
    driver = webdriver.Chrome()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    time.sleep(2)
    while True:
        driver.find_element(By.NAME, "BienKiemSoat").clear()
        driver.find_element(By.NAME, "BienKiemSoat").send_keys(bienSo)
        Select(driver.find_element(By.NAME, "LoaiXe")).select_by_value(loaiXe)
        cap_img = driver.find_element(By.ID, "imgCaptcha")
        cap_img.screenshot("captcha.png")
        cap_image = Image.open("captcha.png")
        cap_image = cap_image.convert("L")
        cap_image = ImageOps.autocontrast(cap_image) 
        captcha_text = pytesseract.image_to_string(cap_image, config='--psm 8').strip()
        captcha_text = re.sub(r'[^a-z0-9]', '', captcha_text.lower())[:6]
        print("captcha text:", captcha_text)
        captcha_input = driver.find_element(By.NAME, "txt_captcha")
        captcha_input.clear()
        captcha_input.send_keys(captcha_text)
        driver.find_element(By.CLASS_NAME, "btnTraCuu").click()
        time.sleep(3)
        try:
            result = driver.find_element(By.ID, "bodyPrint123")
            thoi_gian = result.find_element(By.XPATH, "//*[@id='bodyPrint123']/div[4]/div/div").text
            hanh_vi = result.find_element(By.XPATH, "//*[@id='bodyPrint123']/div[6]/div/div").text
            trang_thai = result.find_element(By.XPATH, "//*[@id='bodyPrint123']/div[7]/div/div/span").text
            print("thời gian vi phạm:", thoi_gian)
            print("hành vi vi phạm:", hanh_vi)
            print("trạng thái vi phạm:", trang_thai)
            break
        except Exception as e:
            print("Captcha sai or ko lấy được kết quả, thử lại...")
            driver.refresh() 
            time.sleep(2)
            continue
    driver.quit()

schedule.every().day.at("17:48").do(tra_cuu_phat_nguoi)
schedule.every().day.at("17:04").do(tra_cuu_phat_nguoi)

if __name__ == "__main__":
    print("Đang chạy")
    while True:
        schedule.run_pending()
        time.sleep(30)