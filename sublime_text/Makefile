UNAME := $(shell uname)
all:
ifeq ($(UNAME), Darwin)
	mv ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/Preferences.sublime-settings ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/Preferences.sublime-settings.back
	ln ./Preferences.sublime-settings ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/Preferences.sublime-settings
	sudo ln -s /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl /usr/bin/subl
endif
ifeq ($(UNAME), Linux)
	cp ./Preferences.sublime-settings ~/.config/sublime-text-2/Packages/User/
endif
