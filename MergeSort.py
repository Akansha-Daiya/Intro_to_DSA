#User function Template for python3

class Solution:
    def merge(self,arr, low, mid, high):
        left = low
        right = mid+1
        lst = []
        while left <= mid and right<=high:
            if arr[left]<=arr[right]:
                lst.append(arr[left])
                left = left+1
            else:
                lst.append(arr[right])
                right = right +1
        while left<=mid:
            lst.append(arr[left])
            left = left+1
        while right<=high:
            lst.append(arr[right])
            right  = right + 1
        for i in range(low,high+1):
            arr[i] = lst[i-low]
            
    def mergeSort(self,arr, low, high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
obj=Solution() 
ar=[2,5,1,6,9]
e=len(ar)-1   
s=0     
obj.mergeSort(ar, s, e)
print(ar)