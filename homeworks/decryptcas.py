def chipper(plntxt, key):
    decoded=""
    for c in plntxt:
        nb=ord(c)-key
        wd=chr(nb)
        decoded+=str(wd)
    return decoded

def main():
    txt="kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    magicnumber=3
    decmes=chipper(txt,magicnumber)
    print(decmes)

if __name__=="__main__":
    main()