import numpy as np

class Detector(object):

    def __init__(self):
        self.result = False
        self.counter = 0

    def detectar(self, senal):

        noise = ((np.random.random())*0.001)
        for i in senal:
            if i > noise:
                self.counter += 1
        if self.counter > len(senal)/2:
            self.result = True

        return self.result
