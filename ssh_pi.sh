#!/bin/bash

eval "$(ssh-agent -s)"
ssh-add rpi
ssh-copy-id pi@172.20.10.3
