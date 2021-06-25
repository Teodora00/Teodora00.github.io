def my_reverse(l):
     rev_list = []
     length = len(l)
     s = length - 1
     while s >= 0:
         rev_list.append(l[s])
         s -= 1
     return print(rev_list)
         


my_reverse(['1','2','3'])