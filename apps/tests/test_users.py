import pytest
import json

from app.models.category import Category, CategoryGroup


def test_category():
    data = json.dumps(
        {"id": 1, "title": "some title"}
    )
    category = Category.parse_raw(data)
