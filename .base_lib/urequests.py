class Request:
    def __init__(self) -> None:
        # Get the response body status code
        self.status_code = ""
        # Get the response body Reason-Phrase
        self.reason = ""
        # Get the native response body
        self.content = ""
        # Get response body string
        self.text = ""
        # Get response body JSON
        self.json = ""


def request(method, url, json, headers) -> Request: ...  # noqa
