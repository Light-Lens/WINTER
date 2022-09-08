@echo off

title Train

python train.py -i intents\Chats.json -o pth\chat.pth

echo:

python train.py -i intents\Func.json -o pth\func.pth
