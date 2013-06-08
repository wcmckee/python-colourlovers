import unittest


class FixtureTestCase(unittest.TestCase):
    fixtures = []

    def setUp(self):
        super(FixtureTestCase, self).setUp()
        self.data = {}

        for filename in self.fixtures:
            __, basename = filename.rsplit('/', 1)
            with open(filename) as fh:
                self.data[basename] = fh.read()
