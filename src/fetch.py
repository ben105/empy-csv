import requests
from auth import Auth


def fetch(auth: Auth, method: str, url: str, **kwargs) -> requests.Response:
    """Retrieves resources from Emporia endpoints."""
    headers = kwargs.get("headers")
    if headers is None:
        headers = {}
    else:
        headers = dict(headers)
    headers["authtoken"] = auth.get_id_token()
    return requests.request(method, url, **kwargs, headers=headers)
