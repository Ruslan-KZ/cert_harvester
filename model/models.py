from sqlalchemy import (String, Integer, Text, Column, Enum, func, DateTime, ForeignKey, Float, Boolean, DECIMAL, Date)
from sqlalchemy.orm import relationship
from database.db import Base
import enum


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    coursera_email = Column(String, unique=True, nullable=False)
    coursera_password_encrypted = Column(String, nullable=False)

    courses = relationship("Course", back_populates="user", cascade="all, delete-orphan")


class CourseStatusEnum(enum.Enum):
    pending = "pending"         
    in_progress = "in_progress" 
    done = "done"               
    failed = "failed"          


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    link = Column(Text, nullable=False)               
    name = Column(String, nullable=True)              
    duration_hours = Column(Float, nullable=True)    
    cert_link = Column(Text, nullable=True)           
    status = Column(Enum(CourseStatusEnum), default=CourseStatusEnum.pending)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="courses")


