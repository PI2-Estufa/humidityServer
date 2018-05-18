from nameko.rpc import rpc
from nameko.messaging import Publisher
from kombu import Echange, Queue

exchange = Exchagen("main", "direct", durable=True)
queue = Queue("humidity_queue", exchange=exchange)

class Humidity():
    name = "humidity_server"
    publish = Publisher(exchange=exchange, queue=queue)

    @rpc
    def receive_humidity(self, humidity):
        h = Humidity()
        return humidity
