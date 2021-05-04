# Desktop to desktop_archives

import os  # function to navigate, create, delete and modify files and folders
import shutil
# Folder path
desktop_directory = "/Users/jakeayoub/Desktop/"
desktop_library = "/Users/jakeayoub/Desktop/desktop_archives"
exclude_list = ["python_projects", "venv", "desktop_archives"]


def main():
    for file in os.listdir(desktop_directory):
        # we want to ignore certain files, update "exclude_list" above
        if file in exclude_list:
            pass
        else:
            source = desktop_directory + file
            # ignores duplicates and move files from one directory to another
            try:
                shutil.move(source, desktop_library)
            except:
                pass
# To run file name from terminal
if __name__ == '__main__':
    main()