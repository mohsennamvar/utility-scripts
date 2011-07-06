''' This file scrapes the images from the DYK archives and associates the images
with the respective hooks '''
import os
import urllib
import codecs

import BeautifulSoup

directory = "hookhtmls"
        

def main():
    ''' test main '''
    sno = 1
    files = os.listdir(directory)
    imagefile = codecs.open("images.csv", encoding='utf-8', mode='w+')
    imagefile.write("sno,title,imgtitle,src,alt\n")
    for fil in files:
        print fil        
        html = open(os.path.join(directory,fil), "r")
        soup = BeautifulSoup.BeautifulSoup(html.read())
        h3 = soup.find('h3')
        div = h3.findNext('div',
                          attrs={'style':'float:right;margin-left:0.5em;'})
        #print div
        while div != None:    
            li = div.findNext("li",
                              attrs={'style':'-moz-float-edge: content-box'})
            try:
                link = li.b.a['href']
            except TypeError:
                link = li.find("a")["href"]
            link = link.replace("/wiki/","")
            title = urllib.unquote(unicode(link).encode('ascii')).decode('utf-8')
            title = " ".join(title.split('_')).replace(",",";")
            print title
            try:
                imgAnchor = div.find("a", attrs={'class':'image'})
                imgtitle = unicode(imgAnchor["title"]).replace(",",";")
                img = imgAnchor.find("img")
                src = unicode(img['src']).replace(",",";")
                alt = unicode(img['alt']).replace(",",";")
                
                imagefile.write(str(sno)+","+title+","+imgtitle+","+src+","+alt+"\n")
                sno += 1
            except:
                print "Image Unavailable"
            div = div.findNext('div',
                               attrs={'style':'float:right;margin-left:0.5em;'})
            #print "nextdiv",div.a["title"]
    imagefile.close()
                
                


        
if __name__ == "__main__":
    main()
