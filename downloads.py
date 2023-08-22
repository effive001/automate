import os
import shutil

def get_file_extension(file_name):
    _, extension = os.path.splitext(file_name)
    return extension[1:].lower()

def sort_downloading_files(source_folder, destination_folders):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            extension = get_file_extension(filename)
            if extension in destination_folders:
                destination_folder = destination_folders[extension]
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                try:
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"Moved '{filename}' to '{destination_folder}'.")
                except Exception as e:
                    print(f"Error moving '{filename}' to '{destination_folder}': {e}")
            else:
                print(f"File '{filename}' with extension '{extension}' not sorted.")

if __name__ == "__main__":
    # Customize the source folder and destination folders here
    source_folder = r"C:\Users\effiv\Downloads"  # Update with your source folder path
    destination_folders = {
        'pdf': r"C:\Users\effiv\Documents\PDFs",
        'docx': r"C:\Users\effiv\Documents\WordFiles",
        'jpg': r"C:\Users\effiv\Pictures\JPGs",
        'mp4': r"C:\Users\effiv\Pictures\MP4s",
        'mov': r"C:\Users\effiv\Pictures\MP4s",
        'mp3': r"C:\Users\effiv\Pictures\Audios",

        'png': r"C:\Users\effiv\Pictures\JPGs",
        'jpeg': r"C:\Users\effiv\Pictures\JPGs",
        'exe': r"C:\Users\effiv\Pictures\Apps",
        'zip': r"C:\Users\effiv\Pictures\Archs",





        # Add more extensions and corresponding folders as needed
    }

    sort_downloading_files(source_folder, destination_folders)
