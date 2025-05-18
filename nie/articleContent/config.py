articleRawContentExtension = '.html'
articleContentExtension = '.txt'

articleRawContentFolder = '../article_content_raw/'
articleContentFolder = '../article_content/'

rawFilePath = lambda id: articleRawContentFolder + id + articleRawContentExtension
cleanFilePath = lambda id: articleContentFolder + id + articleContentExtension