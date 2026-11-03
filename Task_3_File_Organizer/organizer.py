
import os
import shutil
from pathlib import Path


# File extension categories
FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".xls", ".xlsx", ".ppt", ".pptx"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".svg", ".webp"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".wmv"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".java", ".cpp", ".c",
        ".html", ".css", ".js", ".json"
    ]
}


def get_category(extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Avoid overwriting files with the same name."""
    if not destination.exists():
        return destination

    base_name = destination.stem
    extension = destination.suffix
    parent = destination.parent

    counter = 1

    while True:
        new_name = f"{base_name}_{counter}{extension}"
        new_destination = parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: The selected folder does not exist.")
        return

    moved_count = 0
    error_count = 0

    print("\nStarting file organization...\n")

    # Scan files in the selected folder
    for item in folder.iterdir():

        # Skip directories
        if item.is_dir():
            continue

        # Skip this script itself
        if item.name == Path(__file__).name:
            continue

        extension = item.suffix.lower()
        category = get_category(extension)

        destination_folder = folder / category

        try:
            # Create category folder if required
            destination_folder.mkdir(exist_ok=True)

            # Get destination path
            destination = destination_folder / item.name

            # Avoid filename collision
            destination = get_unique_destination(destination)

            # Move file
            shutil.move(str(item), str(destination))

            print(f"Moved: {item.name} -> {category}/")
            moved_count += 1

        except PermissionError:
            print(f"Permission denied: {item.name}")
            error_count += 1

        except OSError as error:
            print(f"Could not move {item.name}: {error}")
            error_count += 1

    # Display summary
    print("\n" + "=" * 40)
    print(" FILE ORGANIZATION SUMMARY")
    print("=" * 40)

    print(f"Total files moved: {moved_count}")
    print(f"Errors encountered: {error_count}")

    print("\nOrganization completed!")


def main():
    print("=" * 40)
    print(" AUTOMATED FILE ORGANIZER")
    print("=" * 40)

    print("\nEnter the folder path you want to organize.")
    folder_path = input("Folder path: ").strip().strip('"')

    organize_files(folder_path)


if __name__ == "__main__":
    main()
