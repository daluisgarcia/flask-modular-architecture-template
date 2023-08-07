
from core import AppModule
from landing_page import controllers


class LandingPageModule(AppModule):

    def __init__(self):
        super().__init__('landing')
        self.blueprint = controllers.bp
        self.template_folder = 'landing/templates'
