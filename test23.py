#t = int(input())
t = 1
for i in range(t):
    #n = int(input())
    n = 6
    dict = {}
    dict["upper"] = []
    dict["lower"] = []
    dict["person"] = []
    dict["middle"] = []
    perss = ["mom", "dad", "quuenelizabeth", "chair", "unclebob", "giulia"]
    classes = ["upper-upper-lower-middle class", "middle-middle-middle-lower-middle class", "upper-upper-upper class", "lower-lower class", "middle-middle-lower-middle class", "middle-middle-lower-middle class"]

    for i in range(n):
        pers, clas = perss[i], classes[i]
        dict["upper"].append(clas.count("upper"))
        dict["lower"].append(clas.count("lower"))
        dict["middle"].append(clas.count("middle"))
        dict["person"].append(pers)
    
    sort_person = []
    for key in ["upper", "middle", "lower"]: 
        while sum(dict[key])!=0: 
            max_upper = max(dict[key])
            indexes = [i for i, v in enumerate(dict[key]) if v == max_upper]
            equivalent_people = [dict["person"][index] for index in indexes]
            equivalent_people.sort()
            for i in equivalent_people: sort_person.append(i)
            print("ho trovato i massimi ", equivalent_people)
            for key2 in ["upper", "middle", "lower", "person"]: 
                for i, index in enumerate(indexes): 
                    print("procedo a rimuoverli con indice ", index)
                    if i!=0: index -=1
                    dict[key2].pop(index)
                    
            
            print("----------------")
            print(dict)
    

    print(sort_person)

        
        