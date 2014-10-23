__author__ = 'androideka'


class Bowl(object):

    name = ''
    frame_scores = {}
    frame = 1
    score = 0

    def __init__(self, name):
        self.name = name
        self.frame_scores = {
            1: []
        }

    def bowl(self, pin_count):
        # Pin count is the number of pins still standing after a bowl. Strike/spare -> pin_count = 0
        if pin_count > 10:
            raise ValueError('Only values 0-10 accepted. Pin counter error.')
            return False
        # Don't forget about the bonus frame if the 10th frame is a strike or a spare
        current_frame = self.frame_scores[self.frame]
        if len(current_frame) != 0:
            pins_left = 10 - current_frame[0]
        else:
            pins_left = 10
        if not pin_count:
            current_frame.append(pins_left - pin_count)
            self.frame += 1
            self.frame_scores[self.frame] = []
            self.score += sum(current_frame)
        else:
            current_frame.append(pins_left - pin_count)
            if len(current_frame) == 2:
                self.frame += 1
                self.frame_scores[self.frame] = []
                self.score += sum(current_frame)

        print self.frame_scores
        print self.score


bob = Bowl('Bob')
bob.bowl(9)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(3)
bob.bowl(0)


