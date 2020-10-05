from datetime import datetime

import pytest

from challenges.codewars.objectid import Mongo


class TestMongo:
    @pytest.mark.parametrize('oid', [
        '5eeaa9f471cf5af67b7feaae',
        '507f1f77bcf86cd799439016'
    ])
    def test_mongo_correctly_identifies_valid_object_ids(self, oid):
        assert Mongo.is_valid(oid) is True

    @pytest.mark.parametrize('oid', [
        'd07f1f77bcf86FF799439016',
        '507f1f77bcF86cd799439011',
        'greger',
        'greghrehersher',
        5,
        True,
        []
    ])
    def test_mongo_correctly_identifies_invalid_object_ids(self, oid):
        assert Mongo.is_valid(oid) is False

    @pytest.mark.parametrize('oid,time', [
        (True, False),
        (False, False),
        ('greger', False),
        ('507f1f77bcf86cd799439016', datetime(2012, 10, 17, 16, 13, 27)),
        ('d07f1f77bcf86cd799439016', datetime(2080, 11, 4, 18, 27, 35)),
    ])
    def test_mongo_correctly_returns_oid_time(self, oid, time):
        assert Mongo.get_timestamp(oid) == time
