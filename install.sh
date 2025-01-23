#!/bin/bash
# version v0.0.1
SDK_DIRECTORY=${BIN_DIRECTORY:=/home/$USER/pysh-v0.0.1}
BIN_DIRECTORY=${BIN_DIRECTORY:=/home/$USER/pysh-v0.0.1/bin}
echo -e "\n"
echo  ______   __  __     ______     __  __     ______     _____     __  __    
echo /\  == \ /\ \_\ \   /\  ___\   /\ \_\ \   /\  ___\   /\  __-.  /\ \/ /    
echo \ \  _-/ \ \____ \  \ \___  \  \ \  __ \  \ \___  \  \ \ \/\ \ \ \  _!-.
echo  \ \_\    \/\_____\  \/\_____\  \ \_\ \_\  \/\_____\  \ \____-  \ \_\ \_\ 
echo   \/_/     \/_____/   \/_____/   \/_/\/_/   \/_____/   \/____/   \/_/\/_/ 
echo -e "\n"
sleep 2
echo Moving files...
echo -e "\n"
mv $BIN_DIRECTORY/bin.zip $SDK_DIRECTORY/bin.zip
sleep 1
echo Decompressing files...
echo -e "\n"
unzip 'bin.zip'
sleep 1
echo Creating access...
echo -e "\n"
cd Escritorio
echo chmod +x /home/$USER/pysh-v0.0.1/start.sh && /home/$USER/pysh-v0.0.1/start.sh> pysh.sh
cd..
wait 1
echo Done!
echo -e "\n"
notify-send "PYSH.SDK has been successfully installed!"
wait 2
# destroy
rm -f install.sh