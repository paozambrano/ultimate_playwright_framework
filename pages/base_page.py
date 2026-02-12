from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        self.page.click(selector)

    def type_text(self, selector: str, text:str):
        self.page.fill(selector, text)

    def wait_for_text(self, selector: str, text: str):
        expect(self.page.locator(selector)).to_have_text(text)