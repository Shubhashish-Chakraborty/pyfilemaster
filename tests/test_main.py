from pyfilemaster.main import readBinFile, convertBinToCSV, writeBinFile

def test_readBinFile():
    # Testing with a valid file path
    readBinFile("./testFiles/SampleBin1")

def test_convertBinToCSV():
    # Testing with a valid file path and output file
    convertBinToCSV("./testFiles/SampleBin1", "CSV_FILE_GENERATED")

def test_writeBinFile():
    # Testing with a valid output file path and the data content of the binary file
    writeBinFile("./testFiles/binary_file_created.dat" , [
        {
            "name": "Andrew",
            "language": "python"
        },
        {
            "name": "Tristan",
            "language": "JavaScript"
        }
    ])