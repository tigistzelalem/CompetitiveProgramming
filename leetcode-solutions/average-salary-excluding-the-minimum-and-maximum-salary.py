class Solution:
    def average(self, salary: List[int]) -> float:
        sum_ = sum(salary)
        min_ = min(salary)
        max_ = max(salary)
        new_salary = sum_ - min_ - max_
        len_salary = len(salary) - 2

        return new_salary / len_salary