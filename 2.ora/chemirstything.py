def main():
    hydrogen=int(input("Hydrogen: "))
    oxygen=int(input("Oxygen: "))
    h2o=0
    excessOxygen=0
    excessHydrogen=0

    if hydrogen==oxygen*2:
        h2o=oxygen*2

    elif hydrogen>oxygen*2:
        h2o=oxygen*2
        excessHydrogen=(hydrogen-oxygen)*2
    
    else:
        h2o=hydrogen
        excessOxygen=oxygen*2-hydrogen

    print("Létrejött víz: {0},\nmaradék hidrogénatom: {1},\nmaradék oxigénatom: {2}".format(h2o, excessHydrogen, excessOxygen))

if __name__=="__main__":
    main()