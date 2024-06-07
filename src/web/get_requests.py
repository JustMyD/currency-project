from ast import literal_eval
from typing import Optional

from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from web.models import ExternalInfo
from core.gateways.currency_gateway import CurrencyAPI

get_router = APIRouter(prefix='/currency/get')


@get_router.get('/status')
async def get_account_status(meta_info: ExternalInfo):
    """
    Получение справки о текущем статусе аккаунта
    """
    currency_api = CurrencyAPI()
    response = currency_api.get_account_status()

    result = dict()
    result['content'] = literal_eval(response.content.decode(response.encoding))

    return JSONResponse(result, response.status_code)


@get_router.get('/currencies')
async def get_currencies(meta_info: ExternalInfo, currencies: Optional[str] = Body('', embed=True)):
    """
    Получение информации по указанному списку валют.
    В случае если список валют не передан - возвращается информация по всем доступным валютам.
    :param meta_info:  Инфо запроса
    :param currencies: Список валют через запятую
    """
    currency_api = CurrencyAPI()
    response = currency_api.get_currencies(currencies=currencies)

    result = dict()
    result['content'] = literal_eval(response.content.decode(response.encoding))

    return JSONResponse(result, response.status_code)


@get_router.get('/latest')
async def get_latest_exchange_rate(
        meta_info: ExternalInfo,
        base_currency: Optional[str] = Body('', embed=True),
        currencies: Optional[str] = Body('', embed=True)
):
    """
    Получение курсов валют отностельно базовой валюты.
    В случае если список валют не указан - возвращается информация по всем доступным валютам.
    В случае если не указана базовая валюта - за базу берется `USD`.
    :param meta_info:     Инфо запроса
    :param base_currency: Базовая валюта
    :param currencies:    Список валют по которым нужен курс
    """
    currency_api = CurrencyAPI()
    response = currency_api.get_latest_currency(base_currency=base_currency, currencies=currencies)

    result = dict()
    result['content'] = literal_eval(response.content.decode(response.encoding))

    return JSONResponse(result, response.status_code)


@get_router.get('/historical')
async def get_historical_exchange_rates(
        meta_info: ExternalInfo,
        date: str = Body(embed=True),
        base_currency: Optional[str] = Body('', embed=True),
        currencies: Optional[str] = Body('', embed=True)
):
    """
    Получение курсов валют относительно базовой валюты за указанный период.
    В случае если список валют не указан - возвращается информация по всем доступным валютам.
    В случае если не указана базовая валюта - за базу берется `USD`.
    Бесплатная версия поддерживает данные курсов валют вплоть до 1999 года, при необходимости получить данные ранее 1999
    года необходимо обновить аккаунт.
    :param meta_info:     Инфо запроса
    :param date:          Дата начала периода
    :param base_currency: Базовая валюта
    :param currencies:    Список валют по которым нужен курс
    """
    currency_api = CurrencyAPI()
    response = currency_api.get_currency_by_date(currency_date=date, base_currency=base_currency, currencies=currencies)

    result = dict()
    result['content'] = literal_eval(response.content.decode(response.encoding))

    return JSONResponse(result, response.status_code)
