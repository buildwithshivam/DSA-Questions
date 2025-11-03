from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue=deque([])

    def ping(self, t: int) -> int:
        previous=t-3000
        while self.queue and self.queue[0]<previous:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue) 


