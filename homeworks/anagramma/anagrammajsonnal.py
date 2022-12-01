import json

def main():
    ops=open("anagrammak.json",'r')
    sablon=json.load(ops)
    anagrammae=input("adj meg egy stringet: ")

    if sablon[anagrammae]:
        print(sablon[anagrammae])
    else:
        print("nem anagramma :(")

if __name__=="__main__":
    main()