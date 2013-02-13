'''
Created on Feb 7, 2013

Simple script to pull down all resources from the course Introduction to Astronomy:
Reference: https://class.coursera.org/introastro-2012-001/class/index

Exploring the use of Beautiful Soup as a html parsing framework and OptionParser to handle command line options

@author: Krishnan_Narayan
'''
import urllib.request
import os
import time
import optionsParser
from bs4 import BeautifulSoup

DEST_PATH = ''
__startTime__ = 0
__endTime__ = 0
__downloadCount__ = 0

optionsParser.TestPythonVersion()
(options, source) = optionsParser.OptionParserWrapper()

if options is not None and options.dest is not None:
    DEST_PATH = options.dest
elif source is None:
    exit()
else:
    DEST_PATH = os.getcwd()
    
resource = source[0]

if not os.path.exists(resource):
    print("Invalid path specified or the source file does not exist")
    exit()


page = urllib.request.urlopen('file:///' + resource)

text = page.read().decode('utf-8')
print("Initiating job...")
__startTime__ = time.time()
soup = BeautifulSoup(text)
pdfList = soup.find_all(title='Lecture slides PDF')
pdfLinks = []

if pdfList is not None and pdfList.__len__() > 0:
    for element in pdfList:
        strg = str(element)
        bs = BeautifulSoup(strg)
        title = str(bs.find('div').string)
        pdf_url = bs.find('a', href=True)['href']
        s = title.split(' - ')
        if s is not None and s.__len__() == 2:
            week = s[0][s[0].__len__() - 1]
            slide = s[1][0:2]
            # look at week number and create collection just for that set of slides
            if not os.path.exists(DEST_PATH + 'Week ' + week):
                if options.verbose is True:
                    print("***********Creating folder for Week " + week + " ***************")
                os.makedirs(DEST_PATH + 'Week ' + week)
            
            if options.verbose is True:
                print("fetching file from URL: " + pdf_url)
                    
            pdf = urllib.request.urlopen(pdf_url)
            data = pdf.read()
            pdf.close()
            f = open(DEST_PATH + 'Week ' + week + '/' + 'Slide ' + slide + ".pdf", 'wb')
            f.write(data)
            f.close()
            if options.verbose is True:
                print("Saved to : " + DEST_PATH + "Week " + week + "/" + "Slide " + slide + ".pdf")
            __downloadCount__ += 1
            
__endTime__ = time.time()
print("Job complete...")
print("Time taken for downloading " + str(__downloadCount__) + " files: " + str(__endTime__ - __startTime__) + " seconds.")
             
                                
                
                
                
        
        
                
        
    
    
    
    
        
    
                
                   








