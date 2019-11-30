def rotate_array( arr , n ):
    for i in range(0,n):
        first = arr[0]
        for j in range(0,len(arr) - 1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = first



def vignette_encrypt (message, key, mode):
    
    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 
    alphabet_ordered = characters.copy()
    message_characters = list(message.upper())
    encrypted_message = ''
    key_index = 0



    for character in message_characters :

        if ( character not in characters ):
            encrypted_message += character
            continue
        if ( key_index >= len(key)):
            key_index=0

        key_character = key[key_index]
        n = key.index(key_character) + 1
        
        key_index += 1
        
        rotate_array (characters, n )
        
        if ( mode == 'e'):
            index = alphabet_ordered.index(character)
            encrypted_message += characters[index]
        elif ( mode == 'd'):
            index = characters.index(character)
            encrypted_message += alphabet_ordered[index]
        else :
            return 'INVALID MODE'

        
        alphabet = alphabet_ordered

    return encrypted_message


while True :
    mode = input("[e]ncrypt or [d]ecrypt: ")
    messageMode =  "plaintext" if mode == 'e' else "ciphertext"
    message = input ("Enter your {0}:".format(messageMode))
    if (message == '' ):
        break
    key = input("Enter your key: ")
    if (key == ''):
        print('Must have a key of atleast one valid charater')

    answerText = "Encrypted version of your personal message:" if mode == 'e' else "Encrypted message says: "
    print (answerText)
    print (vignette_encrypt(message,key, mode))
    print ('')
    
