from sqlalchemy import String, Integer, Text, Column, func, DateTime, ForeignKey, Float, Boolean, DECIMAL, Date
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable= False)
    password = Column(String, nullable=False)

    courses = relationship("CourseStatus", back_populates="user")

class CourseStatus(Base):
    __tablename__ = 'course_status'

    id = Column(Integer, primary_key=True, index=True)
    user_id =Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Boolean, default=False)

    user = relationship("User", back_populates="courses")
    finished = relationship("FinishedCourses", back_populates="status")

class FinishedCourses(Base):
    __tablename__ = 'finished_courses'

    id = Column(Integer, primary_key=True, index=True)
    user_cert_id = Column(Integer,ForeignKey('course_status.id'),nullable=True)
    link_cert = Column(Text,nullable=False) 
    course_hauor = Column(Float, nullable=False )

    status = relationship("CourseStatus", back_populates="finished")


