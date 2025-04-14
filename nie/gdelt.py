import datetime
import gzip
import json
import re
import requests

class GdeltReadability:
    baseUrl = 'http://data.gdeltproject.org/gdeltv3/readability/'
    unformatedFileName = '{datetime}.readability.json'
    datetimeFormat = '%Y%m%d%H%M%S'
    compressionExtension = '.gz'

    compressedFolder = 'gdelt_compressed/'
    uncompressedFolder = 'gdelt_files/'

    def __init__(self, requestTime: datetime.datetime):
        self.requestTime = requestTime
        self.formattedDate = self.requestTime.strftime(self.datetimeFormat)
        self.fileName = self.unformatedFileName.format(datetime= self.formattedDate)
        self.url = self.baseUrl + self.fileName + self.compressionExtension
        self.compressedFilePath = self.compressedFolder + self.fileName + self.compressionExtension
        self.uncompressedFilePath = self.uncompressedFolder + self.fileName
        return

    def getGdelt(self)-> str:
        response = requests.get(self.url)

        with open(self.compressedFilePath, 'wb') as f:
            f.write(response.content)

        return self.compressedFilePath

    def uncompressGdelt(self)-> str:

        with gzip.open(self.compressedFilePath, 'rb') as fIn:
            content = self.gdeltParser(fIn.read().decode('utf-8'))

            with open(self.uncompressedFilePath, 'w') as fOut:
                fOut.write(content)

        return self.uncompressedFilePath
    
    def getJson(self):
        with open(self.uncompressedFilePath, 'r') as fIn:
            gdeltJson = json.loads(fIn.read())
        return gdeltJson

    def gdeltParser(gdeltJson: str):
        # Step 1: Make it a list
        gdeltJson = '[' + gdeltJson + ']'
        gdeltJson = re.sub('\n{', ',{', gdeltJson)
        gdeltJson = re.sub('\\n', '', gdeltJson)

        # Step 2: Make it all JSON
        jsonObject = json.loads(gdeltJson)
        
        for i in range(len(jsonObject)):
            # From GNU `style` output to JSON
            sourceScores = jsonObject[i]['readabilityScores']

            retrieved = re.findall(r'[^\/0-9]([0-9.]+)[^%0-9]', sourceScores)
            
            cleanScores = {
                "readability grades":{
                    "Kincaid": float(retrieved[0]),
                    "ARI": float(retrieved[1]),
                    "Coleman-Liau": float(retrieved[2]),
                    "Flesch Index": float(retrieved[3]),
                    "Flesch Label": re.search(r'Flesch Index: [0-9.]+/100 \(([a-zA-Z].?)\)', sourceScores),
                    "Fog Index": float(retrieved[4]),
                    "Lix": float(retrieved[5]),
                    "Lix school year": int(retrieved[6]),
                    "SMOG-Grading": float(retrieved[7]),
                },
                "sentence info":{
                    "characters": int(retrieved[8]),
                    "words": int(retrieved[9]),
                    "word average length": float(retrieved[10]),
                    "word average syllables": float(retrieved[11]),
                    "sentences": int(retrieved[12]),
                    "sentence average length": float(retrieved[13]),
                    "short sentences": int(retrieved[14]),
                    "short sentences most words": int(retrieved[15]),
                    "long sentences": int(retrieved[16]),
                    "long sentences least words": int(retrieved[17]),
                    "paragraphs": int(retrieved[18]),
                    "paragraph average length": float(retrieved[19]),
                    "questions": int(retrieved[20]),
                    "passive sentences": int(retrieved[21]),
                    "longest sentence": int(retrieved[22]),
                    "longest sentence index": int(retrieved[23]),
                    "shortest sentence": int(retrieved[24]),
                    "shortest sentence index": int(retrieved[25])
                },
                "word usage":{
                    "verb types": {
                        "to be": int(retrieved[26]),
                        "auxiliary": int(retrieved[27])
                    },
                    "conjunctions": int(retrieved[28]),
                    "pronouns": int(retrieved[29]),
                    "prepositions": int(retrieved[30]),
                    "nominalizations": int(retrieved[31])
                },
                "sentence beginnings":{
                    "pronoun": int(retrieved[32]),
                    "interrogative pronoun": int(retrieved[33]),
                    "article": int(retrieved[34]),
                    "subordinating conjunction": int(retrieved[35]),
                    "conjunction": int(retrieved[36]),
                    "preposition": int(retrieved[37])
                }
            }

            jsonObject[i]['readabilityScores'] = cleanScores

        return json.dumps(jsonObject, indent=4)