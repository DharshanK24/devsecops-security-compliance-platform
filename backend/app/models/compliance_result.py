from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from backend.app.database.connection import Base


class ComplianceResult(Base):
    __tablename__ = "compliance_results"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    compliance_score = Column(
        Integer,
        nullable=False
    )

    total_checks = Column(
        Integer,
        nullable=False
    )

    compliant_checks = Column(
        Integer,
        nullable=False
    )

    review_required = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )