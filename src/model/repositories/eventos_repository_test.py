from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
 
 
class SubscribersRepository:
     def insert(self, subscriber_info: dict) -> None:
         with DBConnectionHandler() as db:
             try:
                 new_subscriber = Inscritos(
                     nome=subscriber_infos.get("name"),
                     email=subscriber_infos.get("email"),
                     link=subscriber_infos.get("link"),
                     email_id=subscriber_infos.get("email_id")
                 )
                 db.session.add(new_subscriber)
                 db.session.commit()
             except Exception as exception:
                 db.session.rollback()
                 raise exception
 