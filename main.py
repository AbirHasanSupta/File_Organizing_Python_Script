import os
import shutil
from datetime import datetime

import get_creation_date


def week_of_month_extract(date):
    first_day = date.replace(day=1)
    return (date.day + first_day.weekday()) // 7 + 1


def month_group_extract(month, interval):
    curr_year = datetime.now().year
    month_start = ((month - 1) // interval) * interval + 1
    month_end = min(month_start + interval - 1, 12)
    start_month = datetime(curr_year, month_start, 1).strftime("%B")
    end_month = datetime(curr_year, month_end, 1).strftime("%B")
    return f"{start_month} - {end_month}"

def get_folder_name(timeframe, date, src_dir):
    folder_name = None
    if timeframe == "day":
        folder_name = date.strftime("%B %d, %Y")
    elif timeframe == "week":
        month = date.strftime("%B %Y")
        month_folder = os.path.join(src_dir, month)
        week = week_of_month_extract(date)
        week_folder = f"Week {week}"
        folder_name = os.path.join(month_folder, week_folder)
    elif timeframe == "month":
        folder_name = date.strftime('%B %Y')
    elif timeframe == "year":
        folder_name = date.strftime("%Y")
    else:
        if timeframe.endswith('months'):
            interval = int(timeframe.split(' ')[0])
            folder_name = month_group_extract(date.month, interval)
    return folder_name



def organize_files(src_dir, timeframe, date_type='default'):
    if not os.path.exists(src_dir):
        print(f"Directory '{src_dir}' does not exist.")
        return
    files = os.listdir(src_dir)
    for file in files:
        path = os.path.join(src_dir, file)
        if os.path.isfile(path):
            try:
                if date_type == 'defualt':
                    date = datetime.fromtimestamp(os.stat(path).st_mtime)
                else:
                    date = get_creation_date.get_creation_date(path)
                folder_name = get_folder_name(timeframe, date, src_dir)
                if not folder_name:
                    print("Invalid Timeframe")
                    return
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
    organize_files(src, timeframe)

