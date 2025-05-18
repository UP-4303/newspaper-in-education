baseUrl = 'http://data.gdeltproject.org/gdeltv3/readability/'
unformattedFileName = '{datetime}.readability.json'
datetimeFormat = '%Y%m%d%H%M%S'
compressionExtension = '.gz'

compressedFolder = '../gdelt_compressed/'
rawFolder = '../gdelt_raw/'
cleanFolder = '../article_data/'

formattedDate = lambda date: date.strftime(datetimeFormat)
fileName = lambda date: unformattedFileName.format(datetime = formattedDate(date))
url = lambda date: baseUrl + fileName(date) + compressionExtension
compressedFilePath = lambda date: compressedFolder + fileName(date) + compressionExtension
rawFilePath = lambda date: rawFolder + fileName(date)
cleanFilePath = lambda date: cleanFolder + fileName(date)