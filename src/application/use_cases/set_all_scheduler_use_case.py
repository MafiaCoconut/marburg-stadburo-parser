from datetime import datetime, timedelta

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.s3_service import S3Service
from application.services.termins_service import TerminsService
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from application.use_cases.set_stadburo_jobs_use_case import SetStadburoJobsUseCase
from domain.entities.job import Job
from infrastructure.config.logs_config import log_decorator


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 set_stadburo_jobs_use_case: SetStadburoJobsUseCase,
                 set_s3_job_use_case: SetS3JobUseCase
                 ):
        self.scheduler_interface = scheduler_interface
        self.set_stadburo_jobs_use_case = set_stadburo_jobs_use_case
        self.set_s3_job_use_case = set_s3_job_use_case

    @log_decorator(print_args=False, print_kwargs=False)
    async def execute(self):
        await self.set_stadburo_jobs()
        await self.set_s3_jobs()

        await self.scheduler_interface.start()

    @log_decorator(print_args=False, print_kwargs=False)
    async def set_stadburo_jobs(self):
        await self.set_stadburo_jobs_use_case.execute()

    @log_decorator(print_args=False, print_kwargs=False)
    async def set_s3_jobs(self):
        await self.set_s3_job_use_case.execute()




