__version__ = "1.0"

import socket
import sys
import time

import umsgpack
import zmq

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from kivy.garden.knob import Knob

import time
import signal
import sys
import umsgpack
import zmq
from xibotics.utils.xibotbase.xibotbase import XiBotBase

class MainWidget(Widget):
    pass

class XibotControlApp(App):


    def __init__(self,  router_ip_address=None, subscriber_port='43125', publisher_port='43124'):
        # print('control init')
        super().__init__()
        # If no router address was specified, determine the IP address of the local machine
        if router_ip_address:
            self.router_ip_address = router_ip_address
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # use the google dns
            s.connect(('8.8.8.8', 0))
            self.router_ip_address = s.getsockname()[0]

        # print('\n**************************************')
        # print('Using router IP address: ' + self.router_ip_address)
        # print('**************************************')

        self.subscriber_port = subscriber_port
        self.publisher_port = publisher_port

        # establish the zeriomq sub and pub sockets
        self.context = zmq.Context()
        self.subscriber = self.context.socket(zmq.SUB)
        connect_string = "tcp://" + self.router_ip_address + ':' + self.subscriber_port
        self.subscriber.connect(connect_string)

        self.publisher = self.context.socket(zmq.PUB)
        connect_string = "tcp://" + self.router_ip_address + ':' + self.publisher_port
        self.publisher.connect(connect_string)
        Clock.schedule_interval(self._zmq_read, .0001)
        # Clock.ClockBaseInterrupt(self.zmq_read, .2)

    def _zmq_read(self, dt):
        data = None
        # print(time.time())
        try:
            data = self.subscriber.recv_multipart(zmq.NOBLOCK)
            self.incoming_message_processing(data[0].decode(), umsgpack.unpackb(data[1]))
            time.sleep(.001)
        except zmq.error.Again:
            time.sleep(.001)
        except KeyboardInterrupt:
            self.clean_up()

    def publish_payload(self, payload, topic=''):
        """
        This method will publish a payload with the specified topic.

        :param payload: A dictionary of items
        :param topic: A string value
        :return:
        """
        if not type(topic) is str:
            raise TypeError('Publish topic must be a string', 'topic')

        # create a message pack payload
        message = umsgpack.packb(payload)

        pub_envelope = topic.encode()
        self.publisher.send_multipart([pub_envelope, message])
        # self.publisher.send_multipart([pub_envelope, payload])


    def incoming_message_processing(self, topic, payload):
        """
        Override this method with a message processor for the application

        :param topic: Message Topic string
        :param payload: Message Data
        :return:
        """
        pass
        # print('this method should be overwritten in the child class', topic, payload)

    def clean_up(self):
        """
        Clean up before exiting - override if additional cleanup is necessary

        :return:
        """
        self.publisher.close()
        self.subscriber.close()
        self.context.term()
        self.stop()
        sys.exit(0)


    def build(self):
        return MainWidget()

    def left_spin_pressed(*args):
        # print('left spin pressed')
        pass

    def right_spin_released(*args):
        pass
        # print('right spin released')


if __name__ == '__main__':
    XibotControlApp().run()
