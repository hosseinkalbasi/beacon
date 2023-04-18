from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class EventData(BaseModel):
    event_name: str
    timestamp: datetime


class BeaconData(BaseModel):
    page_location: str
    page_start: datetime
    page_end: Optional[datetime]
    events: Optional[List[EventData]]

    class Config:
        schema_extra = {
            "example": {
                "page_location": "https://google.com/blog/how-to-test-2",
                "page_start": "2023-03-30T11:43:16.029Z",
                "page_end": "2023-03-30T12:43:16.029Z",
                "events": [
                    {
                        "event_name": "page_view",
                        "timestamp": "2023-03-30T11:43:16.029Z",
                    }
                ],
            }
        }
