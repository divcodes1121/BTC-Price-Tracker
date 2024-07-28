import time
import requests
from alerts.models import Alert
from alerts.tasks import send_alert_email

def get_current_price():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
        'vs_currency': 'USD',
        'ids': 'bitcoin'
    })
    data = response.json()
    return data[0]['current_price']

while True:
    current_price = get_current_price()
    alerts = Alert.objects.filter(triggered=False)

    for alert in alerts:
        if current_price >= alert.price:
            alert.triggered = True
            alert.save()
            # Send email using Celery
            send_alert_email.delay(
                alert.user.email,
                alert.price,
                current_price
            )
    time.sleep(60)
