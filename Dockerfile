# Use an official Python runtime as a parent image
FROM python:3.11.9-slim-bullseye as builder

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock src ./

# Set arguments
ARG POETRY_VERSION=1.8.3
RUN python -m venv .venv

# Install Poetry
RUN . .venv/bin/activate && \
 pip install "poetry==$POETRY_VERSION" && \
 poetry install && \
  ls -ls .venv/bin/
ENV PATH="/app/.venv/bin:$PATH"

# Expose port 8080
EXPOSE 8080

