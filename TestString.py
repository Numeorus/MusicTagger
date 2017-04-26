import os

print "Test String\n"

class MusicFile(object):
	fileName = ""
	trackName = ""
	artist = ""

	def __init__(self,fileName,trackName,artist):
		self.fileName = fileName
		self.trackName = trackName
		self.artist = artist


for file in os.listdir("/home/sebastien/Documents"):
    if file.endswith(".m4a"):
    	trackName = (file.split('.',1)[0]).split('-',1)[1]
    	artist = file.split('-',1)[0]
    	print "file : "+file+"\n\t=> trackName : "+trackName+"\n\t=> artist: "+artist
        #musicFile1 = MusicFile(musicFile1,file,trackName,artist)

x = []
n=10

for i in range (0,n):
	x.append(i)

print x
print x[5]
print len(x)