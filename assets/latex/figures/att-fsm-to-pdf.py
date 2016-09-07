
import sys
import getopt

def print_usage_and_die():
  print >> sys.stderr, "usage: python att-fsm-to-pdf.py [-t|--isfst] [-f|--stxtfile filename]"
  sys.exit(2)

def create_files(stream):
  try: stream = open(stxtfile, 'r')
  except: print_usage_and_die()
  for line in stream:
    line = line.strip()
    print line
  stream.close()

def att_fsm_to_pdf(isfst, stxtfile):
  create_files(stxtfile)

if __name__ == '__main__':
  try:
    (isfst, stxtfile) = (0, None)
    opts, args = getopt.getopt(sys.argv[1:], "tf:", ["isfst", "stxtfile="])
  except getopt.GetoptError:
    print_usage_and_die()

  for o, a in opts:
    if o in ("-t", "--isfst"):
      isfst = 1
    if o in ("-f", "--file"):
      stxtfile = a

  if (stxtfile == None): print_usage_and_die()
  att_fsm_to_pdf(isfst, stxtfile)

