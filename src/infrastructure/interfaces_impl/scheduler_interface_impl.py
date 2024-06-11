from typing import List

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.termins_service import TerminsService
from domain.entities.job import Job
from infrastructure.config.scheduler_config import scheduler


class SchedulerInterfaceImpl(SchedulerInterface):
    def __init__(self, termins_service: TerminsService):
        self.termins_service = termins_service

    @staticmethod
    def add_job(job: Job) -> None:
        scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            run_date=job.run_date,
            args=job.args
        )

    def set_all_jobs(self):
        scheduler.add_job(
            self.termins_service.parse_all,
            trigger='cron',
            id="parser_stadburo_1",
            hour=9, minute=0
        )

        scheduler.add_job(
            self.termins_service.parse_all,
            trigger='cron',
            id="parser_stadburo_2",
            hour=13, minute=0
        )

        scheduler.add_job(
            self.termins_service.parse_all,
            trigger='cron',
            id="parser_stadburo_3",
            hour=18, minute=0
        )

