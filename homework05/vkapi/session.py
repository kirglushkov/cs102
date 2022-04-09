import typing as tp

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry as Retri


class Session:
    """
    Сессия.

    :param base_url: Базовый адрес, на который будут выполняться запросы.
    :param timeout: Максимальное время ожидания ответа от сервера.
    :param max_retries: Максимальное число повторных запросов.
    :param backoff_factor: Коэффициент экспоненциального нарастания задержки.
    """

    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
    ) -> None:
        self.session = requests.Session()
        self.base_url = base_url
        self.timeout = timeout
        self.retry = Retri(
            total=max_retries,
            backoff_factor=backoff_factor,
            allowed_methods=["GET", "POST"],
            status_forcelist=list(range(400, 666)),
        )
        self.adapter = HTTPAdapter(max_retries=self.retry)
        self.session.mount(base_url, self.adapter)

    def timeout_kwarg(self, kwargs):
        return kwargs["timeout"] if "timeout" in kwargs else self.timeout

    def get(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
        kwargs["timeout"] = self.timeout_kwarg(kwargs)
        return self.session.get(self.base_url + url, *args, **kwargs)

    def post(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
        kwargs["timeout"] = self.timeout_kwarg(kwargs)
        return self.session.post(self.base_url + url, *args, **kwargs)
