
class Band():

    instances = []

    def __init__(self, name, members=None):

        self.name = name
        self.members = members
        Band.instances.append(self)
    
    
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        
        return solos


    @classmethod
    def to_list(band):
        return band.instances



class Musician():
    
    def __init__(self,name):
        self.name = name



class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)
        self.instrument = "guitar"
        self.intro = f"My name is {self.name} and I play {self.instrument}"
        self.solo = "face melting guitar solo"

    def __str__(self):
        return self.intro

    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    

    def play_solo(self):
        return self.solo
    

    def get_instrument(self):
        return self.instrument




class Bassist(Musician):

    def __init__(self,name):
        super().__init__(name)
        self.instrument = "bass"
        self.intro = f"My name is {self.name} and I play {self.instrument}"
        self.solo = "bom bom buh bom"

    def __str__(self):
        return self.intro

    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    

    def play_solo(self):
        return self.solo
    

    def get_instrument(self):
        return self.instrument



class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)
        self.instrument = "drums"
        self.intro = f"My name is {self.name} and I play {self.instrument}"
        self.solo = "rattle boom crash"

    def __str__(self):
        return self.intro

    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    

    def play_solo(self):
        return self.solo
    

    def get_instrument(self):
        return self.instrument