class Record:
    def __init__(self, row):
        self.values = row

    def __repr__(self):
        return f"Record({self.values})"
