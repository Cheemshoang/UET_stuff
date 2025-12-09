from typing import Dict, List
def check(d1: Dict, d2: Dict) -> Dict:
    ans = {}
    for k,v in d1.items():
        if k not in ans: ans[k] = v
        else: ans[k] += v
    for k,v in d2.items():
        if k not in ans: ans[k] = v
        else: ans[k] += v
    return dict(sorted(ans.items()))