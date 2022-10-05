# Audio Transcript

This software was created to transcript videos into text.

## How to install

First you have to make sure you have Python installed:

```sh
# Windows
python --version

# Linux
python3 --version
```

Then you need to download this repository or clone it with git:

```sh
git clone git@github.com:RuaN-debug/Audio_Transcript.git
```

Now you have to install all the requirements for it to work:

```sh
# Windows
pip install -r requirements.txt

# Linux
pip3 install -r requirements.txt
```

Now, make sure you download the video and paste it in this directory, next to transcriptor.py file, and also copy the name and extension of the video and paste it inside the quotes of the variable called path in transcriptor.py file:

```sh
path = "name_of_video.extension"
```

At last, in order to run this script you have to type:

```sh
# Windows
python transcriptor.py

# Linux
python3 transcriptor.py
```

## Output

While it's running, it will create a few audio files with 3 minutes each to make it easier to transcript, but once it's done, all the text will be inside text.txt file and all audio files will be safely removed.