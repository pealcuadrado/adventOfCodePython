import sys
def main():
    ans = 0
    children = dict()
    values = dict()
    all_kids = set()
    total = set()
    lines=[]
    with open('data') as f:
        lines=f.readlines()
    for line in lines:
        a = list(line.replace(',','').strip().split())
        val = a[0]
        values[val] = int(a[1].replace('(','').replace(')',''))
        kids = a[3:]
        children[val] = kids
        total.add(val)
        for kid in kids:
            all_kids.add(kid)
    ans = (total - all_kids).pop()
    print ans

    def calc_kids_weights(root):
        kid_weights = []
        for kid in children[root]:
            kid_weights.append(calc_weight(kid))
        return kid_weights


    def check_bal(root):
        if children[root] == []:
            return True
        kid_weights = calc_kids_weights(root)
        return len(set(kid_weights)) == 1

    def unbalanced_kid(root):
        kid_weights = calc_kids_weights(root)
        for kid in children[root]:
            curr_weight = calc_weight(kid)
            if kid_weights.count(curr_weight) == 1:
                return kid

    def calc_weight(root):
        tot = values[root]
        for kid in children[root]:
            tot += calc_weight(kid)
        return tot

    ans_parent = ans
    while not check_bal(ans):
        ans_parent = ans
        ans = unbalanced_kid(ans)
    another_kid = children[ans_parent][0]
    if another_kid == ans:
        another_kid = children[ans_parent][1]
    print values[ans] - calc_weight(ans) + calc_weight(another_kid)

main()