from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker


engine = create_async_engine(
    url=f"sqlite+aiosqlite:///database.db",
    pool_size=30,
    max_overflow=10,
    pool_recycle=3600,
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base: DeclarativeMeta = declarative_base()

