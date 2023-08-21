from core import AppModule

from blogs import BlogModule
from admin import AdminModule
from web_page import WebPageModule


APP_MODULES: set[AppModule] = {
    BlogModule(),
    AdminModule(),
    WebPageModule()
}
