from pytube import YouTube

link=input("enter link : ")
yt=YouTube(link)

videos=yt.streams.filter(progressive=True, file_extension='mp4')

# print(*videos,sep="\n")


i=1
for stream in videos:
    # if (stream.is_progressive ==True):
        print(str(i) + " " + str(stream))
        i+= 1

choice=int(input("Select Your Choice :"))
video=videos[choice-1]
print("Download Started")
video.download("E://")
print("Downloaded")




