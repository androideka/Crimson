__author__ = 'androideka'


class Bowler(object):

    def __init__(self, name):
        self.name = name
        self.score = []
        self.frames = {}
        self.current_frame = 1

    """ Rolls a bowling ball. Special (lengthy) logic for final frame
    """
    def bowl(self, pins_left):
        # Tenth-frame logic
        if self.current_frame == 12:
            if len(self.frames[10]) == 1 and len(self.frames[11]) == 1:
                self.calculate_score(pins_left)
                self.advance_frame()
            return True
        elif self.current_frame == 11:
            if len(self.frames[11]) > 2:
                return True
            elif len(self.frames[10]) == 1:
                self.calculate_score(pins_left)
                if self.frames[11] == [10]:
                    self.advance_frame()
                    return False
                elif len(self.frames[11]) == 1:
                    return False
                else:
                    return True
            elif sum(self.frames[10]) == 10:
                if len(self.frames[11]) < 1:
                    self.calculate_score(pins_left)
                self.advance_frame()
                return True
            else:
                self.advance_frame()
                return True
        elif self.current_frame == 10:
            self.calculate_score(pins_left)
            if self.frames[10] == [10] or sum(self.frames[10]) == 10:
                self.advance_frame()
                return False
            elif len(self.frames[10]) == 2:
                self.advance_frame()
                return True
            else:
                return False

        # Every other frame
        self.calculate_score(pins_left)
        if len(self.frames[self.current_frame]) == 2 or sum(self.frames[self.current_frame]) == 10:
            self.advance_frame()
            return True
        else:
            return False

    """ Get score for current roll, given pins left standing
    """
    def calculate_score(self, pins_left):
        if not len(self.get_current_frame()):
            pin_count = 10
            self.frames[self.current_frame] = [pin_count - pins_left]
        else:
            pin_count = 10 - self.get_current_frame()[0]
            self.frames[self.current_frame].append(pin_count - pins_left)

    """ Adds an empty frame to the end of frames score
    """
    def advance_frame(self):
        self.score.append(sum(self.get_current_frame()))
        if self.score and self.current_frame < 12:
            self.check_strike_or_spare()
        self.current_frame += 1
        self.frames[self.current_frame] = []

    """ Implements special scoring for strikes and spares and changes scores accordingly
    """
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
            return self.frames[self.current_frame - 1]

    def get_total_score(self):
        return sum(self.score)

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_frame_scores(self):
        return self.frames

