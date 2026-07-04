from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.dependencies import get_session
from app.repositories.account_repository import AccountRepository
from app.schemas.account import (AccountCreate, AccountListResponse, AccountResponse, AccountStatusUpdate, AccountUpdate
)
from app.services.account_service import AccountService

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)

def get_account_service(
    session: Session = Depends(get_session),
) -> AccountService:
    repository = AccountRepository(session)
    return AccountService(repository)

@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_account(payload: AccountCreate, service: AccountService = Depends(get_account_service)):
    try:
        account = service.create(payload)
        return AccountResponse(
            success=True,
            message="Account created successfully.",
            data=account,
        )
    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(ex),
        )

@router.get(
    "",
    response_model=AccountListResponse,
)
def get_accounts(service: AccountService = Depends(get_account_service)):
    accounts = service.get_all()
    return AccountListResponse(
        success=True,
        message="Accounts retrieved successfully.",
        data=accounts,
    )

@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
def get_account(account_id: UUID, service: AccountService = Depends(get_account_service)):
    try:
        account = service.get_by_id(account_id)
        return AccountResponse(
            success=True,
            message="Account retrieved successfully.",
            data=account,
        )
    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
        )

@router.put(
    "/{account_id}",
    response_model=AccountResponse,
)
def update_account(account_id: UUID, payload: AccountUpdate, service: AccountService = Depends(get_account_service)):
    try:
        account = service.update(
            account_id,
            payload,
        )
        return AccountResponse(
            success=True,
            message="Account updated successfully.",
            data=account,
        )
    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )

@router.patch(
    "/{account_id}/status",
    response_model=AccountResponse,
)
def update_account_status(
    account_id: UUID,
    payload: AccountStatusUpdate,
    service: AccountService = Depends(get_account_service),
):
    account = service.update_status(account_id, payload)

    return AccountResponse(
        success=True,
        message="Account status updated successfully.",
        data=account,
    )
