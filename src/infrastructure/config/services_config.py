from application.services.s3_service import S3Service
from application.services.scheduler_service import SchedulerService
from application.services.termins_service import TerminsService
from infrastructure.config.providers_config import categories_of_termins_provider, repositories_provider
from infrastructure.config.repositories_config import get_termins_repository, get_category_of_termins_repository
from infrastructure.config.s3_config import s3client
from infrastructure.config.scheduler_interfaces_config import scheduler_interface
from infrastructure.config.translation_service_config import translation_service

termins_service = TerminsService(
    repositories_provider=repositories_provider,
    category_of_termins_repository=get_category_of_termins_repository(),
    categories_of_termins_provider=categories_of_termins_provider,
    translation_service=translation_service
)

s3_service = S3Service(
    s3client=s3client
)


def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=scheduler_interface,
        termins_service=termins_service,
        s3_service=s3_service
    )
