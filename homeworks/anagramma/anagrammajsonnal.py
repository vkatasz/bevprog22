import json

def main():
    try:
        ops=open("anagrammak.json",'r')
        sablon=json.load(ops)
        anagrammae=input("adj meg egy stringet: ")

        if sablon[anagrammae]:
            print(sablon[anagrammae])
        else:
            pass
        
    except KeyError:
        print("engedd el...")

if __name__=="__main__":
    main()