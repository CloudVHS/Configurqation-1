import re
import xml.etree.ElementTree as ET
from xml.dom import minidom


class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse(self, text):
        text = self.remove_comments(text)

        lines = text.splitlines()

        root = ET.Element("configuration")
        for line in lines:
            self.parse_line(line, root)

        return root

    def remove_comments(self, text):
        text = re.sub(r'"[^\n]*', '', text)

        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

        return text

    def parse_line(self, line, root):
        line = line.strip()
        if not line:
            return

        if line.startswith("let "):
            self.parse_constant(line)
        elif line.startswith("table("):
            self.parse_table(line, root)
        elif line.startswith("({"):
            self.parse_array(line, root)

    def parse_constant(self, line):
        # Пример let PI = 3.14
        match = re.match(r"let (\w+) = (.+)", line.strip())
        if match:
            name = match.group(1)
            value = match.group(2).strip()
            self.constants[name] = value

    def parse_table(self, line, root):
        table_element = ET.SubElement(root, "table")
        line = line[len("table(["):-2]
        pairs = [pair.strip() for pair in line.split(",")]
        for pair in pairs:
            match = re.match(r"(\w+) = (.+)", pair)
            if match:
                name = match.group(1)
                value = match.group(2)
                pair_element = ET.SubElement(table_element, "pair", name=name)
                pair_element.text = value

    def parse_array(self, line, root):
        array_element = ET.SubElement(root, "array")
        line = line[len("({"):-2]
        values = [value.strip() for value in line.split(",")]
        for value in values:
            value_element = ET.SubElement(array_element, "value")
            value_element.text = value

    def format_xml(self, root):
        xml_str = ET.tostring(root, encoding="utf-8", method="xml").decode("utf-8")
        return minidom.parseString(xml_str).toprettyxml(indent="  ")


def main(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        input_text = file.read()

    parser = ConfigParser()
    root = parser.parse(input_text)

    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)


if __name__ == "__main__":
    input_filename = 'config1.txt'
    output_filename = 'output.xml'
    main(input_filename, output_filename)
