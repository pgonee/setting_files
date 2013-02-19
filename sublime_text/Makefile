UNAME := $(shell uname)

CURRENT_PATH=$(shell pwd)

MAC_HOME_PATH=$(shell echo ~)
MAC_BINARY_PATH=/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl
MAC_SUBL_PATH=$(MAC_HOME_PATH)/Library/Application\ Support/Sublime\ Text\ 2/Packages/User
MAC_SUBL_PREF_FILE=Preferences.sublime-settings
MAC_SUBL_KEY_FILE=Default\ \(OSX\).sublime-keymap

SHORTCUT_PATH=/usr/bin
SHORTCUT_NAME=subl
SHORTCUT=$(SHORTCUT_PATH)/$(SHORTCUT_NAME)

all: clean
ifeq ($(UNAME), Darwin)
	mv $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE) $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE).back
	mv $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE) $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE).back
	ln -s $(CURRENT_PATH)/$(MAC_SUBL_PREF_FILE) $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE)
	ln -s $(CURRENT_PATH)/$(MAC_SUBL_KEY_FILE) $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE)
	sudo ln -s $(MAC_BINARY_PATH) $(SHORTCUT)
endif
ifeq ($(UNAME), Linux)
	cp ./Preferences.sublime-settings ~/.config/sublime-text-2/Packages/User/
endif

clean:
ifeq ($(UNAME), Darwin)
	if [ -a $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE).back ]; \
		then \
			mv $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE).back $(MAC_SUBL_PATH)/$(MAC_SUBL_PREF_FILE); \
	fi
	if [ -a $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE).back ]; \
		then \
			mv $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE).back $(MAC_SUBL_PATH)/$(MAC_SUBL_KEY_FILE); \
	fi
	if [ -a $(SHORTCUT) ]; \
		then \
			sudo rm $(SHORTCUT); \
	fi
endif
