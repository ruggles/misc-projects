# pro/g/ramming challenge #29
# Create a double transposition cipher
# encoder/decoder

# Simply put, Colimnar transposition is accomplished
# by writing your text as a series of columns, 
# then rearrange the columns and read those off row
# by row to get the encrypted message

def stringFilter(string):
    """
    Take a string, remove all non-alphanumeric characters,
    and return the upper case.
    """
    assert type(string) == str
    
    filteredString = ''
    for char in string:
        if char.isalnum():
            filteredString += char
    
    return filteredString.upper()
    
def transpose(message, key):
    """
    Takes a message and applies the transposition
    cipher according to the key
    
    message: a string containing the text to be encoded or decoded
    key: a list of containing the order of the columns,
    i.e. [3, 5, 1, 4, 2] tells us to put the third
    column in the first place, the fifth column in the 
    second place, etc.
    """
    assert type(message) == str
    assert type(key) == list
    
    message = stringFilter(message)
    
    """
    Convert message into a list of strings, where
    each string is of length len(key)
    
    Each letter should be callable using grid[i][j] 
    notation, where sequentially calling grid[i]
    will reconstruct the original string
    
    Then build a new string by calling grid[i][j] where
    j is called in the order of the key for each i. 
    """
    
    if len(message)%len(key) != 0:
        message += 'X'*(len(key) - len(message)%len(key))
        
    encodingGrid = buildGrid(message, len(key))
    
    encodedMessage = ''    
    for j in key:
        for i in range(len(encodingGrid)):
            encodedMessage += encodingGrid[i][j-1]
            
    return encodedMessage
    
def buildGrid(message, length):
    """
    Takes a message and an integer, and builds a list of strings 
    where each string is of that integer length. This makes
    it easily callable using grid[i][j] notation
    """
    
    encodingGrid = []
    
    while len(message) > 0:
        encodingGrid.append(message[:length])
        message = message[length:]
        
    return encodingGrid

# Quick Example
if __name__ == '__main__':    
    message = "Blue is a good dog."
    key = [1,3,2]
    print message
    print key
    print transpose(message, key)
    

