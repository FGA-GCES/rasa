import rasa

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = rasa.__version__
