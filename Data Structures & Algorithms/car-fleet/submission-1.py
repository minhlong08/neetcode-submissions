class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0] * n

        for i in range(n):
            timeToTarget = float((target - position[i])) / float(speed[i])
            time[i] = (position[i], timeToTarget)
        
        time.sort()
        fleet = n

        stack = deque()
        for i in range(0, len(time)):
            # check if the previous car can catch up with the car infront
            while stack and stack[-1][1] <= time[i][1]:
                # the previous car will be able to catch up to this current car
                stack.pop()
                fleet -= 1

            stack.append(time[i])
        
        return fleet

