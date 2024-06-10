from fastapi import FastAPI

from infrastructure.config import logs_config
from infrastructure.db.base import Base, sync_engine
from infrastructure.web.api import router
from infrastructure.db.models.categories_of_termins_orm import CategoriesOfTermins
from infrastructure.db.models.termins_orm import TerminsOrm

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    # start_scheduler_service.execute()
    logs_config.config()
    # TODO настроить scheduler
    # TODO красивый вывод текст
    # TODO оставшиеся 3 парсера доделать
    # TODO доделать api




if __name__ == '__main__':
    # Base.metadata.create_all(sync_engine)

    pass
    # obj = GiessenTHMParserInterfaceImpl()
    # obj.parse()

