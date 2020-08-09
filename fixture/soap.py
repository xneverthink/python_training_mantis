from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        projects = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            for element in client.service.mc_projects_get_user_accessible(username, password):
                id = str(element.id)
                name = element.name
                description = element.description
                status = element.status.name
                view_state = element.view_state.name
                projects.append(Project(id=id, name=name, description=description, view_state=view_state,
                                        status=status))
            return projects
        except WebFault:
            return False
