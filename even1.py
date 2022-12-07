#even1.py
#HMWK_3

def printeven(nums):
    for x in nums:
        if x%2 == 0 :
            print(x)
        else:
            pass


def main():

    printeven([1,3,4,6,3,1,3,0,7])
    printeven([1,1,1,2,3,4,4,5,6])
    printeven([2,2,2,5,6,3,6,12,12])

main()
