from pyfilemaster.main import ReadBinFile, convertToCSV

def test_ReadBinFile():
    # Testing with a valid file path
    ReadBinFile("./testFiles/SampleBin1")

def test_convertToCSV():
    # Testing with a valid file path and output file
    convertToCSV("./testFiles/SampleBin1", "CSV_FILE_GENERATED")