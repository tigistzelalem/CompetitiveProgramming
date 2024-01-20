class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = defaultdict(int)
        count = 0

        for i in range(len(fruits)):
            basket[fruits[i]] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            count = max(count, i - left + 1)
        
        return count    

                


       





        