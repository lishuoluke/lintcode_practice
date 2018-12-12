


def interval(start, end):
    interval.start = start
    interval.end = end

a = interval(1,2)
b = interval(3,4)

instancelist = [ interval(0,0) for i in range(2)]
instancelist[0]= a
instancelist[1]= b
print(instancelist)

def canAttendMeetings(self, intervals):
    # Write your code here
    #intervals.sort()
    for i in range (0,len(intervals)-1):
        print (intervals[i])
        #if (intervals[i].end > intervals[i+1].start):
         #   return False
    #return True

a = [(465,497),(386,462),(354,380),(134,189),(199,282),(18,104),(499,562),(4,14),(111,129),(292,345)]
canAttendMeetings(1,instancelist)
