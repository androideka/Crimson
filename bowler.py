__author__ = 'mrose'


class Bowler(object):

    def __init__(self, name):
        self.name = name
        self.score = []
        self.frames = {}
        self.current_frame = 1

    def bowl(self, pins_left):
        #End-of-game stuff
        if self.current_frame >= 11:
            if len(self.frames[10]) == 2 and len(self.frames[11]) >= 1:
                return True
            elif len(self.frames[10]) == 1 and len(self.frames[11]) == 2:
                return True
            elif self.current_frame > 12:
                return False
        # Bowl logic
        if not len(self.get_current_frame()):
            pin_count = 10
            self.frames[self.current_frame] = [pin_count - pins_left]
        else:
            pin_count = 10 - self.get_current_frame()[0]
            self.frames[self.current_frame].append(pin_count - pins_left)
        frame = self.frames[self.current_frame]

        if len(frame) == 2 or sum(frame) == 10:
            self.advance_frame()
            return True
        else:
            return False

    def advance_frame(self):
        self.score.append(sum(self.get_current_frame()))
        if self.score:
            self.check_strike_or_spare()
        self.current_frame += 1
        self.frames[self.current_frame] = []

    def check_strike_or_spare(self):
        for frame, frame_score in self.frames.iteritems():
            # Check whether frame is not open
            if sum(frame_score) == 10 and len(self.score) > frame + 1 and self.score[frame - 1] <= 10:
                if len(frame_score) == 1 and len(self.score) > 2:
                    # Strike
                    print 'Strike!'
                    if frame == len(self.frames) - 1 or frame > 9:
                        break
                    if len(self.frames[frame + 1]) == 2:
                        self.score[frame - 1] += sum(self.frames[frame + 1])
                    else:
                        self.score[frame - 1] += self.frames[frame + 1][0] + self.frames[frame + 2][0]
                elif len(frame_score) != 1:
                    # Spare
                    print 'Spare!'
                    self.score[frame - 1] += self.frames[frame + 1][0]

    def get_current_frame(self):
        if len(self.frames):
            return self.frames[self.current_frame]
        else:
            return {}

    def get_last_frame(self):
        if len(self.frames) > 1:
            last_frame = self.frames[self.current_frame - 1]
            return last_frame

    def get_total_score(self):
        return sum(self.score)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_frame_scores(self):
        return self.frames

