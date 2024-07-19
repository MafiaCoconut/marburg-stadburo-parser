from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from infrastructure.config.services_config import termins_service

router = APIRouter()


@router.get("/parser/all")
def start_parser_all():
    return termins_service.parse_all()


@router.get("/parser/{category_of_termin_id}")
def start_parser(category_of_termin_id: str, get_result: bool = False):
    if get_result:
        return termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))
    else:
        termins_service.parse_termins_category(termin_category_id=int(category_of_termin_id))


@router.get("/category_of_termins/{category_of_termins}")
def get_text_category_of_termins(category_of_termins: str, locale: str):
    return termins_service.get_text_category_of_termins(category_of_termins=int(category_of_termins), locale=locale)


