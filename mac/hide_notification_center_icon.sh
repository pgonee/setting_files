#!/bin/bash

sudo launchctl remove com.apple.notificationcenterui.agent
sudo launchctl unload -w /System/Library/LaunchAgents/com.apple.notificationcenterui.plist
sudo killall NotificationCenter

