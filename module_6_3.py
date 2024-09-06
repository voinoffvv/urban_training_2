class Horse:
    # x_distance = 0
    # sound = 'Frrr'
    def __init__(self, x_distance = 0,    sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound
    def run(self, dx):
        self.x_distance  += dx

    pass
class Eagle:
    # y_distance = 0
    # sound = 'I train, eat, sleep, and repeat'
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    # def __init__(self):
    #     self.x_distance = super().x_distance
    #     self.y_distance = super().y_distance
    #     self.sound = Eagle.sound
    # def move(self, dx, dy):
    #     self.run(dx)
    #     self.fly(dy)
    # def get_pos(self):
    #     return (super().x_distance, super().y_distance)
    # def voice(self):
    #     print(super().sound)

p1 = Pegasus()

