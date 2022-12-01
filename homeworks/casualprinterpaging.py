def main():
    try:
        nyomtatando=input("add meg melyik oldalakat szeretnéd kinyomtatni: a -> ha 1-4, b -> ha 7, c -> ha 9, d -> ha 11-15: ")
        if nyomtatando=='a':
            printing=[1,2,3,4]
        elif nyomtatando=='b':
            printing=[7]
        elif nyomtatando=='c':
            printing=[9]
        elif nyomtatando=='d':
            printing=[11,12,13,14,15]
        else:
            print("nincs ilyen opció!")
        print(printing)
    except ValueError:
        print("ismeretlen input..")
    except KeyboardInterrupt:
        print("I'm heading out")
    except KeyError:
        print("Invalid input")
    except:
        print("engedd el...")

if __name__=="__main__":
    main()