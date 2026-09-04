from datetime import datetime, timezone

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from backend.app.database.connection import Base


class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    security_score = Column(
        Integer,
        nullable=False
    )

    total_checks = Column(
        Integer,
        nullable=False
    )

    passed_checks = Column(
        Integer,
        nullable=False
    )

    critical = Column(Integer, default=0)
    high = Column(Integer, default=0)
    medium = Column(Integer, default=0)
    low = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )