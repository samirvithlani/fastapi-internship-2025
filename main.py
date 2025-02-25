from fastapi import FastAPI
from routes.RoleRoutes import router as role_router
#from routes.UserRoutes import router as

app = FastAPI()

app.include_router(role_router)


#routes