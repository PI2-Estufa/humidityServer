from nameko.rpc import rpc
import db
from db import Humidity


class HumidityServer():
    name = "humidity_server"

    @rpc
    def receive_humidity(self, humidity):
        humidity = int(humidity)
        h = Humidity()
        h.value = humidity
        db.session.add(h)
        db.session.commit()
        return humidity
