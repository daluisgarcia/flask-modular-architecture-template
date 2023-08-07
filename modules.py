from core import AppModule

from blogs import BlogModule
from admin import AdminModule
from landing_page import LandingPageModule


APP_MODULES: set[AppModule] = {
    BlogModule(),
    AdminModule(),
    LandingPageModule()
}
