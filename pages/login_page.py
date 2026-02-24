from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.email_input = "#email"
        self.pass_input = "#pass"
        self.login_button = "#send2"
        self.header_msg = ".panel .welcome"

    def login(self, email, password):
        self.type_text(self.email_input, email)
        self.type_text(self.pass_input, password)
        self.click_element(self.login_button)

    def verify_success(self):
        self.is_visible(self.header_msg)