from turtle import pos
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_list = list()

        # Create set of all numbers
        potential_answer_set = set(nums)
        
        # Iterate over list and calculate the corresponding answers
        for position, value in enumerate(nums):
            answer = target - value

            if answer in potential_answer_set:
                # Solution found
                answer_list.append(position)
                second_position = nums.index(answer)
                answer_list.append(second_position)
        
        return answer_list
