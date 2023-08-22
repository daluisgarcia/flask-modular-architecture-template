from core import AppModule
from blogs import controllers


class BlogModule(AppModule):

    def __init__(self):
        self.blueprint = controllers.bp
        self.permission_names = set()
        self.template_folder = 'blogs/templates'
        super().__init__('blogs')
