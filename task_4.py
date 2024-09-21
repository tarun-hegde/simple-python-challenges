import threading
import time
from collections import defaultdict, deque

class RateLimiter:
    """
    RateLimiter class to limit the number of requests a user can make within a specified time window.
    """
    def __init__(self, max_requests, time_window):
        """
        Initializes the rate limiter with a maximum number of requests and a time window.
        """

        self.max_requests = max_requests
        self.time_window = time_window
        self.lock = threading.Lock()
        self.requests = defaultdict(deque)

    def allow_request(self, user_id):
        """
        Determines if a request from a user is allowed based on the rate limiting policy.
        This method checks if the number of requests made by the user within a specified
        time window is below the maximum allowed requests. If so, it records the current
        request and returns True. Otherwise, it returns False.
        """

        current_time = time.time()
        with self.lock:
            if user_id in self.requests:
                # Remove outdated requests
                while self.requests[user_id] and self.requests[user_id][0] <= current_time - self.time_window:
                    self.requests[user_id].popleft()
            
            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

#this is for running the task
if __name__ == "__main__":
    rate_limiter = RateLimiter(max_requests=5, time_window=60)

    user_id = "user_123"
    for i in range(10):
        if rate_limiter.allow_request(user_id):
            print(f"Request {i+1} allowed")
        else:
            print(f"Request {i+1} denied")
        time.sleep(10)  