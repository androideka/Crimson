__author__ = 'androideka'


class Bowl(object):

    name = ''
    score = []
    frame = 1

    def __init__(self, name):
        self.name = name
        self.score = []

    def bowl(self, pin_count):
        # Pin count will be the number of pins still standing after a bowl
        if not pin_count:
            self.score.append(10)
            self.frame += 1
            print self.frame
            print self.score
        elif 


bowl = Bowl([])
bowl.bowl(0)