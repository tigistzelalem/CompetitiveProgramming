class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:  
        index_map = {}
        min_index = float('inf')
        result = []

        for idx, word in enumerate(list1):
            index_map[word] = idx
        
        for idx, word in enumerate(list2):
            if word in index_map:
                current_idx = idx + index_map[word]

                if current_idx < min_index:
                    min_index = current_idx
                    result = [word]
                elif current_idx == min_index:
                    result.append(word)

        return result


        


            