from src.model.entities.InscritosGroup import inscritosGroup
from src.model.repositories.interface.inscritos_group_respository import inscritosRepositoryInterface


class InscritosGroupRepository(inscritosRepositoryInterface):
  
  def insert_subscriber(self, subscriber_id: str ) -> None: pass
    
  def select_group(self, group_name: str)-> inscritosGroup: pass