class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # second item from the pair list is the PreReq for the first item!!
        # use PreMap a map that will store course (first item in the list) and its prereqs as the value of each key
        # Then we will run DFS on every single node in the order from 0 to n - 1

        # for every course map it to an empty list, empty list will contain the prerequistes -- python syntax for that!
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:  # [crs, pre] this is how the given prerequisites list is structured
            preMap[crs].append(pre)
        
        # visitset will tell us if there is a cycle or loop as it cannot contain copies
        visitSet = set()
        def dfs(crs):
            # base case:
            if crs in visitSet:
                return False  # endless loop
            if preMap[crs] == []:
                return True  # this particulat crs has no prereqs so we can return True already!
            
            # if none of the above statements' conditions met, means we can add it in our visitSet and run recursive calls to the courses in this crs
            visitSet.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:  # if even one course returns False, we can 
                    return False  # return False for all of them!
            
            visitSet.remove(crs)  # we will also remove it from our visited set
            preMap[crs] = []  # since this course can be taken we can make its value in the map an empty list []
            return True  # if above dfs(pre) never returns False at any point, meaning this given course can be taken!

            # End of dfs function, only need to call it now!

        # But we need to call this function for each and every single course in the number of courses that we have

        for crs in range(numCourses):
            if dfs(crs) == False:  # or if not dfs(crs): return False
                return False
        return True