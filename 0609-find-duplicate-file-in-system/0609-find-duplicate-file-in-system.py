class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for path in paths:
            values = path.split(" ")
            for i in range(1, len(values)):
                name_cont = values[i].split("(")
                name_cont[1] = name_cont[1].replace(")", "")
                map[name_cont[1]].append(values[0] + "/" + name_cont[0])

        res = []
        for key in map:
            if len(map[key]) > 1:
                res.append(map[key])

        return res