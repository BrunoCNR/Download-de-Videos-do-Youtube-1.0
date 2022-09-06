from pytube import YouTube, Playlist
from time import sleep

print('ESCOLHA A OPÇÃO DE DOWNLOAD')
print('1 -- DOWNLOAD VIDEO UNICO')
print('2 -- DOWNLOAD DE PLAYLIST')
print('3 -- DOWNLOAD SOMENTE AUDIO VIDEO UNICO')
print('4 -- DOWNLOAD PLAYLIST AUDIO')

um = int(input('Digite a opção desejada : '))
if um == 1:
    url = input('Digite o link do Download :')
    print('*' * 50)
    local = input('Local de Download: ')
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('{}'.format(local))
    print("FAZENDO DOWNLOAD DO VIDEO")
    sleep(2)
    print('Descrição do video : ' + youtube.title)

elif um == 2:
    url = input("Digite a PLAYLIST do Download :")
    print('Para Selecionar o local de Download, comece sempre pela unidade C: ou D:')
    local = input('Local de Download: ')
    youtube_playlist = Playlist(url)
    for video in youtube_playlist.videos:
        video.streams.get_highest_resolution().download('{}'.format(local))
        print("Download finalizado: ", video.title)
    print('DOWNLOAD FINALIZADO')

elif um == 3:
    url = input('Digite o link do Download :')
    print('*' * 50)
    print('Para Selecionar o local de Download, comece sempre pela unidade C: ou D:')
    loc = input('Local de Download: ')
    audio = YouTube(url)
    video = audio.streams.get_audio_only()
    video.download('{}'.format(loc))
    print("FAZENDO DOWNLOAD DO VIDEO")
    sleep(2)
    print('Descrição do video : ' + audio.title)
    print('Download Finaliado....')

elif um == 4:
    url = input("Digite a PLAYLIST do Download :")
    print('Para Selecionar o local de Download, comece sempre pela unidade C: ou D:')
    local = input('Local de Download: ')
    playlist_audio = Playlist(url)
    for video in playlist_audio.videos:
        video.streams.get_audio_only('{}'.format(local))
        print("Download finalizado: ", video.title)
    print('DOWNLOAD FINALIZADO')

else:
    print('Opção inválida, reinicie a operação ! ')
