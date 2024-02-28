from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from schemas.checks import (
    CheckCreateSchema,
    CheckSchema,
    CheckListPaginatedResponseSchema,
    CheckListSchema,
    CheckSchemaOutput,
)
from schemas.pagination import PaginationQueryParamsSchema
from schemas.exceptions import BadRequestSchema

from services.checks import check_service

from filters.checks import CheckFilter

from models.users import User

from utils.auth import get_current_user
from utils.filters import FilterSet
from utils.paginatior import Paginator, get_paginated_response


router = APIRouter(prefix="/checks", tags=["checks"])

templates = Jinja2Templates(directory="templates")


@router.post(
    "",
    responses={status.HTTP_400_BAD_REQUEST: {'model': BadRequestSchema}},
)
async def create_check(
    check: CheckCreateSchema,
    current_user: User = Depends(get_current_user),
) -> CheckSchema:
    check = check.model_dump()
    check["created_by"] = current_user
    check = await check_service.create(**check)
    return await CheckSchema.from_tortoise_orm(
        await check_service.get(id=check.id)
    )  # not use check instance in previous line because not corrent show decimal fields, i think problem with tortoise-orm lib


@router.get(
    "",
    responses={status.HTTP_400_BAD_REQUEST: {'model': BadRequestSchema}},
)
async def list_checks(
    pagination_params: PaginationQueryParamsSchema = Depends(),
    filter_params: CheckFilter = Depends(CheckFilter),
    current_user: User = Depends(get_current_user),
) -> CheckListPaginatedResponseSchema:
    queryset = FilterSet(
        check_service.filter_by_created_by(current_user).prefetch_related("products"),
        filter_params,
    ).apply()
    paginated_queryset = Paginator(queryset, pagination_params).paginate()
    return get_paginated_response(
        await CheckListSchema.from_queryset(paginated_queryset), **pagination_params.model_dump()
    )


@router.get(
    "/{check_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {'model': BadRequestSchema},
        status.HTTP_400_BAD_REQUEST: {'model': BadRequestSchema},
    },
)
async def get_check(check_id: int, current_user: User = Depends(get_current_user)) -> CheckSchema:
    return await CheckSchema.from_tortoise_orm(await check_service.get(id=check_id, created_by=current_user))


@router.get(
    "/{check_id}/output",
    responses={status.HTTP_404_NOT_FOUND: {'model': BadRequestSchema}},
    description="For correct show - open new tab in browser, copy url from this view and replace check_id for show check (Check representations as HTML)",
)
async def get_check_output(request: Request, check_id: int) -> HTMLResponse:
    check_data = await CheckSchemaOutput.from_tortoise_orm(await check_service.get(id=check_id))
    return templates.TemplateResponse(request=request, name="check.html", context={"check_data": check_data})
