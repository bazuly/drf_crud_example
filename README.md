# Library CRUD Application with PostgreSQL, Celery, and RabbitMQ

This is a simple CRUD example application for managing a library system, implemented with Django rest framework, PostgreSQL, Celery, and RabbitMQ. It allows authenticated users to create, retrieve, update, and delete library records while leveraging Celery for background task processing.

---

## **Features**

- **CRUD Operations**: Create, Read, Update, and Delete library records.
- **Background Tasks**: Asynchronous processing of notifications using Celery.
- **Database**: PostgreSQL for efficient data storage and retrieval.
- **Message Queue**: RabbitMQ for managing message queues and ensuring task reliability.
- **REST API**: Fully functional REST API with filters and pagination.
- **Dockerized**: All services are containerized using Docker for easy deployment.

---

## **Tech Stack**

- **Backend**: Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Task Queue**: Celery with RabbitMQ as the message broker
- **Cache**: Redis for result backend
- **Containerization**: Docker & Docker Compose

---

## **Prerequisites**

Before running the application, ensure you have the following installed:

- Docker
- Docker Compose

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/drf_crud_example.git
   cd drf_crud_example
   docker-compose up --build -d 
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser

2. API Tests

   ```bash
   docker-compose run test

