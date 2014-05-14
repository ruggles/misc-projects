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
    
    # If message isn't evenly divisible by len(key), pad it with X
    if len(message)%len(key) != 0:
        message += 'X'*(len(key) - len(message)%len(key))
        
    encodingGrid = buildGrid(message, len(key))
    
    encodedMessage = ''    
    # Reads each column up to down in order of the key.
    # i.e. if key is [1,3,2], read first column, then third, then second
    readKey = []
    for i in key:
        readKey.append(0)
        
    index = 0
    for j in key:
        readKey[j-1] = index + 1
        index += 1

    for j in readKey:
        for i in range(len(encodingGrid)):
            encodedMessage += encodingGrid[i][j - 1]
            
    return encodedMessage
    
def buildGrid(message, length):
    """
    Takes a message and an integer, and builds a list of strings 
    where each string is of that integer length. This makes
    it easily callable using grid[i][j] notation
    """
    assert type(length) == int and length > 0
    assert type(message) == str
    
    grid = []
    
    while len(message) > 0:
        grid.append(message[:length])
        message = message[length:]
        #print message, encodingGrid
        
    return grid
    
def inverseTranspose(encodedMessage, key):
    """
    Decodes a string which has been transposed using the given key.
    """
    assert type(message) == str
    assert type(key) == list
    
    decodingGrid = buildGrid(encodedMessage, len(encodedMessage)/len(key))
    
    decodedMessage = ''
    # Read decodingGrid column by column left to right
    # Read each character in column according to the order
    # in key. i.e. key = [1,3,2] Read first character, then
    # third character, then last.
    for j in range(len(encodedMessage)/len(key)):
        for i in key:
            decodedMessage += decodingGrid[i-1][j]
            
    return decodedMessage

# Quick Test
if __name__ == '__main__':    
    message = "Blue is a good dog."
    keys = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    print "Message: ", message
    
    for key in keys:
    
        encodedMessage = transpose(message, key)
        print "Key: ", key
        print "Encrypted Message: ", encodedMessage
        decodedMessage = inverseTranspose(encodedMessage, key)       
        print "Decrypted Message: ", decodedMessage
        
        if decodedMessage == "BLUEISAGOODDOGX":
            print "TEST PASSED"
        else:
            print "TEST FAILED"
        

    

