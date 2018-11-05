
class GameObject:

    def __init__(self,type,size_x,size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.type = type


    def __repr__(self):
        return "type: " + self.type + ", size_x: {}, size_y: {}".format(self.size_x, self.size_y)


    



