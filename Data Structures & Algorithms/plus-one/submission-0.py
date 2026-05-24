class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # given a list
        # go through each item of that list
        # add that item to an empty string
        # convert that string to an int
        # add 1 to that int
        # now append each item of that int in a new list

        empty_string = ""

        for d in digits:
            empty_string += str(d)

        large_number = int(empty_string) + 1
        large_number_str = str(large_number)

        res = []
        for char in large_number_str:
            res.append(int(char))

        return res



        

        