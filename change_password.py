from playwright.sync_api import sync_playwright
import re


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


email = 'fcguzxkoel@rambler.ru'
old_password = '41196785PFTMv'
new_password = 'abcd12345678'

change_password(email, old_password, new_password)
