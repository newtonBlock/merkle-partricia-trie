# Merkle Patricia Trie

## Setup

To use, create a python2 virtualenv with miniconda:
`conda create --name yourNameEnv python=2.7`

Then, activate the virtualenv with:
`source activate yourNameEnv`

Last, quit the virtual env
`source deactivate`
 
Now install dependencies:
`pip install -r requirements.txt`

bitcoin==1.1.42 can be installed
leveldb and sha3 have to be upgrade, using new version

If got error using pip install leveldb that `include path for stdlibc++ headers not found`;
Amending the flag CPPFLAG priot to my pip install

export CPPFLAGS = "-stdlib=libc++"

## Credits
Code is based from:
http://easythereentropy.wordpress.com/2014/06/04/understanding-the-ethereum-trie/

Hopefully, this will help those confused soles who have yet to grasp the trie
