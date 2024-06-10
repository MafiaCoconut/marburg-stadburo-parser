from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl
from infrastructure.config.termins_service_config import termins_service


scheduler_interface = SchedulerInterfaceImpl(
    termins_service=termins_service
)
