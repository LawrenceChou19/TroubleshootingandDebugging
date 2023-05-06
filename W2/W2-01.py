#This tool lets us see which currently running processes are using the most CPU time.
top
iotop iftop

logrotate

ab -n 500 site.example.com/
ab -n 500 www.coursera.org/

#create webserver on ubuntu

sudo apt update
sudo apt install apache2
vi /var/www/html/index.html
sudo vi /var/www/html/index.html
sudo apt install vim


#webserver
ssh webserver
top

#the higher the priority. Typical numbers go from 0(high) to 19(low). By default
#ffmpeg is vedio program
for pid in $(pidof ffmpeg); do renice 19 $pid; done
#ps ax which shows us all the running processes on the computer
ps ax | less
/ffmpeg
#locate command find specific file on local drive
#static/001.webm is a example ffmpeg file on coursera
locate static/001.webm
#check the path is exist
cd /srv/deploy_videos/
#check file permission and list on the path 
ls -l
#create folder and file
sudo mkdir deploy_videos
sudo touch deploy.sh
#grep can find the specific words in the file 
#Practice shows deploy.sh:#This script runs ffmped in parallel to convert all of the webm files to mp4.
grep ffmpeg *
#continued modify deploy.sh 
vim deploy.sh
#kill all ffmpeg processes
killall -STOP  ffmpeg

#Inside the for loop, we want to send the cont signal and then wait until the process is done. 
# Unfortunately, there's no command to wait until the process finishes. 
# But we can create a while loop that sends the cont signal to the process. 
# This will succeed as long as the process exists, and fails once the process goes away. 
# Inside this while loop, we'll simply add a call to sleep one
for pid in $(pidof ffmpeg); do ; done
for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done