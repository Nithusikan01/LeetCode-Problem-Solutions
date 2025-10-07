class Solution(object):
    def getMedianOfTwoSortedArrays(self, nums1: list, nums2: list) -> float:
        """Brute Force Approach

        - merge the arrays into a single sorted array.
            -  Merge sort considering 2 arrays
             
        - get the size of the new array
            - if odd: index of median is (length + 1)/2
            - if even: average of middle and the next element.
        """

        result_arr = []
        i = 0 # nums1
        j = 0 # nums2

        # When both has numbers
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result_arr.append(nums1[i])
                i += 1
            else:
                result_arr.append(nums2[j])
                j += 1
        
        # When only nums1 has numbers
        while i < len(nums1):
            result_arr.append(nums1[i])
            i += 1

        # When only nums2 has numbers
        while j < len(nums2):
            result_arr.append(nums2[j])
            j += 1
        
        # Median
        n = len(result_arr)
        if n == 0:
            return None
        if n % 2 == 1:
            return float(result_arr[n // 2])
        else:
            return (result_arr[n // 2 - 1] + result_arr[n // 2]) / 2.0

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMedianOfTwoSortedArrays([1,2,3], [4,5,6]))
