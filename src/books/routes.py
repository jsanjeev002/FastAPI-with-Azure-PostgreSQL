from fastapi import APIRouter, Depends, status, HTTPException   # ✅ Uses Depends for DB session
from sqlalchemy.ext.asyncio import AsyncSession                 # ✅ Async DB session
from typing import List
from src.db.main import get_session                             # ✅ Dependency that opens DB connection
from src.books.models import Book                               # ✅ ORM model (mapped to DB table)
from src.books.schema import BookCreateModel, BookUpdateModel   # ✅ Pydantic models for validation
from sqlmodel import select                                     # ✅ SQLModel query builder
import uuid

book_router = APIRouter()

@book_router.get("/", response_model=List[Book])                # ✅ Returns all DB records
async def get_all_books(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book))                   # ✅ Executes SQL SELECT
    return result.all()


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = Book(**book_data.dict())                         # ✅ ORM instance created
    session.add(new_book)                                       # ✅ Adds record to DB session
    await session.commit()                                      # ✅ Saves to DB
    await session.refresh(new_book)                             # ✅ Refreshes object with DB values (like id)
    return new_book                                             # ✅ Returns full DB record


@book_router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not available")
    
    return book


@book_router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: str, book_update_model: BookUpdateModel, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    update_data = book_update_model.dict(exclude_unset=True)  # only update fields that are provided
    for key, value in update_data.items():
        setattr(book, key, value)

    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    await session.delete(book)
    await session.commit()
    return {}


