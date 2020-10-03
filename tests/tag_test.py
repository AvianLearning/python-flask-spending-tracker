import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def test_tag_has_category(self):
        tag = Tag("travel")
        self.assertEqual("travel", tag.category)