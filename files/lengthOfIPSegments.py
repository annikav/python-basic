ip = input("Enter an IP Address, or q to quit: ")
lenSegment = 0
numSegments = 1
while ip != 'q':
    print("ip is:" + ip)
    for char in ip:
        if char == '.':
            print("length of segment {0}: {1}".format(numSegments,str(lenSegment)))
            numSegments += 1
            lenSegment = 0
        else:
            lenSegment += 1
    print("length of segment {0}: {1}".format(numSegments,str(lenSegment)))
    print("number of segments:" + str(numSegments))
    ip = input("Enter an IP Address, or q to quit: ")
