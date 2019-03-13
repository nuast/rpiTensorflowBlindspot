# Raspberry Pi TensorFlow machine learning object detecting blind spot camera and warning system for vehicles
Made for the PA Pi Competition 2019

## The need and function of this project
![Cyclist](https://github.com/nuast/rpiTensorflowBlindspot/blob/master/documentation/pexels-photo-1458935.jpeg)
Cyclists and pedestrians are 15 times more likely than drivers to be killed on UK roads. In a society where we’re trying to desperately to promote environmentally friendly modes of transport, we’re instead unwillingly discouraging them with the safety risks. The cyclist safety movement usually focuses on the cyclist, wearing high-visibility clothing and covering bikes with flashing lights. However, these methods are only effective when seen. Many cyclists get seriously injured or even killed in blind spots, especially when the vehicles are turning, hence for the need of our project; an object detecting blind spot camera that warns both drivers and those at risk in the blind spot.

When a bike or pedestrian enters the blindspot (both identified in code as a “person”), the driver will be notified through an audible tone and text-to-speech message. The pedestrian or bike at risk will be warning through an 8x8 LED matrix hat attached to the Pi, placed in view of the vehicle’s blind spot that will flash a warning when detected, alerting the pedestrian or cyclist of the risk.

## Development Images
![Development](https://raw.githubusercontent.com/nuast/rpiTensorflowBlindspot/master/documentation/IMG_20190311_123431.jpg)
Editing the object detection code using nano.
