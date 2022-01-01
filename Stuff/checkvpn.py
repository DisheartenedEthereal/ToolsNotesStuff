import os,sys,socket,requests
try: 
    def ipInfo(addr=''):
        from urllib.request import urlopen
        from json import load
        if addr == '':
            url = 'https://ipinfo.io/json'
        else:
            url = 'https://ipinfo.io/' + addr + '/json'
        res = urlopen(url)
        #response from url(if res==None then check connection)
        data = load(res)
        #will load the json response into data
        for attr in data.keys():
            #will print the data line by line
            print(attr,' '*13+'\t->\t',data[attr])

    for x in range(100):
        SOMEHOST = "v"+str(x)+".serspeed.info"
        HOST_UP  = True if os.system("ping -q -c 1 -w 1 " + SOMEHOST) == 0 else False
        if HOST_UP == True:
            ip = socket.gethostbyname(SOMEHOST)
            print (SOMEHOST + "-- : " )
            ipInfo(ip)
        else:
            pass
except KeyboardInterrupt:
    sys.exit()
