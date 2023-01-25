#!/bin/bash
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPO_DIR=$(realpath ${SCRIPT_DIR}/..)
SHORT_SHA=$(git rev-parse --short HEAD)
IMAGE_TAG="gcr.io/jarvis-dev-268314/hackathon/gohockey-back:${SHORT_SHA}"

# Deploys to Belgium
gcloud run deploy hackathon-gohockey-back \
    --image=$IMAGE_TAG \
    --region=europe-west1 \
    --max-instances=4 \
    --port=8080 \
    --env-vars-file=${REPO_DIR}/.env.staging.yaml \
    --allow-unauthenticated
