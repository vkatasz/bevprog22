def decoder(plntxt, key):
    decodedtxt=""
    for c in plntxt:
        if c.isalpha():
            if c.isupper():
                if (ord(c)>26):
                    nb=(ord(c)+key)%ord('Z')-26
                    decodedtxt+=chr(nb)
                else:
                    nb=(ord(c)+key)%ord('Z')
                    decodedtxt+=chr(nb)
            else:
                # nb=(ord(c)+key)%ord('z')
                # decodedtxt+=chr(nb)
                if (ord(c)>26):
                    nb=(ord(c)+key)%ord('z')-26
                    decodedtxt+=chr(nb)
                else:
                    nb=(ord(c)+key)%ord('z')
                    decodedtxt+=chr(nb)
        else:
            decodedtxt+=c
    return decodedtxt

def main():
    text=open("codedmessage.txt","r")
    textli=text.readlines()
    magicnumber=2
    for e in textli:
        decmes=decoder(e,magicnumber)
        print(decmes)

if __name__=="__main__":
    main()