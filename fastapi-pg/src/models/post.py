from sqlalchemy import Column, Integer, String, Text, Boolean
from src.database.base_class import Base

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    published = Column(Boolean, default=False)