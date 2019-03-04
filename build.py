from zipfile import ZipFile
import os

if __name__ == "__main__":
    folder_name = "StackAtNight.zip"
    file_paths = ["manifest.json", "night.css"]
    with ZipFile('src\\' + folder_name,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  
    print("File succesfullly built")
    print('\t' + os.path.abspath(os.getcwd()) + "src\\")