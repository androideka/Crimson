__author__ = 'androideka'


class Bowler(object):

    def __init__(self, name):
        self.name = name
        self.score = []
        self.frames = {}
        self.current_frame = 1

    def bowl(self, pins_left):
        if self.current_frame > 12:
            return True
        if self.current_frame == 12:
            print 'twelfth frame'
            if len(self.frames[10]) == 1 and len(self.frames[11]) == 1:
                self.calculate_score(pins_left)
                self.advance_frame()
            print 'this'
            return True
        if self.current_frame == 11:
            print 'eleventh frame'
            if len(self.frames[11]) > 2:
                return True
            if len(self.frames[10]) == 1:
                print 'tenth strike'
                self.calculate_score(pins_left)
                if self.frames[11] == [10]:
                    self.advance_frame()
                    print 'that'
                    return False
                elif len(self.frames[11]) == 1:
                    print 'what'
                    return False
                else:
                    return True
            elif sum(self.frames[10]) == 10:
                print 'is this the one you want?'
                if len(self.frames[11]) < 1:
                    self.calculate_score(pins_left)
                self.advance_frame()
                return True
            else:
                self.advance_frame()
                print 'this!'
                return True

        #End-of-game stuff
        print self.current_frame

        if self.current_frame == 10:
            self.calculate_score(pins_left)
            print 'tenth frame'
            print 'Fucking frames: ' + str(self.frames)
            if self.frames[10] == [10]:
                self.advance_frame()
                print 'huh?'
                return False
            elif sum(self.frames[10]) == 10:
                self.advance_frame()
                print 'FUCK OFF'
                return False
            elif len(self.frames[10]) == 2:
                print 'here'
                self.advance_frame()
                return True
            else:
                return False
        self.calculate_score(pins_left)
        if len(self.frames[self.current_frame]) == 2 or sum(self.frames[self.current_frame]) == 10:
            self.advance_frame()
            print 'GODDAMMIT'
            return True
        else:
            return False

    def calculate_score(self, pins_left):
        if not len(self.get_current_frame()):
            pin_count = 10
            self.frames[self.current_frame] = [pin_count - pins_left]
        else:
            pin_count = 10 - self.get_current_frame()[0]
            self.frames[self.current_frame].append(pin_count - pins_left)

    def advance_frame(self):
        self.score.append(sum(self.get_current_frame()))
        if self.score and self.current_frame < 12:
            self.check_strike_or_spare()
        self.current_frame += 1
        self.frames[self.current_frame] = []

    def check_strike_or_spare(self):
        for frame, frame_score in self.frames.iteritems():
            # Check whether frame is not open
            if sum(frame_score) == 10 and len(self.score) > frame and self.score[frame - 1] <= 10:
                if len(frame_score) == 1 and len(self.score) > 2:
                    # Strike
                    if frame == len(self.frames) - 1 or self.current_frame >= 12:
                        break
                    if len(self.frames[frame + 1]) == 2:
                        self.score[frame - 1] += sum(self.frames[frame + 1])
                    else:
                        self.score[frame - 1] += self.frames[frame + 1][0] + self.frames[frame + 2][0]
                elif len(frame_score) != 1:
                    # Spare
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

