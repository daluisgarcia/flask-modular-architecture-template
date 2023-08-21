
from core import AppModule
from web_page import controllers


class WebPageModule(AppModule):

    def __init__(self):
        super().__init__('web_page')
        self.blueprint = controllers.bp
        self.template_folder = 'web_page/templates'
