from nameko.rpc import rpc
import db
from db import Humidity
from psycopg2 import OperationalError


class HumidityServer():
    name = "humidity_server"

    @rpc
    def receive_humidity(self, humidity):
        humidity = int(humidity)
        h = Humidity()
        h.value = humidity
        try:
            db.session.add(h)
            db.session.commit()
        except OperationalError:
            db.session.rollback()
        return humidity
