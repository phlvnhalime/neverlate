import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# ── CONCEPT: DATABASE_URL ────────────────────────────────────────────────────
#  We build the URL from individual pieces instead of one string.
#  This safely handles special characters in passwords (like @ # %)
#  which would break a plain string URL like postgresql://user:p@ss@host
# ────────────────────────────────────────────────────────────────────────────
DATABASE_URL = URL.create(
    drivername="postgresql",
    username=os.getenv("DB_USER", "neverlate"),
    password=os.getenv("DB_PASSWORD", "neverlate"),
    host=os.getenv("DB_HOST", "db"),
    port=5432,
    database=os.getenv("DB_NAME", "neverlate"),
)

# ── CONCEPT: ENGINE ──────────────────────────────────────────────────────────
#  The engine is the actual connection to PostgreSQL.
#  Think of it as the phone line between Python and the database.
# ────────────────────────────────────────────────────────────────────────────
engine = create_engine(DATABASE_URL)

# ── CONCEPT: SESSION ─────────────────────────────────────────────────────────
#  A session is one conversation with the database.
#  Each API request gets its own session, uses it, then closes it.
#  autocommit=False → we manually confirm (commit) changes
#  autoflush=False  → we control when data is sent to the DB
# ────────────────────────────────────────────────────────────────────────────
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ── CONCEPT: BASE ────────────────────────────────────────────────────────────
#  All your database table models will inherit from this Base class.
#  SQLAlchemy uses it to know which Python classes are database tables.
# ────────────────────────────────────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ── CONCEPT: get_db (dependency) ─────────────────────────────────────────────
#  This function gives each API endpoint its own database session.
#  FastAPI calls this automatically via Depends(get_db).
#  The "yield" means: give the session to the endpoint, then close it after.
# ────────────────────────────────────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
