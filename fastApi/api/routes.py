from fastapi import APIRouter
from .items import router as items_router

# 主路由器，用于注册所有API路由
api_router = APIRouter()

# 注册各个模块的路由
api_router.include_router(items_router)

# 如果需要添加新的路由模块，在这里导入并注册
# 例如：
# from .users import router as users_router
# api_router.include_router(users_router)
