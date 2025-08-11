# 这是一个示例文件，展示如何创建新的路由模块
# 使用时请删除此注释，并实现具体的路由逻辑

from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["example"])


@router.get("/")
def read_examples():
    """示例端点：获取所有示例"""
    return {"message": "This is an example endpoint"}


@router.get("/{example_id}")
def read_example(example_id: int):
    """示例端点：获取单个示例"""
    return {"example_id": example_id, "message": "This is a specific example"}


# 要启用此路由，请在 api/routes.py 中添加：
# from .example import router as example_router
# api_router.include_router(example_router)
