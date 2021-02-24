class States:

    def __init__(self, name, capitol, abrev, largest_city):
        self.name = name
        self.capitol = capitol
        self.abrev = abrev
        self.largest_city = largest_city

    def show_name(self):
        return self.name
        
    def show_capitol(self):
        return self.capitol
        
    def show_abrev(self):
        return self.abrev
        
    def show_largest(self):
        return self.largest_city