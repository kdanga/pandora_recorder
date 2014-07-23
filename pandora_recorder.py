import subprocess
import downloader
import parser
import re

def main():
  dler = downloader.Downloader()

  try:
    cmd = 'pianobar'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    output = p.stdout.readline().rstrip()
  except:
    pass

  while(output):
    print output
    results = parser.parse_pianobar_line(output)
    if results:
      print results
      dler.download_song(results['song'], results['artist'])
    output = p.stdout.readline().rstrip()

if __name__ == '__main__':
  main()