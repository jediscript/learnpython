def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a/b

print "Let's do some math with just functions!"

real_age = float(raw_input("How old are you? "))
real_height = float(raw_input("How tall are you (cm)? "))
real_weight = float(raw_input("How much do you weigh(kg)? "))

age = add(real_age, 5)
height = substract(real_height, 4)
weight = multiply(real_weight, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
