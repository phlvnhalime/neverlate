from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# ── CONCEPT: MODEL = TABLE ───────────────────────────────────────────────────
#  This class defines what the "tasks" table looks like in PostgreSQL.
#  Each attribute = one column in the table.
#
#  When the app starts, SQLAlchemy reads this and creates the table
#  in PostgreSQL automatically if it doesn't exist yet.
#
#  SQL equivalent:
#  CREATE TABLE tasks (
#      id          SERIAL PRIMARY KEY,
#      title       VARCHAR NOT NULL,
#      description VARCHAR,
#      completed   BOOLEAN DEFAULT FALSE,
#      category    VARCHAR DEFAULT 'General',
#      priority    VARCHAR DEFAULT 'Medium'
#  );
# ────────────────────────────────────────────────────────────────────────────

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed   = Column(Boolean, default=False)
    category    = Column(String, default="General")
    priority    = Column(String, default="Medium")
