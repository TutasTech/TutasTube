
#Simple YTdownloader follow us t.me/tutas_tech

from asyncio import streams
from pytube import YouTube


print("\t\t welcome to TutasTube a powerful YT downloader\n \t YT:Tutastech\n\t telegram:@tutastech\n\t my_telegram:@thefaucon\n\t github:Tutastech")

def end(stream,file_path):  
    print("\n download succesful file location:",file_path)
    print("\n\n powered by TutasTech follow us for more")
    

def do(stream,chunk,byte_remaining):   
    t=stream.filesize-byte_remaining
    print("telechargement ",t*100/stream.filesize,"%"," \n")
    


url=input("entrez le lien de la video a telecharger \n")

yt=YouTube(url)

yt.register_on_progress_callback(do)
yt.register_on_complete_callback(end)

titre=input(" ENTREZ LE NOM DU FICHIER DE SORTI OU 0 POUR CONSERVER LE NOM D'ORIGINE \n")
if titre!='0':
    yt.title=titre


i=1

reso=list()
print("selectionez la resolution de votre video\n")
for el in yt.streams.fmt_streams:
    if el.is_progressive==True:       
        print(i," ",el.resolution,el.filesize/1000000," Mo")
        reso.append(el.resolution)
        i=i+1
print(i+1," AUDIO")
ne=0        
a=  int(input())
for el in yt.streams.fmt_streams:
    if el.is_progressive==True:
       ne=ne+1


for el in yt.streams.fmt_streams:
    if a<i+1:

        if el.is_progressive==True and el.resolution==reso[a-1] :
           n=el.itag

if a==i+1:
    stream=yt.streams.get_audio_only()

else:
    stream=yt.streams.get_by_itag(n)
    






stream.download()
print("\n press any key to exit")
input()


