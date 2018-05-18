from nameko.rpc import rpc
from nameko.messaging import Publisher
from kombu import Exchange, Queue
import db
from db import Humidity

exchange = Exchange("main", "direct", durable=True)
queue = Queue("humidity_queue", exchange=exchange)


class HumidityServer():
    name = "humidity_server"
    publish = Publisher(exchange=exchange, queue=queue)

    @rpc
    def receive_humidity(self, humidity):
        h = Humidity()
        h.value = humidity
        db.session.add(h)
        db.session.commit()
        self.publish(humidity)
        return humidity
