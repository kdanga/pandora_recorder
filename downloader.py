import grooveshark
import eyed3
import urllib2

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

client = grooveshark.Client()
client.init()

class Downloader(object):
  """
  A tool object used to download songs using the grooveshark api.
  """

  def __init__(self):
    self._client = grooveshark.Client()
    self._client.init()
    self._header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    self._music_directory = '/Users/kevin/Music/grooveshark_songs'

  def download_song(self, song, artist):
    song = self._song_query(song, artist)

    if not song:
      print "Could not find song. Is it in Grooveshark?"
      return 0

    response = song.download(directory=self._music_directory, song_name='%a - %s')

    if response:
      print "Downloaded song: %s" % response
      audfile = eyed3.load('%s/%s' % (self._music_directory, response + '.mp3'))
      self._tag_audio_file(audfile, song)


  def _song_query(self, song_name, artist_name):
    query = song_name + " " + artist_name
    results = self._client.search(query, type=self._client.SONGS)

    first_song = True
    for song in results:
      # Song must have the name
      if song_name.lower() in song.name.lower() or\
          song.name.lower() in song_name.lower():
        return song

    return None

  def _tag_audio_file(self, audfile, song):
    # Load tags for downloaded audio file
    audfile.tag.artist = unicode(song.artist)
    audfile.tag.album = unicode(song.album)
    audfile.tag.title = unicode(song.name)
    audfile.tag.track_num = int(song.track)

    # Set cover art if it avaliabe (cover usually has image in jpg format)
    if song._cover_url.endswith('jpg'):
      req = urllib2.Request(song._cover_url, headers=self._header)
      img_data = urllib2.urlopen(req).read()
      audfile.tag.images.set(3, img_data, "image/jpeg", u" ")

    audfile.tag.save()

def test_downloader():
  downloader = Downloader()
  downloader.download_song('In Myasdf Place', 'Coldplasdfay')

def main():
  test_downloader()

if __name__ == '__main__':
  main()

