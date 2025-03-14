import os
import shutil
from datetime import datetime


def week_of_month_extract(date):
    first_day = date.replace(day=1)
    return (date.day + first_day.weekday()) // 7 + 1


def organize_files_by_month(src_dir, timeframe):
    if not os.path.exists(src_dir):
        print(f"Directory '{src_dir}' does not exist.")
        return
    for file in os.listdir(src_dir):
        path = os.path.join(src_dir, file)
        if os.path.isfile(path):
            try:
                date = datetime.fromtimestamp(os.stat(path).st_mtime)

                if timeframe == "day":
                    folder_name = date.strftime("%B %d, %Y")
                elif timeframe == "week":
                    month = date.strftime("%B %Y")
                    month_folder = os.path.join(src_dir, month)
                    week = week_of_month_extract(date)
                    week_folder = f"Week {week}"
                    folder_name = os.path.join(month_folder, week_folder)

                elif timeframe == "year":
                    folder_name = date.strftime("%Y")
                else:
                    folder_name = date.strftime('%B %Y')
                folder_path = os.path.join(src_dir, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(path, os.path.join(folder_path, file))
            except Exception as e:
                print(f"Error in {file}: {e}")
    print("Files have been organized successfully.")




if __name__ == "__main__":
    src = input("Enter the source path: ").strip()
    timeframe = str(input("Enter timeframe: ")).lower()
    organize_files_by_month(src, timeframe)

