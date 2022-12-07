#even2.py
#HMWK_3

def chooseEven(nums):

    evens = []
    for x in nums:
        if x%2 == 0 :
            evens.append(x)
        else:
            pass
    print(evens)


def main():

    chooseEven([1,3,4,6,3,1,3,0,7])
    chooseEven([1,1,1,2,3,4,4,5,6])
    chooseEven([2,2,2,5,6,3,6,12,12])

main()
