class Association:
    def __init__(self):
        pass
    
    def run(self):
        option = ''
        while option != 'x':
            option = self.use_option()
        print("Done")
        
    def use_option(self):
        choice = self.read_choice()
        
        return choice
    
    def read_choice():
        return input("Enter option: ")