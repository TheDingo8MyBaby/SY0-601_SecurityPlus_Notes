import os
import fileinput
import urllib.parse

# Get the current directory
current_dir = os.getcwd()

# Loop through files in the current directory
for file_name in os.listdir(current_dir):
    if file_name.endswith(".md"):  # Check if it's a Markdown file
        file_path = os.path.join(current_dir, file_name)
        
        # Open the file in read mode
        with fileinput.FileInput(file_path, inplace=True) as file:
            # Loop through each line in the file
            for line in file:
                # Perform find/replace operations
                line = line.replace('![[../', '![](')
                line = line.replace('g]]', 'g)')
                
                # Replace spaces only within image paths with %20
                parts = line.split('![](')
                if len(parts) > 1:
                    img_path = parts[1].split(')')[0]
                    img_path_parts = img_path.split('/')
                    encoded_path_parts = []
                    for part in img_path_parts:
                        if ' ' in part:
                            part = urllib.parse.quote(part, safe='')
                        encoded_path_parts.append(part)
                    img_path = '/'.join(encoded_path_parts)
                    line = '![](' + img_path + ')'
                
                # Print the modified line
                print(line, end='')
