#start_of_data_region + cluster_size * (cluster_index - 2)

def contentscript():
    start_of_data_region = int(input("start of data region?"), 16)
    cluster_size = int(input("cluster size?"))
    cluster_index = int(input("cluster index?"))
    return "het antwoord staat op dit adress: " + hex(start_of_data_region + cluster_size * (cluster_index - 2))

print(contentscript())
#00108000
#2048
#3374/Users/gregreynders/PycharmProjects/FAT16
#3439

