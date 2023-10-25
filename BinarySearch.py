def binarySearch(list,num,start,end):
    if start == end:
        if(list[start]== num):
            return start
        else:
            return -1
    
    else:
        start = 0
        end = len(list) - 1
        mid = int((start + end)/2)
        if(list[mid] == num):
            return mid
        elif(num < list[mid]):
            return binarySearch(list,num,start,mid-1)
        else:
            return binarySearch(list,num,mid+1,end)
    
        
l = [10,20,30,40,60]
n = int(input('Enter the number: '))

index = binarySearch(l, n, 0, len(l) - 1)
if index == -1:
    print(x, 'not found')
else:
    print(x, ' is found in', index+1)