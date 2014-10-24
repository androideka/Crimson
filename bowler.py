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
            # Check whether frame is not open
            if sum(frame_score) == 10 and len(self.score) > frame and self.score[frame] <= 10:
                if len(frame_score) == 1 and len(self.score) > 2:
                    # Strike
                    if frame == len(self.frames) - 2 or frame > 8:
                        break
                    if len(self.frames[frame + 1]) == 2:
                        self.score[frame] += sum(self.frames[frame + 1])
                    else:
                        self.score[frame] += self.frames[frame + 1][0] + self.frames[frame + 2][0]

                elif len(frame_score) != 1:
                    # Spare
                    self.score[frame] += self.frames[frame + 1][0]

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def get_last_frame(self):
        if len(self.frames) > 1:
            last_frame = self.frames[self.current_frame - 1]
            return last_frame

    def get_total_score(self):
        return sum(self.score)

    def get_name(self):
        return self.name


bob = Bowler("Bob")
bob.bowl(5)
bob.bowl(0)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
bob.bowl(10)
print bob.get_total_score()