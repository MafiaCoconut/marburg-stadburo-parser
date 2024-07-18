# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.termins_service import TerminsService
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from domain.entities.job import Job


# from application.scheduler.interfaces.scheduler_interface import SchedulerInterface
# from application.scheduler.usecases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
# from domain.entities.job import Job


class SchedulerService:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 termins_service: TerminsService):
        self.scheduler_interface = scheduler_interface
        self.termins_service = termins_service

        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(
            scheduler_interface=scheduler_interface,
            termins_service=self.termins_service,
        )

    def add_job(self, job: Job) -> None:
        self.scheduler_interface.add_job(job)

    def add_all_jobs(self, jobs: list[Job]) -> None:
        for job in jobs:
            self.scheduler_interface.add_job(job)
                # func=job.func,
                # trigger=job.trigger,
                # run_date=job.run_date,
                # args=job.args
            # )

    def delete_job(self, job_id: str) -> None:
        self.scheduler_interface.delete_job(job_id)

    def set_all_jobs(self) -> None:
        self.set_all_schedulers_jobs.execute()

    def get_all_jobs(self):
        self.scheduler_interface.get_all_jobs()

