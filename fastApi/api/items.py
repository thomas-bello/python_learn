from fastapi import APIRouter, HTTPException
from api.models import Item

router = APIRouter(prefix="/items", tags=["items"])

# 模拟数据库
items_db = {}


@router.get("/")
def read_items():
    """查询所有条目"""
    return list(items_db.values())


@router.get("/{item_id}")
def read_item(item_id: int):
    """查询单个条目"""
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", status_code=201)
def create_item(item: Item):
    """创建条目"""
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.id] = item.dict()
    return item


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    """更新条目"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    """删除条目"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return
