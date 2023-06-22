#!/usr/bin/python3
"""City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """City"""

    def __init__(self, *args, **kwargs):
        """City"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """State_id"""
        new = self.value()
        self.assertEqual((new.state_id), None)

    def test_name(self):
        """test_name"""
        new = self.value()
        self.assertEqual((new.name), None)
