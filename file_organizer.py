# import os
# import mimetypes

# def get_file_types(directory_path):
#     file_types = {}

#     # Iterate through all files in the directory
#     for root, dirs, files in os.walk(directory_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Use mimetypes module to determine the file type
#             mime_type, encoding = mimetypes.guess_type(file_path)

#             # Store the file type in the dictionary
#             file_types[file_name] = mime_type if mime_type else 'Unknown'

#     return file_types

# # Example usage
# directory_path = 'D:\meghu\source_directory'
# file_types = get_file_types(directory_path)

# # Print the results
# for file_name, file_type in file_types.items():
#     print(f"{file_name}: {file_type}")





# import os
# import shutil
# import mimetypes

# def segregate_files(directory_path, output_directory):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Iterate through all files in the input directory
#     for root, dirs, files in os.walk(directory_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Use mimetypes module to determine the file type
#             mime_type, encoding = mimetypes.guess_type(file_path)

#             # Create a directory for the file type in the output directory
#             type_directory = os.path.join(output_directory, mime_type)
#             if not os.path.exists(type_directory):
#                 os.makedirs(type_directory)

#             # Move the file to the corresponding directory
#             destination_path = os.path.join(type_directory, file_name)
#             shutil.move(file_path, destination_path)

# # Example usage
# input_directory = 'D:\meghu\source_directory'
# output_directory = 'D:\Result_Directory'

# segregate_files(input_directory, output_directory)


""" this code is overding the files """
# import os
# import shutil
# import mimetypes

# def segregate_files(directory_path, output_directory):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Iterate through all files in the input directory
#     for root, dirs, files in os.walk(directory_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Use mimetypes module to determine the file type
#             mime_type, encoding = mimetypes.guess_type(file_path)

#             # Create a directory for the file type in the output directory
#             type_directory = os.path.join(output_directory, mime_type)
#             if not os.path.exists(type_directory):
#                 os.makedirs(type_directory)

#             # Move the file to the corresponding directory
#             destination_path = os.path.join(type_directory, file_name)

#             try:
#                 # Attempt to move the file
#                 shutil.move(file_path, destination_path)
#                 print(f"File moved: {file_name}")
#             except shutil.Error as e:
#                 print(f"Error moving {file_name}: {e}")
#                 # Handle the case where the file already exists in the destination directory

# # Example usage
# input_directory = 'D:\meghu\source_directory'
# output_directory = 'D:\Result_Directory'

# segregate_files(input_directory, output_directory)





""" this code we need to give the path manually"""
# import os
# import shutil
# import mimetypes

# def segregate_files(directory_path, output_directory):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Iterate through all files in the input directory
#     for root, dirs, files in os.walk(directory_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Use mimetypes module to determine the file type
#             mime_type, encoding = mimetypes.guess_type(file_path)

#             # Create a directory for the file type in the output directory
#             type_directory = os.path.join(output_directory, mime_type)
#             if not os.path.exists(type_directory):
#                 os.makedirs(type_directory)

#             # Check if the file already exists in the destination directory
#             destination_path = os.path.join(type_directory, file_name)
#             if os.path.exists(destination_path):
#                 print(f"File '{file_name}' already exists in '{type_directory}'")
#             else:
#                 # Move the file to the corresponding directory
#                 shutil.move(file_path, destination_path)
#                 print(f"File moved: {file_name}")

# # Example usage
# input_directory = 'D:\meghu\source_directory'
# output_directory = 'D:\Result_Directory'

# segregate_files(input_directory, output_directory)






# import os
# import shutil
# import mimetypes
# import tkinter as tk
# from tkinter import filedialog

# def get_input_directory():
#     root = tk.Tk()
#     root.withdraw()
#     input_directory = filedialog.askdirectory(title="Select Input Directory")
#     return input_directory

# def get_output_directory():
#     root = tk.Tk()
#     root.withdraw()
#     output_directory = filedialog.askdirectory(title="Select Output Directory")
#     return output_directory

# def segregate_files(directory_path, output_directory):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Iterate through all files in the input directory
#     for root, dirs, files in os.walk(directory_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Use mimetypes module to determine the file type
#             mime_type, encoding = mimetypes.guess_type(file_path)

#             # Create a directory for the file type in the output directory
#             type_directory = os.path.join(output_directory, mime_type)
#             if not os.path.exists(type_directory):
#                 os.makedirs(type_directory)

#             # Check if the file already exists in the destination directory
#             destination_path = os.path.join(type_directory, file_name)
#             if os.path.exists(destination_path):
#                 print(f"File '{file_name}' already exists in '{type_directory}'")
#             else:
#                 # Move the file to the corresponding directory
#                 shutil.move(file_path, destination_path)
#                 print(f"File moved: {file_name}")

# # Example usage
# input_directory = get_input_directory()
# output_directory = get_output_directory()

# segregate_files(input_directory, output_directory)








import os
import shutil
import mimetypes
import tkinter as tk
from tkinter import filedialog

# Function to get input directory through a GUI dialog
def get_input_directory():
    try:
        root = tk.Tk()
        root.withdraw()
        input_directory = filedialog.askdirectory(title="Select Input Directory")
        return input_directory
    except Exception as e:
        print(f"Error while selecting input directory: {e}")
        return None

# Function to get output directory through a GUI dialog
def get_output_directory():
    try:
        root = tk.Tk()
        root.withdraw()
        output_directory = filedialog.askdirectory(title="Select Output Directory")
        return output_directory
    except Exception as e:
        print(f"Error while selecting output directory: {e}")
        return None

# Function to segregate files based on their MIME types
def segregate_files(directory_path, output_directory):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Iterate through all files in the input directory
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Use mimetypes module to determine the file type
                mime_type, encoding = mimetypes.guess_type(file_path)

                # Create a directory for the file type in the output directory
                type_directory = os.path.join(output_directory, mime_type)
                if not os.path.exists(type_directory):
                    os.makedirs(type_directory)

                # Check if the file already exists in the destination directory
                destination_path = os.path.join(type_directory, file_name)
                if os.path.exists(destination_path):
                    print(f"File '{file_name}' already exists in '{type_directory}'")
                else:
                    # Move the file to the corresponding directory
                    shutil.move(file_path, destination_path)
                    print(f"successful organization: {file_name}")

        # Print the hierarchy of the destination directory after successful organization
        print("\nHierarchy of Destination Directory:")
        for root, dirs, files in os.walk(output_directory):
            level = root.replace(output_directory, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file_name in files:
                print('{}{}'.format(subindent, file_name))

    except Exception as e:
        print(f"Error during file segregation: {e}")

# Example usage
try:
    input_directory = get_input_directory()
    output_directory = get_output_directory()

    # Check if input and output directories are valid before calling the function
    if input_directory and output_directory:
        segregate_files(input_directory, output_directory)
    else:
        print("Error: Invalid input or output directory.")

except PermissionError as pe:
    print(f"Permission error: {pe}")
except Exception as e:
    print(f"Unexpected error: {e}")