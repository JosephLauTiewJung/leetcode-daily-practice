class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check the length first
        if len(s) != len(t): 
            return False
        # use dictionaries to record character mapping 
        s_to_t = {}
        t_to_s = {}
        # for each character pair in s and t, check for conflicts 
        for cs, ct in zip(s, t):
            # if cs already exists in the dictionary but the mapping is incorrect 
            if cs in s_to_t and s_to_t[cs] != ct: 
                return False 
            # check if ct -> cs
            if ct in t_to_s and t_to_s[ct] != cs: 
                return False
            # if no conflict save to the dictionaries
            s_to_t[cs] = ct
            t_to_s[ct] = cs
            # if the loop finish return True
        return True


if __name__ == '__main__': 
    solution = Solution()
    print(solution.isIsomorphic(s="egg", t="add"))