from bs4 import BeautifulSoup
import trafilatura
import langid
import readability
import nltk
from nltk.tokenize import sent_tokenize

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

def removeTags(html: str):
    # BeautifulSoup pre-process
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.select('nav, header, footer, .ads, .sidebar'):
        tag.decompose()
    return soup

def trafilaturaProcess(soup: BeautifulSoup):
    # Trafilatura process
    extracted = trafilatura.extract(str(soup), deduplicate= True, output_format='html')
    return extracted

def textFromParagraphs(extracted: str):
    # BeautifulSoup post-process
    soup = BeautifulSoup(extracted, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return paragraphs

def splitIntoSentences(paragraphs: list[str]) -> list[str]:
    return [sentence for p in paragraphs for sentence in sent_tokenize(p)]

def isTargetLanguage(sentence: str, targetLang: str= 'en'):
    lang, _ = langid.classify(sentence)
    return lang == targetLang

def isShortSentence(sentence: str, min: int= 5):
    if sentence == '':
        return True
    try:
        return readability.getmeasures(sentence)['sentence info']['words'] < min
    except:
        return True

def extractText(html: str):
    soup = removeTags(html)
    extracted = trafilaturaProcess(soup)
    
    if extracted == None:
        paragraphs = []
        return paragraphs
    
    sentences = [sentence
        for sentence in splitIntoSentences(textFromParagraphs(extracted))
        if isTargetLanguage(sentence)
        and not isShortSentence(sentence)
    ]

    return sentences