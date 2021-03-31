import logging
from collections import namedtuple

# from flask import jsonify

loggers: logging.Logger = logging.getLogger(name="sample_deep_code_ex")
result_nt: namedtuple = namedtuple("result_nt", ["code", "status", "message", "desc"])


class Result:
    """class representing the api responses with jsonify"""
    def __init__(self, code: int = 500, status: str = "FAILED",
                 message: str = "", desc: str = "", extra_fields: dict = {}) -> None:

        """
        Base Result class for API responses.
        code - numeric status code, smilar to HTTP status code
        status - short status code
        message - descriptive message.
        """
        self.code: int = code
        self.status: str = status
        self.message: str = message
        self.desc: str = desc
        self.extra_fields: dict = extra_fields

    def http_response(self) -> dict:
        """method for the returning json resp to the object
        :return dict containing the API responses
        """
        try:
            loggers.debug("In the http_response for parsing the data")
            result: dict = result_nt(self.code, self.status, self.message, self.desc)._asdict()
            if self.extra_fields:
                if isinstance(self.extra_fields, dict):
                    result.update(self.extra_fields)
                else:
                    result["related_info"] = self.extra_fields
            loggers.info("the final data to the user is: %s", str(result))
            json_results: dict = result
            return json_results
        except NameError as err:
            loggers.error("named error while returning http jso response is %s", str(err))
        except ValueError as err:
            loggers.error("named error while returning http jso response is %s", str(err))
        except Exception as err:
            loggers.error("Exception while parsing results data is %s", str(err))

        err_results: dict = result_nt(self.code, self.status, self.message, self.desc)._asdict()
        return err_results


class ServerErrorResult(Result):
    """
    class inheriting the Result class for instantiating http server error results
    """
    def __init__(self, errors: dict = {}):
        """
        function for instantiating the Result class with it
        :param errors: it will shown as the extra result to the result objects
        """

        super(ServerErrorResult, self).__init__(500, "FAILED", "InternalServerError",
                                                extra_fields=errors
                                                )


if __name__ == '__main__':
    result_obj: Result = Result()
    results: dict = result_obj.http_response()
    print(results)
