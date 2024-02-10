class RecentCounter(object):
    from collections import deque
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)

        # because ping is increasing, once the new ping passes 3000, remove older pings to stay in range
        while t - self.q[0] > 3000:
            self.q.popleft()

        return len(self.q)

