# Use an official Python runtime as a parent image
FROM python:3.11.9-slim-bullseye as builder

# Set arguments
ARG POETRY_VERSION=1.8.3

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install the dependencies using Poetry
RUN poetry install --no-root --without dev

# Use an official Python runtime as a parent image
FROM python:3.11.9-slim-bullseye as runtime

# Setup the Virtual Environment
ARG VIRTUAL_ENV=/app/.venv
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Update the PATH environment
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copy the rest of the application code into the container
COPY src ./

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["fastapi", "run", "src/main.py"]
