# N spare products  of various products,separate and group by product
# product can have multile spare parts
# same  letter code ,rearranged in all possiblities belong to a productcccccbefeuktgrjggfgnluffikkvhtgiufbibdefikvk
# prints the list after grouping them and printing in ascending order


def hist_simple(strseq: str):
    hist_stor = {}  # {a:2,b:2}
    resultstr = ''
    for each in [*strseq]:
        if hist_stor.__contains__(each):
            hist_stor[each] = hist_stor[each] + 1
        else:
            hist_stor[each] = 1
    for each in sorted(hist_stor):
        resultstr += each + str(hist_stor[each])
    return resultstr


if __name__ == '__main__':

    N_part = ['abba', 'baba', 'cata', 'data', 'tada','aaaa','bbbb','aaada','daaaa']
    result_dict = {}
    for each in N_part:
        result_dict[each] = hist_simple(each)

    finalresult = {} # (unique product key,[list of spare parts])
    for each in result_dict:
        key = result_dict[each]
        if finalresult.__contains__(key):
            finalresult[key].append(each)
            finalresult[key].sort()
        else:
            finalresult[key] = [each]

    print(sorted(finalresult.values()))


