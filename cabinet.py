class Cabinet():
    shelves = []
    def __init__(self, genre):
        self.genre = genre        

    def add_shelf(self, shelf):
        self.shelves.append(shelf)
