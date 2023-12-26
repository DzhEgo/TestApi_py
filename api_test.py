import requests
import pytest
from faker import Faker
import allure

@pytest.fixture(scope="session")
def faker_fixture():
    return Faker()

@pytest.fixture
def base_url():
    return "http://localhost:3030"

@allure.feature("Управление пользователями")
@allure.story("Создание пользователя")
def test_user_post(faker_fixture, base_url):
    with allure.step("Создание пользователя с рандомными значениями"):
        data = {"name": faker_fixture.name(), "password": faker_fixture.word(), "email": faker_fixture.email()}
        response = requests.post(f"{base_url}/user", json=data)
        assert response.status_code == 200

@allure.feature("Управление пользователями")
@allure.story("Получение пользователей")
def test_user_get(base_url):
    with allure.step("Получение всех пользователей"):
        response = requests.get(f"{base_url}/user")
        assert response.status_code == 200

@allure.feature("Управление пользователями")
@allure.story("Получение пользователя по ID")
def test_user_find(base_url):
    with allure.step("Получение пользователя по ID"):
        response = requests.get(f"{base_url}/user/9")
        assert response.status_code == 200

@allure.feature("Управление пользователями")
@allure.story("Удаление пользователя по ID")
def test_user_delete(base_url):
    with allure.step("Удаление пользователя по ID"):
        response = requests.delete(f"{base_url}/user/9")
        assert response.status_code == 200

@allure.feature("Управление книгами")
@allure.story("Создание книги")
def test_book_post(faker_fixture, base_url):
    with allure.step("Создание книги с рандомными значениями"):
        data = {"title": faker_fixture.word(), "autor": faker_fixture.name(), "pages": faker_fixture.random_digit()}
        response = requests.post(f"{base_url}/book", json=data)
        assert response.status_code == 200

@allure.feature("Управление книгами")
@allure.story("Получение книг")
def test_book_get(base_url):
    with allure.step("Получение всех книг"):
        response = requests.get(f"{base_url}/book")
        assert response.status_code == 200

@allure.feature("Управление книгами")
@allure.story("Получение книги по ID")
def test_book_find(base_url):
    with allure.step("Получение книги по ID"):
        response = requests.get(f"{base_url}/book/1")
        assert response.status_code == 200

@allure.feature("Управление доставкой")
@allure.story("Создание доставки")
def test_delivery_post(faker_fixture, base_url):
    with allure.step("Создание доставки с рандомными значениями"):
        data = {"type": faker_fixture.word(), "address": faker_fixture.address()}
        response = requests.post(f"{base_url}/delivery", json=data)
        assert response.status_code == 200

@allure.feature("Управление доставкой")
@allure.story("Получение доставки")
def test_delivery_get(base_url):
    with allure.step("Получение всех данных о доставках"):
        response = requests.get(f"{base_url}/delivery")
        assert response.status_code == 200

@allure.feature("Управление доставкой")
@allure.story("Получение доставки по ID")
def test_delivery_find(base_url):
    with allure.step("Получение данных о доставке по ID"):
        response = requests.get(f"{base_url}/delivery/1")
        assert response.status_code == 200

@allure.feature("Управление транспортом")
@allure.story("Добавление транспорта")
def test_vechicle_post(faker_fixture, base_url):
    with allure.step("Добавление транспорта с рандомными значениями"):
        data = {"brend": faker_fixture.company(), "model_vech": faker_fixture.word(), "dismensioins": faker_fixture.word()}
        response = requests.post(f"{base_url}/vechicle", json=data)
        assert response.status_code == 200

@allure.feature("Управление транспортом")
@allure.story("Получение транспорта")
def test_vechicle_get(base_url):
    with allure.step("Получение всех данных о транспортах"):
        response = requests.get(f"{base_url}/vechicle")
        assert response.status_code == 200

@allure.feature("Управление транспортом")
@allure.story("Получение транспорта по ID")
def test_vechicle_find(base_url):
    with allure.step("Получение данных о транспорте по ID"):
        response = requests.get(f"{base_url}/vechicle/1")
        assert response.status_code == 200

@allure.feature("Управление транспортом")
@allure.story("Обновление транспорта")
def test_vechicle_put(faker_fixture, base_url):
    with allure.step("Обновление данных о транспорте по ID"):
        data = {"brend": faker_fixture.company(), "model_vech": faker_fixture.word(), "dismensioins": faker_fixture.word()}
        response = requests.put(f"{base_url}/vechicle/14", json=data)
        assert response.status_code == 200

@allure.feature("Управление задачами")
@allure.story("Создание задачи")
def test_task_post(faker_fixture, base_url):
    with allure.step("Создание задачи с рандомными значениями"):
        data = {"description": faker_fixture.sentence(), "completed": faker_fixture.boolean()}
        response = requests.post(f"{base_url}/task", json=data)
        assert response.status_code == 200

@allure.feature("Управление задачами")
@allure.story("Получение задач")
def test_task_get(base_url):
    with allure.step("Получение данных о всех задачах"):
        response = requests.get(f"{base_url}/task")
        assert response.status_code == 200

@allure.feature("Управление задачами")
@allure.story("Получение задачи по ID")
def test_task_find(base_url):
    with allure.step("Получение данных задачу по ID"):
        response = requests.get(f"{base_url}/task/3")
        assert response.status_code == 200

@allure.feature("Управление задачами")
@allure.story("Удаление задачи")
def test_task_delete(base_url):
    with allure.step("Удаление задачи по ID"):
        response = requests.delete(f"{base_url}/task/6")
        assert response.status_code == 200

@allure.feature("Управление задачами")
@allure.story("Получение содержимого задачи")
def test_task_get_content(base_url):
    with allure.step("Получение задачи с известным описанием"):
        ex_descrition = "Bit side important yard."
        response = requests.get(f"{base_url}/task/11")
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['description'] == ex_descrition

@allure.feature("Управление задачами")
@allure.story("Создание задачи с верными данными")
def test_task_post_invalid(base_url):
    with allure.step("Добавление задачи с верными данными"):
        data = {"completed": True}
        response = requests.post(f"{base_url}/task", json=data)
        assert response.status_code == 200