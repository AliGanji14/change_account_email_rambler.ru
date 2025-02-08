from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright
import re

load_dotenv()


def change_password(email, old_password, new_password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ورود به اکانت
        page.goto('https://email.rambler.ru/')
        page.fill('input[id=login]', email)
        page.fill('input[id=password]', old_password)
        page.get_by_role("button", name="Войти").click()

        # رفتن به تنظمیات اکانت
        page.get_by_role("button", name="Подтвердить позже").click()
        page.locator("div").filter(has_text=re.compile(
            r"^Пароль и безопасность профиля$")).click()
        page.get_by_label("Изменить пароль").click()

        # وارد کردن پسورد جدید
        page.fill('input[id=password]', new_password)
        page.fill('input[id=newPassword]', new_password)
        page.pause()


email = os.getenv('EMAIL')
old_password = os.getenv('OLD_PASSWORD')
new_password = os.getenv('NEW_PASSWORD')
change_password(email, old_password, new_password)
