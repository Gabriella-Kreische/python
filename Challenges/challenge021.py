import mp3play
import time

filename = r'C:\PARA GUARDAR 2\Musicas\MÚSICAS boas\06 - Wind Of Change.mp3'
clip = mp3play.load(filename)

clip.play()

time.sleep(min(30, clip.seconds()))
clip.stop()
