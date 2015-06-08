# Outlook PST file search

I had a few PST files from old times, which I needed some information out of. Running OS X, without Outlook, made it difficult to get to that stuff.

So I decided to look through the internet, and found [libpff](https://github.com/libyal/libpff), which cans (sort of) parse PST files, and also has python bindings. I used the packages source version of it, because I couldn't get the development version in git to compile. Also, I used a Debian VPS for this experiment.

The code here searches for a keyword in all messages, and if it finds it, it'll write the message as a txt file into the msgs folder.

## Compiling and runing
```
apt-get install python-dev build-essential

wget https://da1ba3cfdffc2404250f16d3711dfb32dcd40e96.googledrive.com/host/0B3fBvzttpiiScU9qcG5ScEZKZE0/libpff-experimental-20131028.tar.gz
tar xvzf libpff-experimental-20131028.tar.gz 
cd libpff-20131028/
./configure --enable-python
make
make install

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib python search.py /home/severin/my_mails.pst rubberducky
```

Searches for the term "rubberducky" in the PST file "/home/severin/my_mails.pst".