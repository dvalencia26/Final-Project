import shutil

from PIL import Image
import os
from PIL.ExifTags import TAGS
from face_ai import face_detection_ai

months_names = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']


def extract_metadata(directory, selected_files):
    for file_path in selected_files:
        if file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
            with Image.open(file_path) as img:
                try:
                    exif = img._getexif()
                    if exif:
                        date_info = exif.get(0x0132)  # Tag for DateTime
                        print(date_info)
                        if date_info:
                            date = date_info.split()[0]  # Extract date (YYYY:MM:DD)
                            # convert each substring into an integer
                            year, month, day = map(int, date.split(':'))
                            print(f"year: {year}, month: {month}, year: {year}")

                            # Create the year and month directories
                            year_directory = os.path.join(directory, str(year))
                            if not os.path.exists(year_directory):
                                os.makedirs(year_directory)
                            print("year folder created")

                            # Get the month name from the list
                            month_name = months_names[month - 1]
                            month_directory = os.path.join(year_directory, month_name)
                            if not os.path.exists(month_directory):
                                os.makedirs(month_directory)
                            print("month folder created")
                            img.close()

                            faces = face_detection_ai(file_path)

                            if faces == True:

                                face_directory = os.path.join(month_directory, str("Images with people"))
                                if not os.path.exists(face_directory):
                                    os.makedirs(face_directory)
                                shutil.move(file_path, os.path.join(face_directory, os.path.basename(file_path)))
                                test = os.path.basename(file_path)
                                print("name of the file: ", test)

                            else:
                                # Move image to the year/month directory
                                shutil.move(file_path, os.path.join(month_directory, os.path.basename(file_path)))
                                print(f"Moved {file_path} to {year}/{month_name} folder")

                        else:
                            print(f"No date information found for {file_path}")
                    else:
                        print(f"No EXIF DATA found for {file_path}")

                except Exception as E:
                    print(f"Error occurred while processing {file_path}, Error: {E}")

    no_name_path = selected_files[0].removesuffix(os.path.basename(selected_files[0]))
    print("this is the no name path: ", no_name_path)
    return len(os.listdir(no_name_path)) == 0
