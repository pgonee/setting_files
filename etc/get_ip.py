import urllib

def get_ip():
    a = urllib.urlopen("http://ipconfig.co.kr")
    a = a.read()
    tmp = a.index("IP address")
    a = a[tmp:tmp+60]

    current_list = ["1","2","3","4","5","6","7","8","9","0","."]
    result = ""
    for char in a:
        if char in current_list:
            result += char
    return result


if __name__ == "__main__":
    print get_ip()
