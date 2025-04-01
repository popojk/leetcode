"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict, deque
from typing import List


class DFSSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.
        Space Complexity: O(V + E) the adjacency list dominates our memory usage.
        """
        req_list = [[] for _ in range(numCourses)]
        # build the course - prerequisites list first
        for course, pre_req in prerequisites:
            req_list[course].append(pre_req)

        # make a list to record the state of each course
        # 0 - not visited
        # -1 - visited and cycle found
        # 1 - visited and no cycle found  
        states = [0 for _ in range(numCourses)]
        def has_cycle(v: int):
            # if course visited with no cycle, just pass
            if states[v] == 1:
                return False
            # found cycle, return True
            if states[v] == -1:
                return True
            
            states[v] = -1
            for pre_req in req_list[v]:
                if has_cycle(pre_req):
                    return True
            
            states[v] = 1
            return False


        # traverse all courses and make sure whether there is a cycle
        for v in range(numCourses):
            if has_cycle(v):
                return False
        return True

class BFSSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.
        Space Complexity: O(V + E) the adjacency list dominates our memory usage.
        """
        relation = defaultdict(list)
        in_degree = defaultdict(int)

        # make relation first
        for course, pre_req in prerequisites:
            relation[pre_req].append(course)
            in_degree[course] += 1

        bfs_q = deque()
        complete_count = 0
        for v in range(numCourses):
            if in_degree[v] == 0:
                bfs_q.append(v)

        while bfs_q:
            cur_course = bfs_q.popleft()
            complete_count += 1

            for course in relation[cur_course]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    bfs_q.append(course)
        return complete_count == numCourses
