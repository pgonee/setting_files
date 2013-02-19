#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

def get_temp():
    rst = commands.getoutput('cat /sys/devices/platform/coretemp.0/temp1_input')
    return int(rst)

def get_max_rpm():
    rst = commands.getoutput('cat /sys/devices/platform/applesmc.768/fan1_max')
    return int(rst)

def get_rpm():
    a, b = commands.getstatusoutput('cat /sys/devices/platform/applesmc.768/fan1_min')
    return int(b)

def set_rpm(rpm_speed):
    a, b = commands.getstatusoutput('echo %d > /sys/devices/platform/applesmc.768/fan1_min' % (rpm_speed))

def main():
    min_temp = 30
    max_temp = 80
    min_rpm = 1500
    max_rpm = get_max_rpm() - 201
    current_temp = get_temp() / 1000
    #print "current : %d" % (current_temp)

    if get_rpm() > max_rpm:
        return

    if current_temp <= min_temp:
        set_rpm(min_rpm)
    #    print "min!"
    elif current_temp >= max_temp:
        set_rpm(max_rpm)
    #    print "max!"
    else:
        index = (max_rpm - min_rpm) / (max_temp - min_temp)
        rpm = 1500 + (current_temp - min_temp) * index
        set_rpm(rpm)
    #    print "hah : %d" % (rpm)

if __name__ == "__main__":
    main()
