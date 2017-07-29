import os

from readability.readability import Document
from bs4 import BeautifulSoup as bs
from .blog_config import *

rootdir = '.'
res = os.walk(rootdir)

class Extract_Text():
    def main(self):
        for parent,dirnames,filenames in os.walk(rootdir+'/testdata'):
            for filename in filenames:
                path = os.path.join(parent,filename)
                print(path)
                with open(path, 'r') as f:
                    source = f.read()
                    self.extrace_text(source, filename)

    def extrace_text(self, source, filename):
        summary = Document(source).summary()
        soup = bs(summary, "lxml")

        for myid in myids:
            markup = soup.find(id=myid)
            if markup is not None: markup.clear()
        for myclass in myclasses:
            markup = soup.find(class_=myclass)
            if markup is not None: markup.clear()
        content = soup.contents[0].text
        path = "res/" + filename
        print(path)
        with open(path, 'w') as f:
            f.write(content)

if __name__=="__main__":
    extract = Extract_Text()
    extract.main()