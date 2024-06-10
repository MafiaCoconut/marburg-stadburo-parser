from application.services.set_all_schedulers_service import StartSchedulersService
from infrastructure.config.scheduler_interfaces_config import scheduler_interface

start_scheduler_service = StartSchedulersService(scheduler_interface=scheduler_interface)