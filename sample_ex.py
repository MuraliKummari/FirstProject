import logging
import secrets
from collections import namedtuple

loggers: logging.Logger = logging.getLogger(name="test_sample_ml")

length_of_cookie_size: int = 10
result_nt: namedtuple = namedtuple("result_nt", ["code", "status", "message", "desc"])


def generate_cookie() -> str:
    """
    function for generate random string that is can be used for the cookie id
    :return: string contains alpha numeric with test as prefix
    """
    loggers.debug("in the generate cookie for the testing user sign_in/user sub")
    sample_dict: dict = {
        "name": "pav"
        "city": "Hyd"
    }
    return 'test_' + secrets.token_urlsafe(length_of_cookie_size)
