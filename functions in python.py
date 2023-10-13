manager =[34,23,76,87]
developer =[32,12,65,43,87]
support_staff =[12,7,5,8,9,3,10]
def get_avg(arr):
    n=len(arr)
    sum=0
    for i in range (0,n):
        sum =sum+arr[i]
        return sum/n
    print('manager avg:',get_avg(manager))
    print('developer avg:',get_avg(developer))
    print('support staff avg:',get_avg(support_staff))
