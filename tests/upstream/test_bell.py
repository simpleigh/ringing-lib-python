import unittest

from ringing import MAX_BELLS, Bell


class BellTest(unittest.TestCase):
    def test_bell(self):
        self.assertEqual(Bell(), 0)
        self.assertEqual(Bell(4), 4)
        self.assertEqual(Bell(MAX_BELLS), MAX_BELLS)

    def test_bell_from_char(self):
        self.assertEqual(Bell('5'), 4)
        self.assertEqual(Bell('0'), 9)
        self.assertEqual(Bell('T'), 11)

        # Should this be a custom excption?
        self.assertRaises(ValueError, lambda: Bell('%'))

    def test_bell_to_char(self):
        self.assertEqual(str(Bell(5)), '6')
        self.assertEqual(str(Bell(10)), 'E')
        self.assertEqual(str(Bell(14)), 'C')
        self.assertEqual(str(Bell(MAX_BELLS)), '*')

    # test_bell_output omitted as we only support MAX_BELLS bells
