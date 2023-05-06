Real
user
sys

#combined with meeting_reminder
time ./send_reminders.py "2023-05-06|Example|test1"

time ./send_reminders.py "2023-05-06|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"
#install first
sudo apt install python3-pprofile 
pprofile3 -f callgrind -o profile.out ./send_reminders.py "2023-05-06|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"
