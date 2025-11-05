from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import config

# ✅ Create async engine
engine = create_async_engine(
    config.DATABASE_URL,
    echo=True,
)

# ✅ Session factory
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# ✅ Dependency for FastAPI routes
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

# ✅ Initialize DB schema
async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)
