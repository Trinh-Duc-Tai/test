from __future__ import unicode_literals
import youtube_dl
import requests
import pyglet
import os
import eyed3
#pip install requests
#pip install eyed3
#pip uninstall python-magic
#pip install python-magic-bin==0.4.14
print('Hello this is TK music app')
print('Pick one of a options:')

player = pyglet.media.Player()


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


def show_all_song_name(song_list):
    for root, dirs, files in os.walk('./'):
        count_i = 1
        for f in files:
            filename = os.path.join(root, f)
            if filename.endswith('.mp3'):
                print('{}. {}'.format(count_i, filename.replace('./', '').replace('.mp3', "")))
                count_i += 1
                song_list.append(filename.replace('./', '').replace('.mp3', ""))


run = True
while run == True:

    # taking valid input
    input_taking = True
    while input_taking == True:
        print("Main Menu:")
        print('1. Show ALL songs')
        print('2. Show detail of a song')
        print('3. Play a song')
        print('4. Search and download songs')
        print('5. Exit')
        try:
            user_Choice = int(input('>>>'))
            if user_Choice - 1 in range(5):
                input_taking = False
            else:
                raise ValueError
        except ValueError:
            print("Sorry, Please enter only a number from range 1 to 5")

    if user_Choice == 1:
        show_all_song_name([])
        input('Press any key to continue ......')

    elif user_Choice == 2:
        song_list = []
        show_all_song_name(song_list)

        # taking valid input
        input_taking = True
        while input_taking == True:
            try:
                choice = int(input('Enter song number')) - 1
                if choice in range(len(song_list)):
                    input_taking = False
                else:
                    raise ValueError
            except ValueError:
                print("Sorry, Please enter only a number from range 1 to {}".format(len(song_list)))

        audio = eyed3.load(song_list[choice] + '.mp3')
        print("FILE NAME: {}".format(song_list[choice]))
        print("DURATION: {} SECONDS".format(audio.info.time_secs))
        print("SIZE: {} BYTES".format(audio.info.size_bytes))
        input('Press any key to continue ......')

    elif user_Choice == 3:
        song_list = []
        show_all_song_name(song_list)

        # taking valid input
        input_taking = True
        while input_taking == True:
            try:
                choice = input('Enter song number to start playing or Enter (n) no go exit')
                if choice == 'n':
                    input_taking = False
                else:
                    choice = int(choice) - 1
                if choice in range(len(song_list)):
                    input_taking = False
                else:
                    raise ValueError
            except ValueError:
                if choice != 'n':
                    print("Sorry, Please enter only a number from range 1 to {}".format(len(song_list)))

        if choice != 'n':
            source = pyglet.media.load('{}.mp3'.format(song_list[choice]))
            player.queue(source)
            play_disc = 'on'
            player.play()
            while play_disc == 'on':
                choice = input('Enter playback option (play, pause, stop)')
                if choice == 'play':
                    player.play()
                elif choice == 'pause':
                    player.pause()
                elif choice == 'stop':
                    player.delete()
                    play_disc = 'off'
                else:
                    print("Sorry, your command is Invalid")

    elif user_Choice == 4:
        search_keyword = input('Enter the song you want to search')
        print('Searching for songs, please wait ....')
        url = "https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&maxResults=5&q={}" \
            "&key=AIzaSyA9gQZ-oYomFypZN7PsupZJtOfQqA6Q3qw".format(search_keyword)
        response = requests.get(url).json()

        count = 1
        for data in response['items']:
            print('{}. {}'.format(count, data['snippet']['title']))
            count += 1
        print('Enter the song position you want to download')
        print("Enter (n) if you don't want to download anything")

        # taking valid input
        input_taking = True
        while input_taking == True:
            song_position = input('>>>')
            if song_position != 'n':
                try:
                    song_position = int(song_position) - 1
                    if song_position in range(5):
                        input_taking = False
                    else:
                        raise ValueError
                except ValueError:
                    if song_position != 'n':
                        print("Sorry, Please enter only a number from range 1 to 5 to download or Enter (n) to escape")
            else:
                input_taking = False

        if song_position != 'n':
            # download a song by its position
            url_to_download = 'https://www.youtube.com/watch?v={}'.format(
                response['items'][song_position]['id']['videoId'])
            song_name = response['items'][song_position]['snippet']['title']

            print("Dowloading {} .....".format(song_name))
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_to_download])
                info_dict = ydl.extract_info(url_to_download, download=False)
                song_name = ydl.prepare_filename(info_dict)
            print('Done')

            play_option = input('Do you want to play it? (y/n)')
            source = pyglet.media.load("./{}".format(song_name.replace('.webm', '.mp3')))
            player.queue(source)
            if play_option == 'y':
                player.play()
                play_disc = 'on'
                while play_disc == 'on':
                    choice = input('Enter playback option (play, pause, stop)')
                    if choice == 'play':
                        player.play()
                    elif choice == 'pause':
                        player.pause()
                    elif choice == 'stop':
                        player.delete()
                        play_disc = 'off'
                    elif choice != 'n':
                        print('Command Invalid !!!')

    elif user_Choice == 5:
        run = False