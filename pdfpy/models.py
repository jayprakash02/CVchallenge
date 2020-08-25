from django.db import models
#Importing NLTK for string processing
import nltk
import string,json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
#Importing PYPDF2 for extracting text from PDF
import PyPDF2
#Importing FileField attribute
from django.core.files import File
from django.core.files.base import ContentFile

from collections import Counter


#Main Model
class Collector(models.Model):
    id = models.IntegerField(primary_key=True)
    pdf_file = models.FileField(upload_to='Document/%Y/%m/%d/Collector')

    def savefile(self,string=""):
        self.pdf_file.save('apigen.json', ContentFile(string))

    #overloading _save()
    def save(self,*args,**kwargs):
        pdfStr = " "
        pdfFileObj = self.pdf_file.open('r')
        #Reading PDF
        try:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #Extracting Text
            for i in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(i)
                pdfStr += pageObj.extractText()
        
            #stop_words Initializing
            stop_words = set(stopwords.words('english'))
            #tokenizing words for processing
            tokens = word_tokenize(pdfStr)
            tokens = [w.lower() for w in tokens]
            #removing puntuations
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in tokens]
            words = [word for word in stripped if word.isalpha()]
            words = [w for w in words if not w in stop_words]
            #stemming of words
            porter = PorterStemmer()
            stemmed = [porter.stem(word) for word in words]
            #creating a final string from list
            #final = ' '.join([str(elem) for elem in stemmed])
            final = json.dumps(stemmed)
            #saving the final into pfile and replacing pdf
            self.savefile(final)
        except IOError:        
            pdfFileObj.close()
            self.pdf_file.close()
        super(Collector,self).save(*args,**kwargs)

class Display(models.Model):
    mostcommon = models.IntegerField()
    freq_csv = models.FileField(upload_to='Document/%Y/%m/%d/Counter/')
    
    def savefile(self,string=""):
        try:
            self.freq_csv.save('freq.json', ContentFile(string))
        except IOError:
            self.freq_csv.close()

    def save(self,*args,**kwargs):
        try:
            temp = {}
            data = ""
            coll = Collector.objects.all()
            for obj in coll:
                f = obj.pdf_file.open('r')
                temp = json.load(f)
                data += json.dumps(temp)
                f.close()
            split_it = data.split()
            counter = Counter(split_it)
            most_occur = counter.most_common(self.mostcommon)
            final = json.dumps(most_occur)
            self.savefile(final)
        except IOError:            
            self.freq_csv.close()
        super(Collector,self).save(*args,**kwargs)