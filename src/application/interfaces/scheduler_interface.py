from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class SchedulerInterface(ABC):
    @staticmethod
    @abstractmethod
    def add_job(job) -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete_job(job_id: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_all_jobs():
        pass



