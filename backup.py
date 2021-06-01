import os

bootsector = "00100000"

# 512 * 4 --> 2048
def size_of_clusters_in_bytes():
    # Size of clusters = Bytes per sector * Sectors per cluster
    bytes_per_sector = int(input('Bytes per sector? '))
    sectors_per_cluster = int(input('Sectors per cluster? '))
    return bytes_per_sector * sectors_per_cluster

def First_FAT_Address():
    Reserved_sectors_from_the_start_of_the_volume = int(input('Reserved sectors from the start of the volume? '))
    Bytes_per_sector = int(input("Bytes per sector"))
    Boot_Sector_Address  = str(input("Boot Sector Address"))
    return hex((Bytes_per_sector * Reserved_sectors_from_the_start_of_the_volume) + int(Boot_Sector_Address, 16))

def Size_Of_FAT_In_Bytes():
    # Size Of FAT In Bytes = FATs
    bytes_per_sector = int(input('Bytes per sector? '))
    fat_copies = int(input("Number of FAT copies?"))
    sectors_per_fat = int(input('Sectors per FAT? '))
    return (fat_copies) * bytes_per_sector * sectors_per_fat

def Root_Directory_Address():
    first_FAT_address = str(input('First FAT Address? '))
    size_of_FAT_in_bytes = int(input('Size of FAT In Bytes? '))
    return hex(int(first_FAT_address, 16) + size_of_FAT_in_bytes)

def Root_Directory_Size_In_Bytes():
    number_possible_root_entries = int(input("Number possible root entries?"))
    return number_possible_root_entries * 32


def Data_Region_Address():
    first_FAT_address = str(input('Root Directory Address? '))
    size_of_FAT_in_bytes = int(input('Root Directory size in Bytes? '))
    return hex(int(first_FAT_address, 16) + size_of_FAT_in_bytes)


def Total_Size_of_FAT16_Volume_In_Bytes():
    bytes_per_sector = int(input('Bytes per sector? '))
    small_numbers_of_sectors = int(input("Small numbers of sectors"))
    return small_numbers_of_sectors * bytes_per_sector



#def select_option():
def print_results(bootsector, size_cluster_bytes, first_fat_addr):
    #Print the results
    print('-------- Results --------')
    print('Boot Sector : ', bootsector)
    print('Size of Cluster in Bytes : ', size_cluster_bytes)
    print('First FAT Address : ', first_fat_addr)
    print('Size of FAT in Bytes : ', )
    print('Root Directory Address : ')

#print_results(bootsector(), size_of_clusters_in_bytes(), First_FAT_Address())

print("Doe eerst de boot sector oefening, die waarde heb je nodig om de disk layout te berekenen via deze tool. De startlijn is 0x100000")
input("Press any key to continue")
print(str(Total_Size_of_FAT16_Volume_In_Bytes()))