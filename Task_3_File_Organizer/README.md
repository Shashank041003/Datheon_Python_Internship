# Automated File Organizer & Cleanup Utility

## Project Overview
The Automated File Organizer is a Python-based utility that helps users organize cluttered folders automatically.

The program scans files in a selected directory, identifies their extensions, creates category folders, and moves files into the appropriate folders.

It also handles duplicate filenames and permission errors to ensure reliable file organization.

## Features
- Automatic file organization based on file extensions
- Creates category folders dynamically
- Supports Documents, Images, Videos, Archives, Code, and Others
- Moves files using Python's file handling libraries
- Handles duplicate filenames without overwriting files
- Handles permission and file operation errors
- Displays a summary of files moved and errors encountered

## Technologies Used
- Python 3
- os module
- shutil module
- pathlib module

## Project Structure
```text
Automated_File_Organizer/
├── organizer.py
└── README.md
```

## How to Run

### Step 1: Install Python
Make sure Python 3 is installed on your system.

### Step 2: Download the Project
Download or clone this repository to your computer.

### Step 3: Run the Program
Open the project folder in VS Code and execute:

```bash
python organizer.py
```

### Step 4: Enter Folder Path
When prompted, enter the complete path of the folder you want to organize.

Example:

```text
C:\Users\YourName\Desktop\Test_Files
```

The program will scan the folder and move files into appropriate category folders.

## Supported File Categories

| Category | File Extensions |
|---|---|
| Documents | .pdf, .docx, .txt, .xlsx |
| Images | .jpg, .jpeg, .png, .gif |
| Videos | .mp4, .mkv, .mov, .avi |
| Archives | .zip, .rar, .7z, .tar |
| Code | .py, .java, .cpp, .html, .css, .js |
| Others | Unsupported or unknown extensions |

## Sample Output
```text
Starting file organization...

Moved: resume.pdf -> Documents/

========================================
FILE ORGANIZATION SUMMARY
========================================
Total files moved: 1
Errors encountered: 0

Organization completed!
```

## Author
Shashank Tiwari   