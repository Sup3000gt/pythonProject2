# size = int(input())
# lst = input().split()
# for i in lst:
#     i = int(i)
lst = ["8","6","7","7","7","7","5","3","4","9"]
save = lst.copy()
def countNum(a_list):
    count = 0
    while len(lst) >0:
        if lst[0] == max(lst):
            lst.pop(0)
            count += 1
        else:
        # while lst[0] != max(lst):
            sublist = []
            a = lst[0]
            sublist.append(a)
            lst.pop(0)
            ind = [ ]
            for j in range(len(lst)):
                if lst[j] > a:
                    sublist.append(lst[j])
                    a = lst[j]
                    ind.append(j)
            # print(sublist)
            count += 1
            rem = ind[::-1]
            for each in rem:
                lst.remove(lst[each])
            # print(lst)
    print(count)
countNum(lst)

def countsub(a_list):
    while len(save) >0:
        if save[0] == max(save):
            print(save.pop(0))
        else:
            sublist2 = []
            a = save[0]
            sublist2.append(a)
            save.pop(0)
            ind = [ ]
            for j in range(len(save)):
                if save[j] > a:
                    sublist2.append(save[j])
                    a = save[j]
                    ind.append(j)
            sequen = " ".join(sublist2)
            print(sequen)
            rem = ind[::-1]
            for each in rem:
                save.remove(save[each])
countsub(save)

