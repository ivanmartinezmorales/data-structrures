class Solution(object):
    '''
    First, turn the brick wall into a dictionary. When in a dictionary,
    We can analyze the length of the spaces, excluding the edges.
    
    Then for ever row, we will count the number of bricks. If there is a brick there
    We will append it to the brickDictionary. 
    '''
    def leastBricks(self, wall):
        brickDict = dict()
        
        for row in wall:
            spaceLength = 0
            
            for brick in row[:-1]:
                spaceLength += brick
                
                if spaceLength not in brickDict:
                    brickDict[spaceLength] = 1
                
                else:
                    brickDict[spaceLength] += 1
        max_value = 0
        for val in brickDict.values():
            max_value = max(max_value, val)
        return len(wall) - max_value
    
'''
here is the row 1:  [1, 2, 2, 1]
here is the row 2:  [3, 1, 2]
here is the row 3:  [1, 3, 2]
here is the row 4:  [2, 4]
here is the row 5:  [3, 1, 2]
here is the row 6:  [1, 3, 1, 1]


{1: 3, 2: 1, 3: 3, 4: 4, 5: 2}

length of the wall is 6 rows deep.


'''
