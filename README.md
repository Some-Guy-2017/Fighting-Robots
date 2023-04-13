# Fighting-Robots
A project where we attempt to build two robots to FIGHT TO THE DEATH.

Each robot has some health, a laser, and a laser receiver. You shoot the laser, trying to hit the receiver. If you do, the other robot's health decrements. Last one standing wins!

## How to dd the Pi Image
Steps to copy the pi image from one SD card to another.\n
Based on [this askubuntu question](https://askubuntu.com/questions/227924/sd-card-cloning-using-the-dd-command).

`code()`

[insert the good micro sd]
joe@joe-ubuntu-20:~/iso$ df -h
joe@joe-ubuntu-20:~/iso$ sudo umount /dev/sda1
joe@joe-ubuntu-20:~/iso$ sudo umount /dev/sda2
joe@joe-ubuntu-20:~/iso/pi$ sudo dd if=/dev/sda of=~/iso/pi/pi_img.img bs=4M status=progress
7939817472 bytes (7.9 GB, 7.4 GiB) copied, 415 s, 19.1 MB/s
1895+0 records in
1895+0 records out
7948206080 bytes (7.9 GB, 7.4 GiB) copied, 415.809 s, 19.1 MB/s
[wait a while, ~10min?]
[swap out for the micro sd you want to copy to]
joe@joe-ubuntu-20:~/iso$ sudo umount /dev/sda1
joe@joe-ubuntu-20:~/iso$ sudo umount /dev/sda2
joe@joe-ubuntu-20:~/iso/pi$ sudo dd of=/dev/sda if=~/iso/pi/pi_img.img bs=4M status=progress
