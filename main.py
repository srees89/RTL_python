multimon_ng = subprocess.Popen("rtl_fm -f 148.8125M - | multimon-ng -t raw -a FLEX -a SCOPE -f alpha /dev/stdin",
stdout=subprocess.PIPE,
                shell=True)
decoded = multimon_ng.stdout.readline().decode('utf-8')
flex,mdate, bitrate, other,capcode ,ALN ,msg = decoded.split("|",7)
mdate, mtime = mdate.split(" ",1)
capcode = str(capcode)
msg = msg.strip()
frag = bitrate.split("/", 3)
multimon_ng.poll()
