from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "meuNome222",
        "email": "email22@email.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
    
@pytest.mark.skip("Insert in DB")    
def test_select_subscriber():
    email = "email22@email.com"
    event_id = 2
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, event_id)
    print(resp.nome)