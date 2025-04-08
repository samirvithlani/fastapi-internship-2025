from fastapi import APIRouter
from controllers.RazorpayController import create_order, verify_order
from controllers.RazorpayController import CreateOrderRequest, VerifyOrderRequest
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request
from fastapi import Depends


router = APIRouter()
@router.post("/payment/create_order/")
async def create_order_route(request: Request, data: CreateOrderRequest):
    try:
        order = await create_order(data)
        return JSONResponse(status_code=200, content=order)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})

@router.post("/payment/verify_order/")
async def verify_order_route(request: Request, data: VerifyOrderRequest):
    try:
        verification = await verify_order(data)
        return JSONResponse(status_code=200, content=verification)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})    