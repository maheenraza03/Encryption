# encryption.py
# Maheen Raza UCID: 30137445, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.




### Define your functions here

def valid_cipher(cipher_from_user):                     ## This function checks if the cipher the user has inputted is valid or not
    valid = True
    if len(cipher_from_user) == 26 and len(cipher_from_user) == len(set(cipher_from_user)):         ##this if statement check whether the length of the cipher matches the requirements and has unique letters/numbers
        valid = True                ## if it does meet the requirements, the boolean value will be true
    else:
        valid = False ## or else it'll be false
    return valid       ## returns whatever the boolean value is

    """
    Summary:
    Determines whether or not the the user's cipher that they have inputted is valid or not

    Parameters:
    cipher_from_user: string representing the cipher the user inputs

    Returns:
    valid: a variable which is made to store the boolean value if the user's cipher is valid or not


    """

def encoding_text(user_input, user_cipher):             ## the function will take input and a cipher from the user and change the input accordingly
    dict_to_encode = {'a': user_cipher[0], 'b': user_cipher[1], 'c': user_cipher[2], 'd': user_cipher[3], 'e': user_cipher[4], 'f': user_cipher[5], 'g': user_cipher[6], 'h': user_cipher[7], 'i': user_cipher[8], 'j': user_cipher[9], 'k': user_cipher[10], 'l': user_cipher[11], 'm': user_cipher[12], 'n': user_cipher[13], 'o': user_cipher[14], 'p': user_cipher[15], 'q': user_cipher[16], 'r': user_cipher[17], 's': user_cipher[18], 't': user_cipher[19], 'u': user_cipher[20], 'v': user_cipher[21], 'w': user_cipher[22], 'x': user_cipher[23], 'y': user_cipher[24], 'z': user_cipher[25]}
    user_output = ''                                    ## the dictionary maps every single letter of the alphabet to the elements in the cipher to produce the desired output
    for letter in user_input:                           ## this for loop goes through the letters/elements in the user's input and changes the value of the output to the corresponding cipher letter and the empty string saves the varibale so it can called outside of the for loop
        user_output = user_output + dict_to_encode[letter]

    return user_output                                  ## this statement returns the desired output once the for loop is excuted

    """
    Summary:
    if the user wants their text to be encoded, their inputs will be passed through this function so the user's text changes according to the cipher

    Parameters:
    user_input: string representing the text that the user wants to be encoded
    user_cipher: string representing the cipher that the user wants to be used so their text can be changed accordingly

    Returns:
    user_output: when the user's text is changed according to the cipher, the function will output the final result

    """


def decoding_text(input_user, cipher_user):     ## this function will decode the user's text according to the cipher
    dict_to_decode = {cipher_user[0] : 'a', cipher_user[1] : 'b', cipher_user[2] : 'c', cipher_user[3] : 'd', cipher_user[4] : 'e', cipher_user[5] : 'f', cipher_user[6] : 'g', cipher_user[7] : 'h', cipher_user[8] : 'i', cipher_user[9] : 'j', cipher_user[10] : 'k', cipher_user[11] : 'l', cipher_user[12] : 'm', cipher_user[13] : 'n', cipher_user[14] : 'o', cipher_user[15] : 'p', cipher_user[16] : 'q', cipher_user[17] : 'r', cipher_user[18] : 's', cipher_user[19] : 't', cipher_user[20] : 'u', cipher_user[21] : 'v', cipher_user[22] : 'w', cipher_user[23] : 'x', cipher_user[24] : 'y', cipher_user[25] : 'z'}
    user_output = ''                ## the dictionary maps every element of the cipher to the letters of the alphabet in order to decode the input and the empty string saves a variable so it can be called outside of the for loop
    for letter in input_user:       ## the for loop the goes through every letter of the input to change it to the letters of the alphabet
        user_output = user_output + dict_to_decode[letter]
    
    return user_output              ## the return then returns the input after its been decoded

    """
    Summary:
    If the user wants their input to be decoded, the following input and cipher will go through this function to get the desired output

    Parameters:
    input_user: string representing initial text that the user wants decoded
    cipher_user: string representing that the user has inputted that will translate the input accordingly

    Returns:
    user_output: this return returns the final desired output after changing the letters in the user's input to the cipher's letters and decoding the message

    """



print("ENDG 233 Encryption Program")                                                            ## this prints out the welcome message
choice_pick = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit:'))   ## this will print out asking for the user on their choice whether they want to decode, encode or exit

while choice_pick != 0:                                                                        ## the while loop is there to keep the program going until the user puts in 0 to quit the program
    if choice_pick == 1:                                                                        ## this if statement will execute if the user wants to encode
        text_to_encode = input('Please enter the text to be processed: ')                       ## the program will ask the user for the text to be processes and the cipher text
        cipher_input = input('Please enter the cipher text: ')
        if valid_cipher(cipher_input) == True:                                                  ## if the function valid_cipher returns a true statement, then the cipher is valid and it will print out the output
            print('Your cipher is valid')
            print('Your output is:', encoding_text(text_to_encode, cipher_input))
            choice_pick = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit:'))
        else:
            print('Your must contain 26 unique elements of a-z or 0-9.')                        ## if the cipher is not valid, the program will tell the user the reason and ask them to enter in new information again
            continue
    elif choice_pick == 2:                                                                      ## this else if statement will excute if the user wants to decode
        text_to_decode = input('Please enter the text to be processed: ')                       ## the program, again, will ask for the text and the cipher text
        user_cipher = input('Please enter the cipher text: ')
        if valid_cipher(user_cipher) == True:                                                   ## if the function valid_cipher returns a true statement, then the cipher is valid and it will print out the output
            print('Your cipher is valid')
            print('Your output is:', decoding_text(text_to_decode, user_cipher)) 
            choice_pick = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit:'))         
        else:
            print('Your must contain 26 unique elements of a-z or 0-9.')                        ## if the cipher is not valid, the program will tell the user the reason and ask them to enter in new information again
else:                                                                                           ## if the user choice is not any of the opitions the program will end
    exit

print('Thank you for using the encryption program.')                                            ## prints out the end message
 
