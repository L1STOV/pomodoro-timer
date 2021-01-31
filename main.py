import time
from gui import gui
from plyer import notification


class Pomodoro:
    def __init__(self, task_name, pomodoro_count=1, pomodoro_duration=25, breaks=0, break_duration=5):
        self.task_name = task_name
        self.pomodoro_count = pomodoro_count
        self.pomodoro_duration = pomodoro_duration
        self.breaks = breaks
        self.break_duration = break_duration

    def notifier(self):
        pass


if __name__ == '__main__':
    pass
