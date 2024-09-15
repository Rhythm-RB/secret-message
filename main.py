a = input("Enter whether you want to encrypt or decrypt your message: ")
message = input("Enter your message: ")
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def random():
    import random
    randomNumber =random.randint(0,25)
    return randomNumber

length = len(message)

if(a == "encrypt"):

    if(length >= 3):
        message = message[1:] + message[0]
        encryptedMessage = alphabets[random()] + alphabets[random()] +alphabets[random()] +message +alphabets[random()] +alphabets[random()] +alphabets[random()]
        print(encryptedMessage)
        
    else:
        print(message[::-1])


elif(a == "decrypt"):

    if(length >= 3):
        # removing first 3 letter
        message = message[3:length]

        # removing last 3 letter
        c = length - 6
        message = message[0:c]
        print(message)

        # removing last letter and adding in first
        message = message[c-1:c] + message[0:c-1]
        print(message)


    else:
        print(message[::-1])

