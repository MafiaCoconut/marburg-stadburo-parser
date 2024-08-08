from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from infrastructure.config.services_config import termins_service

router = APIRouter()


@router.post("/category_of_termins/startParsersAll")
async def start_parser_all():
    return await termins_service.parse_all()


@router.post("/category_of_termins{category_of_termins}/startParser")
async def start_parser(category_of_termin_id: int, get_result: bool = False):
    if get_result:
        return await termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))
    else:
        await termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))


@router.get("/category_of_termins{category_of_termins_id}/getData")
async def get_category_of_termins_data(category_of_termins_id: int):
    """
    Функция возвращает по api данные о категории и текущих терминах
    :param category_of_termins_id: ID категории в базе данных
    :return: {'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
    """
    return await termins_service.get_category_of_termins_data(category_of_termins_id=category_of_termins_id)


@router.put('category_of_termins{category_of_termins}/deactivate')
async def deactivate_category_of_termins(category_of_termin_id: int):
    """
    Функция деактивирует парсинг категории
    :param category_of_termin_id: ID категории в базе данных
    """
    pass


@router.put('category_of_termins{category_of_termins}/reactivate')
async def reactivate_category_of_termins(category_of_termin_id: int):
    """
    Функция деактивирует парсинг категории
    :param category_of_termin_id: ID категории в базе данных
    """
    pass


