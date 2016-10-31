#!/usr/bin/python

import sys
import email
import os
import re

def get_message_body(message):
    """Takes an email.message object and returns the body of the
    message.  A wrapper function is needed because the message might
    be multipart."""
    body = ""
    for part in message.walk():

        if part.get_content_type() == "text/plain":
            body += part.get_payload()

    return body

def extract_email(string):
    """ Accepts an email address field and extracts just the email
    portion of it.  For example, extract_email("Matt Post
    <post@jhu.edu>") will return "post@jhu.edu" """

    m = re.search('[\w_.]+@[\w.]+', string)
    return m.group(0)

raw_data = ""
for line in sys.stdin.readlines():
    raw_data = raw_data + line

message = email.message_from_string(raw_data)
sender = message.get('from')
subject = message.get('subject')
body = get_message_body(message)
email = extract_email(sender)

outdir = '/users/post/code/mt-class/stack-decoder/data/'
if not os.path.exists(outdir):
    os.makedirs(outdir)

for i,line in enumerate(body.split('\n')):
    tokens = line.split()
    if len(tokens) >= 2:
        word = tokens[1].replace('=','').lower()
        outfile = open(os.path.join(outdir,'%s.%s.txt' % (email,i)), 'w')
        outfile.write(word + '\n')
        outfile.close()

