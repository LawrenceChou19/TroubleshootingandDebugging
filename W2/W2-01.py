#This tool lets us see which currently running processes are using the most CPU time.
top

ab -n 500 site.example.com

ssh webserver

for pid in $(pidof ffmpeg); do renice 19 $pid; done

