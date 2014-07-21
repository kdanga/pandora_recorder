import unittest
import re

def parse_pianobar_line(line):
  """Takes a pianobar output line containing the song info, (song, artist and album).
  It parses the information and returns the data as a dictionary.
  """

  results = {}
  try:
    re_line = '|>' + line.split('|>')[1]
  # Not a line containing song info
  except IndexError:
    return results

  match = re.match(r'\|>  "(.*)" by "(.*)" on "(.*)"', re_line)
  if match:
    results['song'] = match.group(1)
    results['artist'] = match.group(2)
    results['album'] = match.group(3)
  return results

class PianobarParserTest(unittest.TestCase):
  line1 = """|>  "(Can't Get My) Head Around You" by "The Offspring" on "Splinter (Explicit)\""""
  line2 = """|>  "Dog Days Are Over" by "Florence + The Machine" on "Lungs\""""
  line3 = '\x1b[2K|>  "Crazy" by "Gnarls Barkley" on "St. Elsewhere"'

  def _assert_values(self, result, song, artist, album):
    self.assertTrue('song' in result)
    self.assertTrue('artist' in result)
    self.assertTrue('album' in result)
    self.assertEquals(result['song'], song)
    self.assertEquals(result['artist'], artist)
    self.assertEquals(result['album'], album)

  def test_line1(self):
    results = parse_pianobar_line(self.line1)
    self._assert_values(results, "(Can't Get My) Head Around You",
                                  "The Offspring",
                                  "Splinter (Explicit)")

  def test_line2(self):
    results = parse_pianobar_line(self.line2)
    self._assert_values(results, "Dog Days Are Over",
                                  "Florence + The Machine",
                                  "Lungs")

  def test_line3(self):
    results = parse_pianobar_line(self.line3)
    self._assert_values(results, "Crazy",
                                  "Gnarls Barkley",
                                  "St. Elsewhere")

  def test_invalid_line(self):
    results = parse_pianobar_line('Not a valid line to parse')
    self.assertEquals(results, {})

if __name__ == "__main__":
  unittest.main()