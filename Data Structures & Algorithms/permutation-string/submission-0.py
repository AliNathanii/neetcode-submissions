class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Lengths of the two input strings
        n1 = len(s1)
        n2 = len(s2)

        # If s1 is longer than s2, it is impossible for s1 to be a permutation of any substring of s2
        if n1 > n2:
            return False

        # Initialize frequency counters for s1 and the first n1 characters of s2
        s1_counts = [0] * 26  # Frequency counter for characters in s1
        s2_counts = [0] * 26  # Frequency counter for the first window of characters in s2

        # Count the frequency of each character in s1 and the first n1 characters of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1  # Update count for s1
            s2_counts[ord(s2[i]) - ord('a')] += 1  # Update count for s2

        # If the initial window matches the frequency counts of s1, return True
        if s1_counts == s2_counts:
            return True

        # Slide the window across s2. This is where a sliding window is used!
        for i in range(n1, n2):
            # Include the next character in the window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            # Exclude the character that is no longer in the window
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1
            # Check if the current window matches the frequency counts of s1
            if s1_counts == s2_counts:
                return True

        # If no matching window is found, return False
        return False

