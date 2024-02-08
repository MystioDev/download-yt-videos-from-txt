from pytube import YouTube

def downloadVideo(url: str):
    videoId: str = url.replace("https://www.youtube.com/watch?v=", "")
    
    yt: YouTube = YouTube(url=url)
    video = yt.streams.get_highest_resolution()
    
    video.download(
       output_path="D:/Python/_yt/videos",
       filename=f"{videoId}.mp4"
    )
    
    print(f"{url} ✓")
    print()
    

urls: list = []

x: int = 0

with open("urls.txt", "rt", encoding="utf-8") as f:
    for i in f:
        urls = f.read().strip().splitlines()

for url in urls:
    downloadVideo(url=url)

print()
print("Done")
print()