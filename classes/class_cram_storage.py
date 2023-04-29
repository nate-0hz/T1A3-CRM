class File:
    def __init__(self, filename):
        self.filename = filename

class CramFile(File):
    def __init__(self, filename, file_attr):
        super().__init__(filename)
        self.file_attr = file_attr

#### Incomplete and unused