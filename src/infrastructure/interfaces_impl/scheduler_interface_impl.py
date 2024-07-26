from typing import List

from application.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.job import Job
from infrastructure.config.scheduler_config import scheduler


class SchedulerInterfaceImpl(SchedulerInterface):
    @staticmethod
    def add_job(job: Job) -> None:
        scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            hour=job.hour,
            minute=job.minute,
            args=job.args,
            id=job.job_id,
        )

    @staticmethod
    def delete_job(job_id: str) -> None:
        scheduler.remove_job(job_id)

    @staticmethod
    def get_all_jobs():
        return [job for job in scheduler.get_jobs()]

    @staticmethod
    def start_scheduler():
        scheduler.start()
