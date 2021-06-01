def main():
    bootsector = "00100000"
    bytes_per_sector = int(input("Bytes per sector? "))
    sectors_per_cluster = int(input("Sectors per cluster? "))
    reserved_sectors_from_the_start_of_the_volume = int(input("Reserved sectors from the start of the volume? "))
    number_possible_root_entries = int(input("Number possible root entries? "))
    small_numbers_of_sectors = int(input("Small numbers of sectors? "))
    sectors_per_fat = int(input("Sectors per FAT? "))
    fat_count = int(input("How many FAT's? "))

    #Disk Layout
    size_of_clusters_in_bytes = bytes_per_sector * sectors_per_cluster
    first_fat_address = hex((bytes_per_sector * reserved_sectors_from_the_start_of_the_volume) + int(bootsector, 16))
    size_of_fat_in_bytes = bytes_per_sector * sectors_per_fat
    root_directory_address = hex(int(first_fat_address, 16) + size_of_fat_in_bytes * fat_count)
    root_directory_size_in_bytes = number_possible_root_entries * 32
    data_region_address = hex(int(root_directory_address, 16) + root_directory_size_in_bytes)
    total_size_of_fat16_volume_in_bytes = small_numbers_of_sectors * bytes_per_sector

    print('-------- Results --------')
    print('Boot Sector : ', bootsector)
    print('Size of Cluster in Bytes : ', size_of_clusters_in_bytes)
    print('First FAT Address : ', first_fat_address)
    print('Size of FAT in Bytes : ',  size_of_fat_in_bytes)
    print('Root Directory Address : ', root_directory_address)
    print('Root Directory Size in Bytes : ', root_directory_size_in_bytes)
    print('Data Region Address : ', data_region_address)
    print('Total Size of FAT16 Volume in Bytes : ', total_size_of_fat16_volume_in_bytes)

print("Doe eerst de boot sector oefening, die waarde heb je nodig om de disk layout te berekenen via deze tool. De startlijn is 0x100000")
input("Press any key to continue")
main()