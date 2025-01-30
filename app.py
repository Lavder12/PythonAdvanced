from sqlalchemy import create_engine, Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import dotenv
import os

dotenv.load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="product")
