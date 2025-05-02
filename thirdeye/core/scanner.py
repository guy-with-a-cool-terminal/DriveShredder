import shodan
import os
from dotenv import load_dotenv

load_dotenv()
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
api = shodan.Shodan(SHODAN_API_KEY)

def shodan_search(query, region, limit=10, mock=False):
    if mock:
        return {
            "matches": [
                {
                    "ip_str": "102.69.45.12",
                    "port": 554,
                    "org": "Safaricom Ltd",
                    "product": "Hikvision DVR"
                },
                {
                    "ip_str": "196.201.208.45",
                    "port": 23,
                    "org": "Zuku Fiber",
                    "product": "Unknown Telnet Device"
                },
                {
                    "ip_str": "41.90.132.177",
                    "port": 80,
                    "org": "Jamii Telecommunications",
                    "product": "Generic Web Server"
                }
            ]
        }
    
    full_query = f"{query} country:{region}"
    results = api.search(full_query, limit=limit)
    return results
