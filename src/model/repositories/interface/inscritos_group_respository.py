from src.model.repositories.interface.inscritos_group_respository import inscritosGroup
from abc import ABC, abstractmethod

class inscritosRepositoryInterface():
  @abstractmethod
  def insert_subscriber(self, subscriber_id: str ) -> None: pass
  @abstractmethod
  def select_group(self, group_name: str)-> inscritosGroup: pass