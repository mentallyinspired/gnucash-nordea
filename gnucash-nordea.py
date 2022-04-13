import os, sys
import argparse
from pathlib import Path

# argparse object
parser = argparse.ArgumentParser(description='Convert Nordea csv files with transaction history to a csv format that GNUCash can handle')

# Limit the choice between files in dir or single file
group = parser.add_mutually_exclusive_group(required=True)

# Add argument for handling single file
group.add_argument('-f', '--file',
                    metavar='CSV File',
                    type=Path,
                    help='Parse single csv file')

# Add argument for handling directory with files
group.add_argument('-d', '--dir',
                    metavar='Parse directory of csv files',
                    type=Path,
                    help='Automatically parses all csv files in suplied directory')

# Execute the arg and create namespace
args = parser.parse_args()

def handle_file(file_path):
    # Return the absolut path
    file_path = file_path.absolute()
    
    # csv columns description (to be added to the file)
    desc = "Date;Deposit;Withdrawal;Description"

    # List for reversing the transaction order in csv file
    reverse_list = list()

    # Open the file with utf-8 encoding
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:

            # Split the csv line
            parts = line.split(";")

            # Check if it is a withtrawal (Also remove '-' in front of the number)
            if parts[1][0] == "-":
                new_line = f"{parts[0]};;{parts[1][1:]};{parts[5]}"

            # If not, then it is a deposit
            else:
                new_line = f"{parts[0]};{parts[1]};;{parts[5]}"

            reverse_list.append(new_line)

    # Reverse the list
    reverse_list.reverse()
    
    # Insert description of csv columns
    reverse_list.insert(0, desc)
    
    # Remove old csv column description
    reverse_list.pop(-1)

    # Remove old file
    os.remove(file_path)

    # Create new file with same name and write reverse order to it
    with open(file_path, mode='w', encoding='utf-8') as f:
        for line in reverse_list:
            f.write(line + "\n")


def handle_dir():
    dir_path = args.dir
    
    for f in dir_path.iterdir():
        # as_posix for str check
        if ".csv" in f.as_posix():
            handle_file(f)


if args.file and args.file.is_file():
    handle_file()
elif args.dir and args.dir.is_dir():
    handle_dir()
else:
    print("Invalid path")
    sys.exit()




