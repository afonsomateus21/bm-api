from fastapi import APIRouter, Request, HTTPException, Depends

appointments_router = APIRouter(prefix="/auth", tags=["User"])