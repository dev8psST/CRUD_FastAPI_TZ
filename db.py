from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database connection parameters
DATABASE_URL = "mysql+pymysql://root:password@localhost/test"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Declarative base for declarative class definitions
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(String(255))
    author_id = Column(Integer, ForeignKey("authors.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    author = relationship("Author", back_populates="posts")
    categories = relationship("Category", back_populates="posts")
    tags = relationship("Tag", back_populates="posts")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    posts = relationship("Post", back_populates="categories")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    posts = relationship("Post", back_populates="tags")


class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False)
    city = Column(String, nullable=False)
    name = Column(String, nullable=False)
    date_register = Column(Date, nullable=False)
    salary_in_year = Column(Float, nullable=False)
    number_phone = Column(String, nullable=False)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
