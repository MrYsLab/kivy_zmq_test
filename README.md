This is a very hacked up example of using zmq with Kivy. It only runs on a PC. Creating an APK with buildozer does not work.

Strangely enough, umspack alone causes no issues with the buildozer APK.

To run this project:

1. Go to kivy_zmq_test/xibotics/utils and start hub.py

The hub is a [zmq forwarder](http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/forwarder.html) 
2. In another terminal window, start monitor.py

This will display all messages on the zmq network

3. In yet another terminal window, in kivy_zmq_test/xibot_control_gui/ start main.py to bring up the GUI.

4. Click on the "Left Encoder button"

The monitor should output the following message:

PUB TOPIC: I am a topic PAYLOAD: I am a payload