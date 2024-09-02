import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i: set() for i in range(numCourses)}
        graph = collections.defaultdict(set)

        for i, j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)

        # find start location
        q = collections.deque([])
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
        # taken used to record taken courses
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for cor in graph[course]:
                preq[cor].remove(course)
                if not preq[cor]:
                    q.append(cor)
        return []
