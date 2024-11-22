from pyfilemaster.main import ReadBinFile, convertToCSV

def test_readBinFile():
    # Testing with a valid file path
    ReadBinFile("./testFiles/SampleBin1")

def test_convertBinToCSV():
    # Testing with a valid file path and output file
    convertToCSV("./testFiles/SampleBin1", "CSV_FILE_GENERATED")