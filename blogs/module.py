from core import AppModule
from blogs import controllers


class BlogModule(AppModule):

    def __init__(self):
        super().__init__('blogs')
        self.blueprint = controllers.bp
        self.template_folder = 'blogs/templates'
