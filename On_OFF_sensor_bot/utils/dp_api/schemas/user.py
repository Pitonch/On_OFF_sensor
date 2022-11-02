

from sqlalchemy import Column, BigInteger, String, sql

from On_OFF_sensor_bot.utils.dp_api.dp_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablenamme__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)
    updated_name = Column(String(50), primary_key=True)

    queri: sql.select
