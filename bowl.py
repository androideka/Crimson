__author__ = 'androideka'

import PySide

class Bowl(object):

    name = ''
    frame_scores = {}
    frame = 1
    score = []

    def __init__(self, name):
        self.name = name
        self.frame_scores = {
            1: []
        }

    def bowl(self, pin_count):
        # Pin count is the number of pins still standing after a bowl. Strike/spare -> pin_count = 0
        if pin_count > 10 or pin_count < 0:
            raise ValueError('Only values 0-10 accepted. Pin counter error.')
            return False

        # Don't forget about the bonus frame if the 10th frame is a strike or a spare
        current_frame_score = self.frame_scores[self.frame]

        if len(current_frame_score) != 0:
            pins_left = 10 - current_frame_score[0]
        else:
            pins_left = 10

        # Spare
        if self.frame > 1:
            last_frame = self.frame_scores[self.frame - 1]
            if sum(last_frame) == 10 and len(last_frame) > 1 and len(self.frame_scores[self.frame]) == 1:
                self.score[self.frame - 2] += 10 - pin_count
        if self.frame > 2:
            if self.frame_scores[self.frame - 2] == [10]:
                print 'strike'
                #self.score[self.frame - 2]

        current_frame_score.append(pins_left - pin_count)
        if not pin_count or len(current_frame_score) == 2:
            self.frame += 1
            self.frame_scores[self.frame] = []
            self.score.append(sum(current_frame_score))

        print self.frame_scores
        print 'Score:' + str(self.score)

    def total_score(self):
        return sum(self.score)

bob = Bowl('Bob')
bob.bowl(1)
bob.bowl(0)
bob.bowl(3)
bob.bowl(2)
bob.bowl(1)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
print bob.total_score()

