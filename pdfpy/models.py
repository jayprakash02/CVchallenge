from django.db import models
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import PyPDF2   
import csv , os
from django.core.files import File
from django.core.files.base import ContentFile
# Create your models here.
class Collector(models.Model):
    id = models.IntegerField(primary_key=True)
    pdf_file = models.FileField(upload_to='')
    
    def save(self,*args,**kwargs):
       
        pfile = self.pdf_file
        
        pdfStr = " "
        pdfFileObj = pfile.open()
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            pdfStr += pageObj.extractText()
            
        pdfFileObj.close()
        stop_words = set(stopwords.words('english'))

        tokens = word_tokenize(pdfStr)
        tokens = [w.lower() for w in tokens]
        
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        words = [word for word in stripped if word.isalpha()]
        
        words = [w for w in words if not w in stop_words]
        # stemming of words
        porter = PorterStemmer()

        stemmed = [porter.stem(word) for word in words]
        final = ' '.join([str(elem) for elem in stemmed])

        
        pfile.save('apigen.csv', ContentFile(final))

        super(Collector,self).save(*args,**kwargs)