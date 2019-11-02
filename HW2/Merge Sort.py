def MergeSort(list):
    if len(list) <= 1:
        return list
    else:
        left=[]
        right=[]
        n=0
        for i in list:
            list[n]=i
            if n < (len(list)/2):
                left.append(i)
                n+=1
                
            elif n >= (len(list)/2):
                right.append(i)
                n+=1
    left=MergeSort(left)
    right=MergeSort(right)
    return merge(list,left,right)


def merge(list,left,right):
    j=0
    p=0
    q=0
    while p <len(left) and q<len(right):
        if left[p] < right[q]:
            list[j] =left[p]
            p+=1
               
        elif left[p] >= right[q]:
            list[j] =right[q]
            q+=1
        j+=1
    while p <len(left):
        list[j] =left[p]
        p+=1
        j+=1
    while  q<len(right):
        list[j] =right[q]
        q+=1
        j+=1

    return list

list=[4,5,8,3,7,2,9,1]
MergeSort(list)

