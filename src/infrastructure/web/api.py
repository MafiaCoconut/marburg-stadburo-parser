from fastapi import Depends, APIRouter, Path, Response, status
from sqlalchemy.orm import Session

from application.services.scheduler_service import SchedulerService
from infrastructure.config.logs_config import log_api_decorator
from infrastructure.config.services_config import termins_service, get_scheduler_service

router = APIRouter()


@router.post("/category_of_termins/startParsersAll")
@log_api_decorator
async def start_parser_all(response: Response):
    return await termins_service.parse_all()


@router.post("/category_of_termins{category_of_termins}/startParser")
@log_api_decorator
async def start_parser(
        category_of_termin_id: int, response: Response, get_result: bool = False,
):
    if get_result:
        return await termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))
    else:
        await termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))


@router.get("/category_of_termins{category_of_termins_id}/getData")
@log_api_decorator
async def get_category_of_termins_data(category_of_termins_id: int, response: Response):
    """
    Функция возвращает по api данные о категории и текущих терминах
    :param category_of_termins_id: ID категории в базе данных
    :return: {'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
    """
    return await termins_service.get_category_of_termins_data(category_of_termins_id=category_of_termins_id)


@router.put('category_of_termins{category_of_termins}/deactivate')
@log_api_decorator
async def deactivate_category_of_termins(category_of_termin_id: int, response: Response):
    """
    Функция деактивирует парсинг категории
    :param category_of_termin_id: ID категории в базе данных
    """
    pass


@router.put('category_of_termins{category_of_termins}/reactivate')
@log_api_decorator
async def reactivate_category_of_termins(category_of_termin_id: int, response: Response):
    """
    Функция деактивирует парсинг категории
    :param category_of_termin_id: ID категории в базе данных
    """
    pass


@router.get('/jobs/getAll')
@log_api_decorator
async def get_all_jobs(
        response: Response,
        scheduler_service: SchedulerService = Depends(get_scheduler_service)
):
    return {'text': await scheduler_service.get_all_jobs()}

