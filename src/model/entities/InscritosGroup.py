from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class inscritosGroup(Base):
    __tablename__ = "inscritos_group"
    
    id = Column(Integer, primary_key = True, autoincrement = true)
    evento_id = Column(Integer, ForeignKey("Eventos.id"))
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"))