
from sqlalchemy import Column, BigInteger, String, sql
from On_OFF_sensor_bot.utils.dp_api.dp_gino import TimedBaseModel


class Registration(TimedBaseModel):
    __tablename__ = 'registration_bot'
    user_id = Column(BigInteger, primary_key=True)
    tg_first_name = Column(String(200))
    tg_last_name = Column(String(200))
    name = Column(String(50))
    phone = Column(String(30))
    age = Column(String(30))
    status = Column(String(25))

    query: sql.select
