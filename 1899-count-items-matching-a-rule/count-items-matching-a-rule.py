class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            idx=0
        elif ruleKey=="color":
            idx=1
        else:
            idx=2
        c=0
        for i in range(len(items)):
            if items[i][idx]==ruleValue:
                c=c+1
        return c