"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time: O(N + E)
        Space: O(N + E)
        """
        # make a dict to store preq, unlock_course_list, and init it
        # in_degree is a list that stores preq required to unlock a course
        course_dict = defaultdict(list)
        in_degree = [0] * numCourses
        for course, preq in prerequisites:
            course_dict[preq].append(course)
            in_degree[course] += 1
        # init a deque for running BFS
        # enque the valus in in_degree with 0, which means the starting point
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        # while queue
        while queue:
            # pop queue, add to set
            course = queue.pop()
            count += 1
            # get all siblings
            siblings = course_dict[course]
            # iterate all siblings, and add to queue
            for unlock_course in siblings:
                in_degree[unlock_course] -= 1
                if in_degree[unlock_course] == 0:
                    queue.appendleft(unlock_course)
        return count == numCourses