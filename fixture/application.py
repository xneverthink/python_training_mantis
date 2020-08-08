from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.chrome.options import Options


class Application:

    def __init__(self, browser, base_url):
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
        self.base_url = base_url

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
