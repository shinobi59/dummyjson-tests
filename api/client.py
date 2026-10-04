import requests
import logging

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _url(self, path):
        if not path.startswith("/"):
            path = "/" + path
        return f"{self.base_url}{path}"

    def _request(self, method, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        url = self._url(path)

        logger.info(f'{method} {url}')
        if 'json' in kwargs:
            logger.info(f'Body: {kwargs["json"]}')

        response = self.session.request(method, url, **kwargs)

        logger.info(f'- {response.status_code} {url}')
        return response

    def get(self, path, **kwargs):
        return self._request('GET', path, **kwargs)

    def post(self, path, **kwargs):
        return self._request('POST', path, **kwargs)

    def put(self, path, **kwargs):
        return self._request('PUT', path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request('DELETE', path, **kwargs)

    def patch(self, path, **kwargs):
        return self._request('PATCH', path, **kwargs)

    def clear_token(self):
        self.session.headers.pop("Authorization", None)

    def set_token(self, token):
        if not token:
            raise ValueError("Token не может быть пустым")
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def close(self):
        self.session.close()
