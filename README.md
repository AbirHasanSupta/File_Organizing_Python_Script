# File Organizer

A Python script to organize files in a specified directory based on modification or creation date.

## Features
- Organizes files into folders based on the selected timeframe: day, week, month, year, or custom intervals (e.g., `3 months`).
- Uses modification date by default or file creation date if specified.
- Automatically creates required directories before moving files.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```
## Usage
Run the script and provide the source directory and timeframe:

```bash
python file_organizer.py
```

### Parameters
- `src_dir`: The source directory where files are located.
- `timeframe`:
  - `day` → Organizes by individual days.
  - `week` → Organizes by week of the month.
  - `month` → Organizes by month.
  - `year` → Organizes by year.
  - `N months` → Organizes into custom intervals (e.g., `3 months`).
- `date_type`: *(Optional)*
  - `default` → Uses file modification date.
  - `creation` → Uses file creation date.

## Example
1. **Organizing by week:**
   ```bash
   Enter the source path: /path/to/files
   Enter timeframe: week
   ```
   *Moves files into folders like `March 2025/Week 2`.*

2. **Organizing by 3-month intervals:**
   ```bash
   Enter the source path: /path/to/files
   Enter timeframe: 3 months
   ```
   *Moves files into folders like `January - March`.*

## Notes
- Ensure you have permission to move files within the source directory.
- The script currently handles only files, not subdirectories.
- Make sure `get_creation_date.py` is available if using creation dates.
- 
