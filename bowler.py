__author__ = 'mrose'


class Bowler(object):

    name = ''
    score = []
    frames = {}
    current_frame = -1

    def __init__(self, name):
        self.name = name
        self.advance_frame()

    def bowl(self, pins_left):

        if not pins_left:
            if not len(self.get_current_frame()):
                print "Strike!"
                pin_count = 10
            else:
                print "Spare!"
                pin_count = 10 - self.get_current_frame()[0]
            self.frames[self.current_frame].append(pin_count - pins_left)
            self.advance_frame()
        else:
            if not len(self.get_current_frame()):
                pin_count = 10
            else:
                pin_count = 10 - self.get_current_frame()[0]
            self.frames[self.current_frame].append(pin_count - pins_left)
            if len(self.frames[self.current_frame]) == 2:
                self.advance_frame()

        print 'Current frame: ' + str(self.current_frame)
        print 'Frame scores: ' + str(self.frames)
        print 'Score: ' + str(self.score)

    def advance_frame(self):
        self.check_strike_or_spare()
        if len(self.frames):
            self.score.append(sum(self.get_current_frame()))
        self.current_frame += 1
        self.frames[self.current_frame] = []

    def check_strike_or_spare(self):
        for frame, frame_score in self.frames.iteritems():
            print frame
            if sum(frame_score) == 10 and self.score and self.score[frame] <= 10:
                if len(frame_score) == 1 and len(self.frames) - 2 > frame:
                    # Strike
                    self.score[frame] += sum(self.frames[frame + 1])
                    if len(self.frames[frame + 1]) == 1:
                        self.score[frame] += self.frames[frame + 2][0]
                else:
                    # Spare
                    self.score[frame] += self.frames[frame + 1][0]


    def get_current_frame(self):
        return self.frames[self.current_frame]

    def get_last_frame(self):
        if len(self.frames) > 1:
            last_frame = self.frames[self.current_frame - 1]
            return last_frame


bob = Bowler("Bob")
bob.bowl(5)
bob.bowl(0)
bob.bowl(1)
bob.bowl(0)
bob.bowl(5)
bob.bowl(4)
