class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequency of each task
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        # always process the most frequent task first -> store in maxHeap
        maxHeap = []
        for task, frequency in freq.items():
            heapq.heappush(maxHeap, -frequency)
        
        # to enforce cooldown, keep track of a queue
        q = deque() # pair of (frequency, idleTime)
        time = 0 

        while maxHeap or q:
            time += 1

            # process the maximum frequency element from the maxHeap
            if maxHeap:
                count = heapq.heappop(maxHeap) * -1
                count = count - 1
                if count > 0:
                    q.append((count, time +n))

            # check if any element in the queue finish it idle time
            # -> add back the the heap
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q[0][0] * -1)
                q.popleft()
        return time