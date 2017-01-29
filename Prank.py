import os
def rename_files():
    #(1) get files names from a folder
    file_list = os.listdir("/Users/Subhankar29/Desktop/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("The working directory is:"+saved_path)
    os.chdir("/Users/Subhankar29/Desktop/prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)    

rename_files()    
    
