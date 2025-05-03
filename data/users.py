import dataclasses
import enum


@dataclasses.dataclass()
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    date_of_birth: []
    subjects: str
    hobbies: enum
    image_name: str
    address: str
    state: str
    city: str


student = User(
    first_name="Oksana",
    last_name="Ivanova",
    email="ivanova_oksana@mail.ru",
    gender="Female",
    phone='8987456327',
    date_of_birth=['1999', 'February', '15'],
    subjects="Physics",
    hobbies='Reading',
    image_name=('test_image.jpg'),
    address="ul. Pobednaya, d.7, kv.55",
    state="Haryana",
    city="Panipat"
)