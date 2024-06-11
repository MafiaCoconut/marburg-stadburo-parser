from infrastructure.config.services_config import termins_service
from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl


scheduler_interface = SchedulerInterfaceImpl(
    termins_service=termins_service
)
