from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_create_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_create_page.php")

    def open_project_manage_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        self.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_project_create_page()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_manage_page()
            self.project_cache = []
            table = wd.find_elements_by_css_selector('table[class="width100"]')[1]
            rows = table.find_elements_by_css_selector('tr[class^="row-"]')[1:]
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                view_state = cells[3].text
                description = cells[4].text
                name_text = wd.find_element_by_link_text(name).get_attribute("href")
                id = name_text.partition("project_id=")[2]
                self.project_cache.append(Project(name=name, status=status, view_state=view_state,
                                                  description=description, id=id))
        return list(self.project_cache)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_manage_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None
