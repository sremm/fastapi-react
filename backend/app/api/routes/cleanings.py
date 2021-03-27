from typing import List

from app.api.dependencies.database import get_repository
from app.db.repositories.cleanings import CleaningsRepository
from app.models.cleaning import CleaningCreate, CleaningInDB, CleaningPublic
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

router = APIRouter()


@router.get(
    "/",
    response_model=List[CleaningInDB],
    name="cleanings:get-all-cleanings",
    status_code=HTTP_200_OK,
)
async def get_all_cleanings(
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> List[CleaningInDB]:
    return await cleanings_repo.get_all_cleanings()


@router.get(
    "/{id}/",
    response_model=CleaningInDB,
    name="cleanings:get-cleaning-by-id",
    status_code=HTTP_200_OK,
)
async def get_cleaning_by_id(
    id: int,
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    cleaning = await cleanings_repo.get_cleaning_by_id(id=id)
    if not cleaning:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with that id."
        )
    return cleaning


@router.post(
    "/",
    response_model=CleaningPublic,
    name="cleanings:create-cleaning",
    status_code=HTTP_201_CREATED,
)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return created_cleaning
