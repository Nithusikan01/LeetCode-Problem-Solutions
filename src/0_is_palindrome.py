class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)


        limit = len(num_str)//2
        for i in range(limit):
            if num_str[i] != num_str[-(i+1)]:
                return False
        return True

    def isPalindrome2(self, x):
            """
            :type x: int
            :rtype: bool
            """
            num_str = str(x)
            # rv_num_str=""

            # for i in range(len(num_str)):
            #     rv_num_str += num_str[len(num_str) - (i + 1)]
            
            rv_num_str = num_str[::-1]
            if num_str == rv_num_str:
                return True
            else:
                return False