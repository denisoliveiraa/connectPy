from src.model.entities.inscritos import Inscritos
from abc import ABC, abstractRepository

class SubscribersRepositoryInterface(ABC):
     @abstractRepository
     def insert(self, subscriber_infos: str) -> None: pass

     @abstractRepository
     def select_subscriber(self, email: str, event_id: int ) -> Inscritos: pass
        