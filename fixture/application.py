from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from selenium.webdriver.chrome.options import Options


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = Options()
            options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chromee.exe"
            self.wd = webdriver.Chrome(options=options)
            #self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]

    def open_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20/") and
                len(wd.find_element_by_link_text("Lost your password?")) > 0):
            wd.get(self.base_url) \


    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
