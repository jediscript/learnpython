from sys import exit


def pci_room():
    print "You waked up inside a room with a logo that says PCI."
    print "There is a Peso Monster inside, that asks: why are you here?"
    print "There is no wrong answer but every answer has a consequence. Get rich or die trying!"

    while True:
        answer = raw_input('> ')
        goodthings = ["learn", "learning", "study", "train", "training"]
        badthings = ["money", "career", "revenge", "rich", "die", "kill", "punch", "kick"]

        # loop inside the answer and check if the keyword is there
        answer = answer.lower()
        for word in answer.split():
            if word in goodthings:
                print "\r\n"
                print "Good, you have a vision in life. You may pass."
                nova_room()
            elif word in badthings:
                print "\r\n"
                print "You are corrupted. Die now!!!"
                killed()
            else:
                print "\r\n"
                print "I have no idea why you are here. You want to die?"


def nova_room():
    print "\r\n"
    print 'You entered another room. A sign says "Nova Seekers, still looking for a Nova"'
    print "A Euro Monster appears!"
    print "GRRR!!! Who dares disturb my sleeps?!"
    print "Anyone who enters must answer my riddle or die!"
    print "A git commit was not committed by a developer who merge a branch from a different remote repository. The remote commits was done by the Interns. Who takes the blame if an error is found, and a user was unable to see the footer?"

    correct = False

    while True:
        answer = raw_input('Developer, Interns, Manager, BA, PNoy, God > ')
        answer = answer.lower()

    correct = switch(answer)

    if correct:
        print "\r\n"
        print "You are correct, the answer is %r." % answer
        print "You may pass!"
        usap_room()
    else:
        print "\r\n"
        print "One miss, you die |3!+(#!"
        killed()


def usap_room():
    print "\r\n"
    print "To be continued..."
    exit(0)


def killed():
    print "\r\n"
    print "**A LOUD AND FAST SLASHING SOUND**"
    print "You die in vain. Never realizing your full potential..."
    exit(0)


def switch(case):
    return {
      'developer': True,
      'interns': False,
      'manager': False,
      'ba': False,
      'pnoy': True,
      'god': False
    }.get(case, False)


# start program
pci_room()
