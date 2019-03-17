# Raspberry Pi TensorFlow machine learning object detecting blind spot camera and warning system for vehicles
Made for the PA Pi Competition 2019

## The need and function of this project
![Cyclist](https://github.com/nuast/rpiTensorflowBlindspot/blob/master/documentation/pexels-photo-1458935.jpeg)
Cyclists and pedestrians are 15 times more likely than drivers to be killed on UK roads. In a society where we’re trying to desperately to promote environmentally friendly modes of transport, we’re instead unwillingly discouraging them with the safety risks. The cyclist safety movement usually focuses on the cyclist, wearing high-visibility clothing and covering bikes with flashing lights. However, these methods are only effective when seen. Many cyclists get seriously injured or even killed in blind spots, especially when the vehicles are turning, hence for the need of our project; an object detecting blind spot camera that warns both drivers and those at risk in the blind spot.

When a bike or pedestrian enters the blindspot (both identified in code as a “person”), the driver will be notified through an audible tone and text-to-speech message*. The pedestrian or bike at risk will be warning through an 8x8 LED matrix hat attached to the Pi, placed in view of the vehicle’s blind spot that will flash a warning when detected, alerting the pedestrian or cyclist of the risk.

[Read the full summary](https://github.com/nuast/rpiTensorflowBlindspot/blob/master/documentation/summary.md)

<sub><sup>*Text-to-speech features are not present in v1 due to [compatibility issues](https://github.com/nuast/rpiTensorflowBlindspot/issues/1)</sub></sup>
## Videos
A video summary of this project
[![gpxdznTmUTI](http://img.youtube.com/vi/gpxdznTmUTI/0.jpg)](http://www.youtube.com/watch?v=gpxdznTmUTI)
Final Software Tweaks Stream in which this project is completed
[![okay epic](http://img.youtube.com/vi/T4XK5zXsulg/0.jpg)](http://www.youtube.com/watch?v=T4XK5zXsulg)
Video of this project working is coming soon.

## Development Images
![Development](https://raw.githubusercontent.com/nuast/rpiTensorflowBlindspot/master/documentation/IMG_20190311_123431.jpg)
Editing the object detection code using nano.
![d2](https://raw.githubusercontent.com/nuast/rpiTensorflowBlindspot/master/documentation/Screenshot%20from%202019-03-17%2014-58-13.png)
Programming using Visual Studio Code.

## Installation guide:
Requirements:

Raspberry Pi 3 (different models may work but not at a frame rate that would be considered effective or safe for this project)

A 32 GB+ SD card with respectable speed. We suggest SanDisk Extreme microSD cards for this project.

A USB webcam with at least 640x480 in resolution that has drivers capable of taking still frames

Speaker

Pimoroni Unicorn HAT - [purchace](https://shop.pimoroni.com/products/unicorn-hat?variant=932565325&gclid=CjwKCAjwmq3kBRB_EiwAJkNDp7C9s3s6A3OEfNFTWRie_01ICHxPHcLrRpQghucTTW0C2z8eRGPvKRoCeh8QAvD_BwE)

Time required:
About 15 mins installation if flashing image provided.
Over a day if you want to manually build and install TensorFlow.

**WARNING**: It is important that the Raspberry Pi is fitted with a heatsink or else it is highly likely that the Pi will overheat, perform poorly and power off (*or even potentially damage your hardware*)!

### Recommended method: Flash pre-built image
First, download the latest system image from the Google Drive link on the latest [release](https://github.com/nuast/rpiTensorflowBlindspot/releases). Then, flash the SD card to your Pi using the tool of your choice, put the SD card into the Pi, plug it in and wait for the device to initialize (can take a few mins). Once initialized, the UnicornHat will scroll "Ready".

### VERY ADVANCED AND TIME-CONSUMING: building and installing Tensorflow on the Pi
[Follow this tutorial](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi) to install TensorFlow onto your Pi, along with all other requirements. Then cd into your object detection model folder and run
```
git clone https://github.com/nuast/rpiTensorflowBlindspot
```
Run the main script as superuser (i.e using sudo) and check for errors.
#### Usage
When fully set up, plug in the Pi and it should boot into the Python script which will take one to two mins to initalise.
### Who made this and when:
Project start: Friday 1st March

Installation and building of Tensorflow and object models: Wednesday 6th March - Saturday 10th March

Programming: Monday, March 10th - Saturday, March 16th

Deadline: Monday, March 18th

This project was programmed, tested, documented and completed in just over two weeks by [@ed6767](https://github.com/ed6767), [@retroaspie](https://github.com/retroaspie) and [@DRagaven](https://github.com/DRagaven) and is provided under the MIT Licence.
