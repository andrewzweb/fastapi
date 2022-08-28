import pytest
import json
from .category import Category, CategoryGroup, CategoryNew


fake_category_data = {
    "data": {
        "status": "active",
        "description": "Багатофункціональні пристрої друку",
        "classification": {
            "scheme": "ДК021",
            "description": "Комп’ютерне обладнання",
            "id": "30230000-0"
        },
        "title": "Принтери багатофункціональні",
        "procuringEntity": {
            "contactPoint": {
                "url": "http://cpb.org.ua/",
                "faxNumber": "380445780480",
                "telephone": "+380441234567",
                "name": "Олександр Дем'яненко",
                "email": "baion1475@gmail.com"
            },
            "identifier": {
                "scheme": "UA-EDR",
                "id": "40000777",
                "legalName": "ДЕРЖАВНА УСТАНОВА «ПРОФЕСІЙНІ ЗАКУПІВЛІ»"
            },
            "kind": "central",
            "address": {
                "countryName": "Україна",
                "postalCode": "01601",
                "region": "м. Київ",
                "streetAddress": "вул. Бульварно-Кудрявська, 22",
                "locality": "м. Київ"
            },
            "name": "ДЕРЖАВНА УСТАНОВА «ПРОФЕСІЙНІ ЗАКУПІВЛІ»"
        },
        "images": [
            {
                "url": "/static/images/cat_mfu_939678.png",
                "sizes": "800x800"
            }
        ],
        "dateModified": "2021-07-23T16:04:49.051604+03:00",
        "id": "30230000-939678-40000777"
    }
}


def test_category():
    data = json.dumps(
        {"id": 1, "title": "some title",
         "group": {
             "id": 1,
             "title": "title group",
             "code": "1200203-09"}
         }
    )
    category = Category.parse_raw(data)
    print(category)
    print(category.group)


def test_parse_category():
    
    raw_data = json.dumps(fake_category_data['data'])
    category = CategoryNew.parse_raw(raw_data)
    print(category)

