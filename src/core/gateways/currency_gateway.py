from ast import literal_eval
from typing import Optional, Dict
import requests
from requests.structures import CaseInsensitiveDict
from requests import Response


class CurrencyAPI:
    def __init__(self, api_key: Optional[str] = None):
        self._base_url = 'https://api.freecurrencyapi.com/v1/'
        self._api_key = api_key if api_key else 'fca_live_6HL9wcI8UVs02OCYGuYXZmb6lOu1wnr8atvMA8JS'
        self._headers = CaseInsensitiveDict()
        self._headers['apikey'] = self._api_key

    def _request_with_retry(self, method: str, url: str, params: Optional[dict] = None, data: Optional[dict] = None,
                            json_data: Optional[dict] = None, requests_count: int = 3) -> Response:
        for attempt in range(requests_count):
            response = requests.request(method=method, url=url, headers=self._headers, params=params, data=data, json=json_data)

            if response.status_code == 200:
                break

        return response

    def _update_headers(self, headers: Dict[str, str]):
        self._headers.update(headers)

    def get_account_status(self):
        response = self._request_with_retry(method='GET', url=self._base_url + 'status')

        return response

    def get_currencies(self, currencies: str):
        request_params = {
            'currencies': currencies
        }
        response = self._request_with_retry(method='GET', url=self._base_url + 'currencies', params=request_params)

        return response

    def get_latest_currency(self, base_currency: str, currencies: str):
        request_params = {
            'base_currency': base_currency,
            'currencies': currencies
        }
        response = self._request_with_retry(method='GET', url=self._base_url + 'latest', params=request_params)

        return response

    def get_currency_by_date(self, currency_date: str, base_currency: str, currencies: str):
        request_params = {
            'date': currency_date,
            'base_currency': base_currency,
            'currencies': currencies
        }
        response = self._request_with_retry(method='GET', url=self._base_url + 'latest', params=request_params)

        return response
