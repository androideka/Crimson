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

        if not len(self.get_current_frame()):
            pin_count = 10
        else:
            pin_count = 10 - self.get_current_frame()[0]
        self.frames[self.current_frame].append(pin_count - pins_left)
        frame = self.frames[self.current_frame]
        if len(frame) == 2 or sum(frame) == 10:
            self.advance_frame()

        print 'Current frame: ' + str(self.current_frame)
        print 'Frame scores: ' + str(self.frames)
        print 'Score: ' + str(self.score)

    def advance_frame(self):
        if self.score:
            self.check_strike_or_spare()
        if len(self.frames):
            self.score.append(sum(self.get_current_frame()))
        self.current_frame += 1
        self.frames[self.current_frame] = []

    def check_strike_or_spare(self):
        for frame, frame_score in self.frames.iteritems():
            if sum(frame_score) == 10 and len(self.score) > frame and self.score[frame] <= 10:
                if len(frame_score) == 1 and len(self.score) > 2:
                    # Strike
                    print 'Strike!'
                    
                elif len(frame_score) != 1:
                    # Spare
                    print 'Spare!'
                    self.score[frame] += self.frames[frame + 1][0]

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def get_last_frame(self):
        if len(self.frames) > 1:
            last_frame = self.frames[self.current_frame - 1]
            return last_frame


bob = Bowler("Bob")
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)
bob.bowl(0)