# Raspberry Pi GPIO Song Player

This simple script plays a song when GPIO pin 2 or 3 is connected to GROUND on the Raspi Pi.
It uses the `pygame` library to play the notes.

Connecting GPIO PIN 4 To GROUND will stop playing the song.


This was build for a christmas installation, where the Raspi Pi was hidden inside a piano.  Triggering the right note on the piano started playing a specific song.



## Installation

Replace 'jimmy' with your username.

Use systemd to start the script on boot.

    sudo nano /lib/systemd/system/piano.service

Add the following content:
    
    [Unit]
    Description=Piano
    
    [Service]
    Type=simple
    ExecStart=/home/jimmy/launcher.sh
    Restart=on-failure
    RestartSec=10
    User=jimmy
    Group=audio
    
    [Install]
    WantedBy=sound.target


launcher.sh:

    cd /home/jimmy
    python piano.py

