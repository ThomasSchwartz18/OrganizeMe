class Notebook:
    def __init__(self, name):
        self.name = name
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def delete_section(self, section_name):
        self.sections = [s for s in self.sections if s.name != section_name]