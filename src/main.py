from fastapi import FastAPI
from contextlib import asynccontextmanager
from infrastructure.config import logs_config
from infrastructure.config.services_config import scheduler_service
from infrastructure.db.base import Base, sync_engine
from infrastructure.web.api import router
from infrastructure.db.models.categories_of_termins_orm import CategoriesOfTerminsOrm
from infrastructure.db.models.termins_orm import TerminsOrm


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler_service.set_all_jobs()
    logs_config.config()
    app.include_router(router)
    yield


app = FastAPI(lifespan=lifespan)


if __name__ == '__main__':
    # Base.metadata.create_all(sync_engine)

    pass
    # obj = GiessenTHMParserInterfaceImpl()
    # obj.parse()

