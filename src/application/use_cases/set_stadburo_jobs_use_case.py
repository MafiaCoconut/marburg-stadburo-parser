from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.termins_service import TerminsService
from domain.entities.job import Job
from infrastructure.config.logs_config import log_decorator


class SetStadburoJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 termins_service: TerminsService
                 ):
        self.scheduler_interface = scheduler_interface
        self.termins_service = termins_service

    @log_decorator(print_args=False, print_kwargs=False)
    async def execute(self):
        await self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                id="parser_stadburo_1",
                hour=9,
                minute=0)
        )
        await self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                id="parser_stadburo_2",
                hour=13,
                minute=0)
        )
        await self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                id="parser_stadburo_3",
                hour=18,
                minute=0)
        )
