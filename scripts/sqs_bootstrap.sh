#!/bin/bash

set -euo pipefail

# List of queue names
queues=("general" "celery_task_queue")

# Endpoint URL for LocalStack
endpoint_url="http://localhost:4566"

# Loop through the queue names and create the queues
for queue_name in "${queues[@]}"; do
    awslocal --endpoint-url="$endpoint_url" sqs create-queue --queue-name "$queue_name"
done
