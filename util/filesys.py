import json

class FileIO:
    def __init__(self):
        pass
    
    def read(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    
    def write(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f)
    