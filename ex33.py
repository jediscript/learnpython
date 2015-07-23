#i = 0
#numbers = []

#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)

#    i = i + 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i

#print "The numbers: "

#for num in numbers:
#    print num

def numLoops(n, inc):
    i = 0;
    numbers = [];
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
     
    return numbers

#nums = numLoops(8,2);

#for num in nums:
#    print num


def numLoopsFor(n, inc):
    i = 0
    numbers = []
    for i in range(0, n, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


numLoopsFor(20, 2)
