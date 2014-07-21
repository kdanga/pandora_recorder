import subprocess

def sub():
  try:
    cmd = 'pianobar'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    output = p.stdout.readline()
  except:
    pass

  while(output):
    print output
    output = p.stdout.readline()

def main():
  print 'test'

if __name__ == '__main__':
  main()