from fastapi import FastAPI
from routes.RoleRoutes import router as role_router
from routes.UserRoutes import router as user_router
from routes.DepartmentRoutes import router as department_router
from routes.EmployeeRoutes import router as employee_router
from routes.StateRoutes import router as state_router
from routes.CityRoutes import router as city_router
from routes.CategoryRoutes import router as category_router
from routes.SubCategoryRoutes import router as sub_category_router
from routes.ProductRoutes import router as product_router
#import cors middleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(role_router)
app.include_router(user_router)
app.include_router(department_router)
app.include_router(employee_router)
app.include_router(state_router)
app.include_router(city_router)
app.include_router(category_router)
app.include_router(sub_category_router)
app.include_router(product_router)


#routes