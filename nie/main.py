import datetime
import os.path

import gdelt as gdeltLib

if __name__ == '__main__':
    targetDate = datetime.datetime(2020, 1, 1, 0, 1, 0)
    gdelt = gdeltLib.GdeltReadability(targetDate)

    if not os.path.isfile(gdelt.compressedFilePath):
        gdelt.getGdelt()
    if not os.path.isfile(gdelt.uncompressedFilePath):
        gdelt.uncompressGdelt()
    
    gdeltJson = gdelt.getJson()

