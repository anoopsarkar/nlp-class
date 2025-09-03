# Anoop Sarkar: NLP Class

Course website for the NLP class at SFU in Computing Science for undergraduate and graduate students.

http://anoopsarkar.github.io/nlp-class

Cloned from https://github.com/mt-class/jhu and then modified.

## Installation

Follow the instructions here:

    https://jekyllrb.com/docs/installation/macos/

In particular:

    brew install chruby ruby-install
    ruby-install ruby 3.4.1
    source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
    source /opt/homebrew/opt/chruby/share/chruby/auto.sh
    chruby ruby-3.4.1
    ruby -v

Then:

    gem install jekyll bundler
    bundle add webrick
    bundle install

## Deploy

    bundle exec jekyll serve

