# Fighting-Robots
A project where we attempt to build two robots to FIGHT TO THE DEATH.

Each robot has some health, a laser, and a laser receiver. You shoot the laser, trying to hit the receiver. If you do, the other robot's health decrements. Last one standing wins!

## How to dd the Pi Image
Steps to copy the pi image from one SD card to another.
Based on [this askubuntu question](https://askubuntu.com/questions/227924/sd-card-cloning-using-the-dd-command).

insert sd with image
/home/joe/iso: df -h
/home/joe/iso: sudo umount /dev/sda1
/home/joe/iso: sudo umount /dev/sda2
/home/joe/iso/pi: sudo dd if=/dev/sda of=/home/joe/iso/pi/pi_img.img bs=4M status=progress
7939817472 bytes (7.9 GB, 7.4 GiB) copied, 415 s, 19.1 MB/s
1895+0 records in
1895+0 records out
7948206080 bytes (7.9 GB, 7.4 GiB) copied, 415.809 s, 19.1 MB/s
(wait a while, about 10min?)
(swap out for the micro sd you want to copy to)
/home/joe/iso: sudo umount /dev/sda1
/home/joe/iso: sudo umount /dev/sda2
/home/joe/iso/pi: sudo dd of=/dev/sda if=/home/joe/iso/pi/pi_img.img bs=4M status=progress
