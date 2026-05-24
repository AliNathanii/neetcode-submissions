class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """We wanna return the order of courses! It is possible
        that we dont take all courses given the prereqs"""
        # this problem teaches you Topological Sort

        # To build the ajacency list we use a Hashmap:
        prereq = {c: [] for c in range(numCourses)}  # each course c is initially mapped to an empty list []
        for crs, pre in prerequisites:
            prereq[crs].append(pre)  # for the key course (crs), append to its value list the current prereq we are at
        

        output = []
        visit, cycle = set(), set()

        def dfs(crs):  # pass in the course number we are currently visiting
            if crs in cycle:  # if a course is in cycle meaning an endless loop and we return False
                return False
            if crs in visit:  # no need to return a course twice
                return True

            cycle.add(crs)  # wanna know if in case we see it again...
            # now go through all prereqs in our current course, like this:
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False  # cycle detected! If returns True we let it keep going
                
            cycle.remove(crs)  # no longer along the path we are going so we can remove it
            visit.add(crs)  # since we just visited this course add it to our visited set
            output.append(crs)  # add it to our output now!
            return True
        

        # now we just need to run dfs on every single course
        for c in range(numCourses):
            if dfs(c) == False:
                return []  # if any of the above dfs call return False, we are forced to return an empty list [] (we dont return the output)
        return output  # if the abovc for loop ends, never returning [] meaning we never got False and then can go ahead and return the output

