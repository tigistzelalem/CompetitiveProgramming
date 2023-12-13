class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # create dict to store the freq of domains
        counts = defaultdict(int)
        for domain in cpdomains:
            # split the list by space to separate the freq and the domains
            freq, splittedDomains = domain.split()
            # split the domains from the above split to get the sub  domains
            subDomains = splittedDomains.split('.')
            one = '.'.join(subDomains)
            two = '.'.join(subDomains[1:])
            # count the freq os each subdomains
            counts[one] += int(freq)
            counts[two] += int(freq)

            # check if we have three subdomains 
            if len(subDomains) == 3:
                three = subDomains[2]
                counts[three] += int(freq)
        result = [f"{val} {key}" for key, val in counts.items()]

        return result
