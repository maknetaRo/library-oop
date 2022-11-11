class Room():
    cabinets = []
    def __init__(self, name, max_cabinets_number):
        self.name = name
        self.max_cabinets_number = max_cabinets_number

    def add_cabinet(self, cabinet):
        if (len(self.cabinets) <  self.max_cabinets_number):
            self.cabinets.append(cabinet)
        else:
            raise Exception("You can't add more cabinets into that room.")