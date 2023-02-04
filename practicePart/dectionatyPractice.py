import re


chessData ={'1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
'2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
'3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
'4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': 'wpawn', '6b': 'wpawn', '6c': 'wpawn', '6d': 'wpawn', '6e': 'wpawn', '6f': 'wpawn', '6g': 'wpawn', '6h': 'wpawn',
'7a': 'wrook', '7b': 'wknight', '7c': 'wbishop', '7d': 'wqueen', '7e': 'wking', '7f': 'wbishop', '7g': 'wknight', '7h': 'wrook'}
# print(chessData.values())

def checkFirstLetter(dictionary):
    pattern = re.compile("^[wb](pawn|knight|bishop|rook|queen|king)$")
    for piece in dictionary.values():
        if piece != '':
            if not pattern.match(piece):
                return False
    return True

def checkKings(dictionary):
    dic_to_check = {'w':0,'b':0}
    for word in dictionary.values():
        if word.startswith('w') and word.endswith('king'):
            dic_to_check['w'] += 1
        if word.startswith('b') and word.endswith('king'):
            dic_to_check['b'] += 1
    if dic_to_check['w'] == 1 and dic_to_check['b'] == 1:
        return True
    else:
        if dic_to_check['w'] != 1:
            print('Please check the Withe king.') 
        if dic_to_check['b'] != 1:
            print('Please check the black king .')
        return False

def checkPiecesNumber(dictionary):
    dic_to_check = {'w':0,'b':0}
    for value in dictionary.values():
        if value.startswith('b'):
            dic_to_check['b'] += 1
        elif value.startswith('w'):
            dic_to_check['w'] += 1
    if dic_to_check['w'] > 16 or dic_to_check['b'] > 16:
        print('Please check the Pieces number.') 
        return False
    return True

def checkPawns(dictionary):
    dic_to_check = {'w':0,'b':0}
    for word in dictionary.values():
        if word.startswith('wp'):
            dic_to_check['w'] += 1
        if word.startswith('bp'):
            dic_to_check['b'] += 1
        if dic_to_check['w'] > 8 or dic_to_check['b'] > 8: 
            print('Please check the the pawns Number.')
            return False
    return True
        
def checkValidPlaces(dictionary):
    pattern = re.compile("^[1-8][a-h]$")
    for key in dictionary.keys():
        if not pattern.match(key):
            print(key)
            print('check one of your chess places Please !!')
            return False
        else:
            return True

def isValidChessBoard(chessBoard):
    if checkFirstLetter(chessBoard):
        if checkKings(chessBoard):
            if checkPiecesNumber(chessBoard):
                if checkPawns(chessBoard):
                    if checkValidPlaces(chessBoard):
                        print('your chess board is valid to use')
    else :
        print('piece names begin with either a \'w\' or \'b\', Please make sure to check that on your board')            
        return False

isValidChessBoard(chessData)