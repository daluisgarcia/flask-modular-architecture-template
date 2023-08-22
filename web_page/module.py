from core import AppModule
from web_page import controllers


class WebPageModule(AppModule):

    def __init__(self):
        self.blueprint = controllers.bp
        self.template_folder = 'web_page/templates'
        self.permission_names = set()
        super().__init__('web_page')
