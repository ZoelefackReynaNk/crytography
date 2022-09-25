import math
while True:
    opt= input("Operation [Encipher/Decipher]?  :")
    if opt == "Encipher" or opt == "encipher":
        #different inputs necessary for encryption.
        k = int(input("enter the key: "))
        l = int(input("enter lambda: "))
        txt = input("enter the text to be encrypted: ")
    
        plane_text = txt.lower()
        print("plane text is: ", txt, "\n")
        print("plane text without capitals: ", plane_text, "\n")
    
        # loop to decompose plane text into a list of letters and alphabet
        list = []
        i = 97
        while i < 123:
            d = chr(i)
            list.append(d)
            i += 1
        print("small case: ", list)
    
        # loop to create a list of capital letters for encryption
        l_c = []
        i = 65
        while i < 91:
            d = chr(i)
            l_c.append(d)
            i += 1
        print("capitals: ", l_c)
    
        #loop to remove all punctuations
        t_l = []
        for x in plane_text:
            if (x == " " or x == "," or x == "." or x == "!" or x == "?" or x == "(" or x == ")"):
                continue
            else:
                t_l.append(x)
        print("text without punctuation: ", t_l, "\n\n")
        
        #loop to bring out the encrypted text using affine cipher
        cipher_text = []
        for t in t_l:
            x = (l*list.index(t) + k) % 26
            cipher_text.append(l_c[x])
        print("cipher text is: ", cipher_text, "\n\n")
    
        #loop to print out cipher text to screen.
        print("Cipher Text: ")
        for i in cipher_text:
            print(i, end = " ")
        print("\n")
    elif (opt == "Decipher" or opt == "decipher"):
        text = input("Cipher text:")
        ctext = text.upper()
        y = int(input("enter lambda: "))
        I = int(input("inverse of lambda: "))
        k = int(input("enter key: "))
        list = []
        for x in ctext:
            list.append(x)
        charac = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", ";", ":"]
        d = 0
        for x in charac:
            if x in list:
                d = d + 1
        if d == 0:
            # loop to decompose cipher text into a list of letters and alphabet
            lc = []
            i = 97
            while i < 123:
                d = chr(i)
                lc.append(d)
                i += 1
            print("small case: ", list)
            # loop to create a list of capital letters for encryption
            uc = []
            i = 65
            while i < 91:
                d = chr(i)
                uc.append(d)
                i += 1

            if (math.gcd(y, k) == 1) and (I * y % 26 == 1):
                dtext = []
                for t in list:
                    x = (I * uc.index(t) + y) % 26
                    dtext.append(lc[x])
                print("\n deciphered text is: ")
                for i in dtext:
                    print(i, end=" ")
                print("\n")
            else:
                print("lambda is not coprime to 26")

        else:
            print(list)
            print("re-enter text.")
    else:
        print("error re-enter operation")
