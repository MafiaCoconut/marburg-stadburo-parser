# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.s3_service import S3Service
from application.services.termins_service import TerminsService
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from application.use_cases.set_stadburo_jobs_use_case import SetStadburoJobsUseCase
from domain.entities.job import Job


# from application.scheduler.interfaces.scheduler_interface import SchedulerInterface
# from application.scheduler.usecases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
# from domain.entities.job import Job


class SchedulerService:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 termins_service: TerminsService,
                 s3_service: S3Service,
                 ):
        self.scheduler_interface = scheduler_interface
        self.termins_service = termins_service
        self.s3_service = s3_service
        self.set_stadburo_jobs_use_case = SetStadburoJobsUseCase(
            scheduler_interface=scheduler_interface,
            termins_service=termins_service
        )
        self.set_s3_job_use_case = SetS3JobUseCase(
            scheduler_interface=scheduler_interface,
            s3_service=s3_service
        )

        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(
            scheduler_interface=scheduler_interface,
            set_stadburo_jobs_use_case=self.set_stadburo_jobs_use_case,
            set_s3_job_use_case=self.set_s3_job_use_case
        )

    async def add_job(self, job: Job) -> None:
        await self.scheduler_interface.add_job(job)

    async def add_all_jobs(self, jobs: list[Job]) -> None:
        for job in jobs:
            await self.scheduler_interface.add_job(job)

    async def delete_job(self, job_id: str) -> None:
        await self.scheduler_interface.delete_job(job_id)

    async def set_all_jobs(self) -> None:
        await self.set_all_schedulers_jobs.execute()

    async def get_all_jobs(self):
        return await self.scheduler_interface.get_all_jobs()

