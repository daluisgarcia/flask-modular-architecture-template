# Flask Modular Architecture Template
This is a template for a Flask project using a modular architecture. This project facilitates the creation of a Flask 
project with a modular architecture, allowing the creation of new modules by extending a class and adding it to a set. 
This template has some flask extension installed, such as: `flask_login`, `flask_principal` and `flask_sqlalchemy`; 
any other extension can be installed by being added to the `core/extensions.py` file, inside the `install_extensions` 
function. 

# Project structure
- `admin/`: An module example for an administration panel. **CAN BE EDITED OR DELETED**
- `blogs/`: An example module of the blogs tutorial project from the old *Flask Quickstart Guide*. **CAN BE EDITED OR DELETED**
- `core/`: Core module of the application. This module contains the core code of the project and orchestrates the 
features of the template. This module contains the base templates and the static folder, also the authentication 
and permissions features. **BE CAREFUL WHEN EDITING THE CODE INSIDE THIS FOLDER, THIS ACTION CAN BREAK THE PROJECT**
- `landing_page/`: An example module for the landing page. This folder contains the minimum code to create a module. 
**CAN BE EDITED OR DELETED**
- `app.py`: Main file of the application. This file is the one that must be executed to run the application. **DO NOT MODIFY**
- `modules.py`: File that contains a set with the modules of the application. Only modify to add new modules to the set.

# Project installation
To install the project package, run the following command `pip install -r requirements.txt`

# Module creation
To create a new module, you only need to create a new folder with a `module.py` file inside it. This file must contain a
class extending the `core.AppModule` class and implementing the `__init__` method defining the `self.bluprint` attribute 
with the blueprint of the module and the `self.template_folder` with the path to the module's templates folder. Also, you 
need to call the super `__init__` method with the module name as the parameter (You can see an example in `admin/module.py` file). 

To subscribe the module to the application, you need to import the module class in the `modules.py` file and add it to the
`APP_MODULES` set in it. This will allow the application to load the module when it starts.

# Project usage
## Setting environment variables
Before running the project, you must create a `.env` file in the root directory of the project as a copy of `.env.example`. 

## Running the project
To run the project you can use either the command `python app.py`

# Contributing
To contribute to this project, you can fork the repository and create a pull request with your changes. Also, you can
open an issue with your suggestion or bug report. I will be happy to review your contributions.
