from dataclasses import dataclass
from typing import Optional

from .base import BaseCaptcha, BaseCaptchaSolution


@dataclass
class YandexSC(BaseCaptcha):
    """ Yandex SmartCaptcha """

    site_key: str
    page_url: str
    api_server: Optional[str] = None  # если когда-нибудь надо будет указать свой сервер API

    def get_optional_data(self, **kwargs):
        """
        Возвращает дополнительные параметры, если они есть.
        Можно расширить, если нужно поддерживать больше аргументов.
        """
        return {}
    

@dataclass
class YandexSCSolution(BaseCaptchaSolution):
    """ Yandex SmartCaptcha solution """

    text: str  # токен, который нужно отправлять на сайт
