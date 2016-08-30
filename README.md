This is a very hacked up example of using zmq with Kivy. It only runs on a PC. Creating an APK with buildozer does not work.

Strangely enough, umspack alone causes no issues with the buildozer APK.

To run this project:

First: Go to kivy_zmq_test/xibotics/utils and start hub.py

The hub is a [zmq forwarder](http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/forwarder.html)
 
Second: In another terminal window, start monitor.py

This will display all messages on the zmq network

Third: In yet another terminal window, in kivy_zmq_test/xibot_control_gui/ start main.py to bring up the GUI.

Fourth: Click on the "Left Encoder button"

The monitor should output the following message:

PUB TOPIC: I am a topic PAYLOAD: I am a payload

ALL THREE COMPONONENTS USE THE ADDRESS OF THE HOST COMPUTER. If building an APK, hardcode the IP address that the hub reports into main.py `__init__()`
. The router_address paramenter should be chnaged from None to that address.
