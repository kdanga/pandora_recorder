import subprocess
import parser
import re

def main():
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
    else:
      print 'no results'
    output = p.stdout.readline().rstrip()

if __name__ == '__main__':
  main()