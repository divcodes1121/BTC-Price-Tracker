# Price Alert Application

## Overview

This application allows users to set price alerts for BTC. Users will receive an email notification when the target price is reached.

## Endpoints

- Create Alert: `/alerts/create/`
- Delete Alert: `/alerts/delete/<int:pk>/`
- Fetch Alerts: `/alerts/`

## Running the Project

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository
2. Navigate to the project directory
3. Build and start the containers:
    ```bash
    docker-compose up --build
    ```
4. Initialize the database:
    ```bash
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    ```
5. Access the application at `http://localhost:8000/`

## Notes

- The application uses Celery for task management and Redis as the message broker.
- Real-time price updates can be fetched using Binance WebSocket or CoinGecko API.
- JWT is used for user authentication.
- Email notifications are sent using Gmail SMTP.
