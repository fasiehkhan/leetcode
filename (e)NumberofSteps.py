class Solution(object):
    def numberOfSteps (self, num):
      
        steps = 0;
        while(num!=0):
            if( num % 2 == 0):
                num = num / 2;
            elif(num % 2 != 0):
                num = num - 1
            steps+=1
        return steps
