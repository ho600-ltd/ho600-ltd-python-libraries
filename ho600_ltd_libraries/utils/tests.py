import unittest

from ho600_ltd_libraries.utils.formats import customize_hex_from_integer

class FormatsTest(unittest.TestCase):
    def test_customize_hex_from_integer(self):
        self.assertEqual('0', customize_hex_from_integer(0))
        self.assertEqual('ff', customize_hex_from_integer(255))
        self.assertEqual('100', customize_hex_from_integer(256))
        self.assertEqual('fff', customize_hex_from_integer(4095))
        self.assertEqual('1000', customize_hex_from_integer(4096))
        self.assertEqual('ffff', customize_hex_from_integer(65535))
        self.assertEqual('10000', customize_hex_from_integer(65536))

        self.assertEqual('0', customize_hex_from_integer(0, base='0123456789abcdefghijklmnopqrstuv'))
        self.assertEqual('v', customize_hex_from_integer(31, base='0123456789abcdefghijklmnopqrstuv'))
        self.assertEqual('10', customize_hex_from_integer(32, base='0123456789abcdefghijklmnopqrstuv'))
        self.assertEqual('vv', customize_hex_from_integer(1023, base='0123456789abcdefghijklmnopqrstuv'))
        self.assertEqual('100', customize_hex_from_integer(1024, base='0123456789abcdefghijklmnopqrstuv'))

if __name__ == '__main__':
    unittest.main()
