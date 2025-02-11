class Section:
    def __init__(self, name, section_type):
        self.name = name
        self.type = section_type  # "page" or "sheet"
        self.pages = []