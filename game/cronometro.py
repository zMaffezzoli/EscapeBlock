import time

class Cronometro:
    def __init__(self):
        self.start = time.perf_counter()

    def obter_tempo(self):
        tempo = time.perf_counter() - self.start
        return f"{tempo:.2f}"