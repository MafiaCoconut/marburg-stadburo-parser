from application.services.termins_service import TerminsService
from infrastructure.config.interfaces_config import termins_parser_interface
from infrastructure.config.repositories_config import termins_repository

termins_service = TerminsService(
    termins_repository=termins_repository,
    termins_parser_interface=termins_parser_interface
)
