##qtile
cd /usr/share/xsessions
sudo wget https://raw.githubusercontent.com/qtile/qtile/master/resources/qtile.desktop
sudo apt install python3 python3-pip -y
pip3 install xcffib
pip3 install --no-cache-dir cairocffi
sudo apt-get install libpangocairo-1.0-0 python-dbus -y
git clone git://github.com/qtile/qtile.git
cd qtile
pip install .
cd ~/.config/
mkdir qtile
cd qtile
wget https://raw.githubusercontent.com/HarryPEthan870/.dotfiles/master/.config/qtile/autostart.sh
wget https://raw.githubusercontent.com/HarryPEthan870/.dotfiles/master/.config/qtile/config.py
