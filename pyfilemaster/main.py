import pickle
import csv

def writeBinFile(path, data):
    """
    Writes data to a binary `.dat` file.

    Parameters:
        path (str): Path to the `.dat` file (with or without extension(.dat)).
        data (list): List of dictionaries to be stored in the file.
    """

    if (path.lower()[-1:-5:-1][::-1] == ".dat"):
        path = path.lower().rstrip(".dat")
    else:
        pass

    try:
        with open(path + ".dat", "ab") as f:
            for record in data:
                pickle.dump(record, f)
        print(f"Data successfully written to {path}.dat")
    except Exception as e:
        print(f"An error occurred: {e}")

def readBinFile(path):
    """
    Reads and prints the contents of a binary `.dat` file.

    Parameters:
        path (str): Path to the `.dat` file (mention path with or without extension(.dat))
    """
    
    if (path.lower()[-1:-5:-1][::-1] == ".dat"):
        path = path.lower().rstrip(".dat")
    else:
        pass
    
    try:
        with open(path + ".dat", "rb") as f:
            while True:
                try:
                    print(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        print(f"File not found: {path}.dat")
    except Exception as e:
        print(f"An error occurred: {e}")


def convertBinToCSV(path, CSVFileName="CSVFile_Generated"):
    """
    Converts data of a binary `.dat` file to a CSV(Excel) file.

    Parameters:
        path (str): Path to the `.dat` file (with or without extension(.dat)).
        CSVFileName (str): Name of the output CSV file (default="CSVFile_Generated").
    """

    if (path.lower()[-1:-5:-1][::-1] == ".dat"):
        path = path.lower().rstrip(".dat")
    else:
        pass
    
    try:
        # Read data from the binary file
        file_data = []
        with open(path + ".dat", "rb") as f:
            while True:
                try:
                    file_data.append(pickle.load(f))
                except EOFError:
                    break

        # Extract headings from the first record
        if file_data:
            headings = list(file_data[0].keys())

            # Write to CSV file
            with open(CSVFileName + ".csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(headings)  # Write headings

                # Write data rows
                for record in file_data:
                    writer.writerow([record[key] for key in headings])
        else:
            print(f"No data found in {path}.dat")

    except FileNotFoundError:
        print(f"File not found: {path}")