# Project features

- **Efficient Data Storage with PostgreSQL**: Leverages [PostgreSQL](https://www.postgresql.org/) as the primary database, optimizing for high-performance queries and data integrity.
- **Containerized Deployment**: Uses [**Docker containers**](https://www.docker.com/) to ensure consistency across different environments and simplify deployment.
- **Automated OpenAPI Generation**: [OpenAPI](https://www.openapis.org/) documentation is generated directly from **Python code** using [flask-openapi3](https://github.com/luolingchun/flask-openapi3) extension
- **Comprehensive API Documentation**: A dedicated documentation page is generated using [Swagger UI](https://swagger.io/tools/swagger-ui/), providing an interactive **API exploration tool**.
- **Object-Relational Mapping with SQLAlchemy**: Uses [SQLAlchemy](https://www.sqlalchemy.org/) ORM to simplify database interactions and improve maintainability.
- **Database Migrations with Alembic**: Uses [Alembic](https://alembic.sqlalchemy.org/en/latest/) for version-controlled database schema migrations.
- **Dependency Management with Dependency Injector**: Utilizes [Dependency Injector](https://github.com/ets-labs/python-dependency-injector) for structured and maintainable dependency management.
- **Automated Cryptocurrency Price Updates**: Uses [Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) workers to periodically fetch and update cryptocurrency prices.

# Project usage

## Running project with Docker Compose

### Prerequisites

1. Ensure you have one of the following installed:

   - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - [Docker Engine](https://docs.docker.com/engine/)

### Usage guide

1. Clone the repository to your preferred location:

   ```sh
   git clone https://github.com/Filiup/crypto_api.git
   ```

2. Navigate to the project directory and create **.env.secret** file

   Add your [Coingecko API key](https://www.coingecko.com/en/developers/dashboard) to the file:

   ```sh
   COINGECKO_API_KEY=YOUR_COINGECKO_API_KEY
   ```

3. Start the application using **Docker Compose**

   ```sh
   docker compose up -d
   ```

   This command will start **docker containers**:

   - **Redis** – accessible on port `6370`
   - **PostgreSQL** – accessible on port `5430`
   - **Crypto API**– exposes REST API on port `9101`
   - **Celery worker** -A background process responsible for updating **cryptocurrency** data in **PostgreSQL**.
   - **Celery beat** - **Schedules** and **triggers** the **Celery Worker** at predefined intervals.
     - The execution interval (in minutes) is configurable via the **.env** file.

4. Apply database migrations

   Before using the application, apply database migrations by running:

   ```sh
   make migration_run
   ```

### **Accessing API Documentation**

Once the application is running, the **Swagger UI** interactive documentation is available at:

👉 [**http://localhost:9101/openapi/**](http://localhost:9101/openapi/)

This allows you to **explore** and **test** the **API endpoints** directly from your browser.
