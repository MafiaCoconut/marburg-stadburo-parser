from datetime import datetime, timedelta

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.termins_service import TerminsService
from domain.entities.job import Job


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 termins_service: TerminsService,
                 ):

        self.scheduler_interface = scheduler_interface
        self.termins_service = termins_service

    def execute(self):
        self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                job_id="parser_stadburo_1",
                hour=9,
                minute=0)
        )
        self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                job_id="parser_stadburo_3",
                hour=18,
                minute=0)
        )
        self.scheduler_interface.add_job(
            Job(
                func=self.termins_service.parse_all,
                trigger='cron',
                job_id="parser_stadburo_2",
                hour=13,
                minute=0)
        )

        # self.scheduler_interface.add_job(
        #     Job(
        #         func=self.termins_service.parse_all,
        #         trigger='cron',
        #         job_id="parser_stadburo_1 5",
        #         hour=9,
        #         minute=0)
        # )
        # self.scheduler_interface.add_job(
        #     Job(
        #         func=self.termins_service.parse_all,
        #         trigger='cron',
        #         job_id="parser_stadburo_2 5",
        #         hour=13,
        #         minute=0)
        # )
        # self.scheduler_interface.add_job(
        #     Job(
        #         func=self.termins_service.parse_all,
        #         trigger='cron',
        #         job_id="parser_stadburo_3 5",
        #         hour=18,
        #         minute=0)
        # )

        print(self.scheduler_interface.get_all_jobs())

