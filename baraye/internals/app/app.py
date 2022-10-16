from internals.app import ascii_art
from repositories.example import ExampleRepository
import logging
import logging.config


# ----------------------------------------------------------------
#                             Repository
# ----------------------------------------------------------------

class Repository:
    example: ExampleRepository = ExampleRepository()


# ----------------------------------------------------------------
#                                App
# ----------------------------------------------------------------

class App:
    app_name: str = 'baraye'
    logger: logging.Logger = None
    repository: Repository = Repository()

    def __init__(self):
        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger(self.app_name)
        ascii_art.project_name()


# ----------------------------------------------------------------
#                         public App variable
# ----------------------------------------------------------------

app: App = App()
