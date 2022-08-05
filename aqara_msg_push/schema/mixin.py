# pylint: disable=no-name-in-module
from datetime import datetime

from pydantic import BaseModel, Field


class TimeMixin(BaseModel):

    raw_time: str = Field(alias='time')

    @property
    def time(self) -> float:
        return int(self.raw_time) / 1000.0

    @time.setter
    def time(self, value: float) -> None:
        self.raw_time = str(int(value * 1000))

    @property
    def dt(self) -> datetime:
        return datetime.fromtimestamp(self.time)

    @dt.setter
    def dt(self, value: datetime) -> None:
        self.time = value.timestamp()
