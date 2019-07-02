import json
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load
import pyglet


print('Hello one of a option')

opt = [
    {
        '1': 'Show all songs'
    },
    {
        '2': 'Show detail of a song'
    },
    {
        '3': 'Play a song'
    },
    {
        '4': 'Search and download songs'
    },
    {
        '5': 'Exit'
    }
]

song_list = []
listToPushData = []
while True:
    with open('data.json', encoding='utf-8') as data:
        dataGet = json.loads(data.read())
    for i in opt:
        for key,value in i.items():
            print(key, '.', value)
    choose = int(input("Choose: "))

    if choose == 1 :
        # Lay du lieu tu data.json
        with open('data.json', encoding = 'utf-8') as data:
            dataGet = json.loads(data.read())
        if dataGet == []:
            print("Not music in lists")
        else:
            for index, music in enumerate(dataGet):
                print(index+1, " - ", music['title'])

    elif choose == 2:
        with open('data.json', encoding = 'utf-8') as data:
            dataGet = json.loads(data.read())
        for index, music in enumerate(dataGet):
            print(index+1, " - ", music['title'])
        detail = int(input("Nhap so cua hat muon show detail? "))

        findSuccess = False
        SongSearched = {}
        for i in range(len(dataGet)):
            if i == detail - 1:
                findSuccess = True
                SongSearched = dataGet[detail - 1]

        if findSuccess == True:
            print(SongSearched["id"], " ", SongSearched["webpage_url"])
        else:
            print("Khong Co")
        # dataGet[0]['id']

    elif choose == 3:
        with open('data.json', encoding = 'utf-8') as data:
            dataGet = json.loads(data.read())
        for index, music in enumerate(dataGet):
            print(index+1, " - ", music['title'])

        choose = int(input("Chon bai hat: "))
        mp3File = dataGet[choose-1]['id']+".mp3"

        player = Player()
        source = load(mp3File)
        player.queue(source)
        player.play()
        while True:
            out_put = input('play , pause or stop ?').lower()
            if out_put == 'play':
                player.play()
            elif out_put == 'pause':
                player.pause()
            elif out_put == "stop":
                player.pause()
                break

    elif choose == 4 :
        # doc data tu file json
        with open('data.json', encoding = 'utf-8') as data:
            dataGet = json.loads(data.read())
        listToPushData = dataGet

        songSearch = input("Name Song Search: ")

        optionsExtract = {
            'default_search': 'ytsearch3',
        }

        ydl = YoutubeDL(optionsExtract)
        search_result = ydl.extract_info(songSearch, download = False)
        song_list = search_result['entries']

        #choose download a song
        optionsDownload = {
            'outtmpl': '%(id)s', # lấy tên file đown về là id của video
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', # Tách lấy audio
                'preferredcodec': 'mp3', # Format ưu tiên là mp3
                'preferredquality': '192', # Chất lượng bitrate
            }],
        }
        for index, music in enumerate(song_list):
            print(index+1, " - ", music['title'])
        chooseDownload = int(input("Choose music want to download: ")) - 1

        ydl1 = YoutubeDL(optionsDownload)
        downloadOneMusic = ydl1.extract_info(song_list[chooseDownload]['id'], download = True)

        listToPushData.append(downloadOneMusic)
        with open('data.json', 'w') as dataPush:
            dataPush = json.dump(listToPushData, dataPush)


    elif choose == 5:
        break
