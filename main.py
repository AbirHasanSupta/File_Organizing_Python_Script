import os
import shutil
from datetime import datetime

def organize_files_by_month(src_dir):
    if not os.path.exists(src_dir):
        print(f"Directory '{src_dir}' does not exist.")
        return
    for file in os.listdir(src_dir):
        path = os.path.join(src_dir, file)
        if os.path.isfile(path):
            try:
                date = datetime.fromtimestamp(os.stat(path).st_mtime)
                folder_name = date.strftime('%B')
                folder_path = os.path.join(src_dir, folder_name)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                shutil.move(path, os.path.join(folder_path, file))
            except Exception as e:
                print(f"Error in {file}: {e}")
    print("Files have been organized successfully.")




if __name__ == "__main__":
    src = input("Enter the source path: ").strip()
    organize_files_by_month(src)