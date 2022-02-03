from fastapi import APIRouter

router = APIRouter()


@router.get('/', response_model=dict)
async def get_users():
    return {
        "hello": "USER",
    }
