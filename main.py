from fastapi import FastAPI
from routes.RoleRoutes import router as role_router
from routes.UserRoutes import router as user_router
from routes.DepartmentRoutes import router as department_router
from routes.EmployeeRoutes import router as employee_router

app = FastAPI()

app.include_router(role_router)
app.include_router(user_router)
app.include_router(department_router)
app.include_router(employee_router)


#routes