import unittest
from main import ConfigParser

class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.parser = ConfigParser()

    def test_remove_comments(self):
        text = """
        let PI = 3.14
        " Этот комментарий должен быть удален
        let RADIUS = 5
        /* Это многострочный комментарий */
        """
        cleaned_text = self.parser.remove_comments(text)
        self.assertNotIn('" Этот комментарий должен быть удален', cleaned_text)
        self.assertNotIn('/* Это многострочный комментарий */', cleaned_text)

    def test_parse_constants(self):
        text = """
        let PI = 3.14
        let radius = 10
        table([ area = $PI$ * $radius$ * $radius$ ])
        """
        root = self.parser.parse(text)
        self.assertEqual(self.parser.constants['PI'], '3.14')
        self.assertEqual(self.parser.constants['radius'], '10')

    def test_parse_array(self):
        text = "({ 1, 2, 3, 4, 5 })"
        root = self.parser.parse(text)
        array_element = root.find('.//array')
        values = [el.text for el in array_element.findall('value')]
        self.assertEqual(values, ['1', '2', '3', '4', '5'])

    def test_parse_table(self):
        text = """
        table([ area = $PI$ * $radius$ * $radius$, status = 'active' ])
        """
        root = self.parser.parse(text)
        table_element = root.find('.//table')
        pairs = table_element.findall('pair')
        self.assertEqual(pairs[0].get('name'), 'area')
        self.assertEqual(pairs[0].text, '$PI$ * $radius$ * $radius$')
        self.assertEqual(pairs[1].get('name'), 'status')
        self.assertEqual(pairs[1].text, "'active'")

    def test_parse_constant_in_expression(self):
        text = """
        let PI = 3.14
        let radius = 10
        table([ area = $PI$ * $radius$ * $radius$ ])
        """
        root = self.parser.parse(text)
        table_element = root.find('.//table')
        pairs = table_element.findall('pair')
        self.assertEqual(pairs[0].get('name'), 'area')
        self.assertEqual(pairs[0].text, '$PI$ * $radius$ * $radius$')

    def test_format_xml(self):
        text = """
        let PI = 3.14
        table([ area = $PI$ * 2 ])
        """
        root = self.parser.parse(text)
        pretty_xml = self.parser.format_xml(root)

        self.assertIn('<table>', pretty_xml)
        self.assertIn('<pair name="area">', pretty_xml)
        self.assertIn('$PI$ * 2', pretty_xml)

if __name__ == '__main__':
    unittest.main()
