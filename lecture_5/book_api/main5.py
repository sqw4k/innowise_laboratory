from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.exc import IntegrityError

from pydantic import BaseModel, ConfigDict
from typing import Optional, List

app = FastAPI(title="Book API")

# Database setup
engine = create_engine('sqlite:///book.db', connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)


Base.metadata.create_all(engine)


# Pydantic Models
class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoints
@app.get("/")
def root():
    return {"message": "Intro to Book API"}


@app.get("/books/", response_model=List[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    try:
        books = db.query(Book).all()
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/books/", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    try:
        new_book = Book(**book.model_dump())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    try:
        book = db.query(Book).get(book_id)

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        db.delete(book)
        db.commit()

        return {"success": True, "message": "Book deleted"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_update: BookCreate, db: Session = Depends(get_db)):
    try:
        book = db.query(Book).get(book_id)

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        book.title = book_update.title
        book.author = book_update.author
        book.year = book_update.year

        db.commit()
        db.refresh(book)

        return book
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/books/search/", response_model=List[BookResponse])
def search_book(
        title: Optional[str] = Query(None, description="Search by book title"),
        author: Optional[str] = Query(None, description="Search by author name"),
        year: Optional[int] = Query(None, description="Search by publication year"),
        db: Session = Depends(get_db)
):
    try:
        query = db.query(Book)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))
        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))
        if year:
            query = query.filter(Book.year == year)

        books = query.all()
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
