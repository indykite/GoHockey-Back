#!/bin/bash
set -e

SHORT_SHA=$(git rev-parse --short HEAD)
IMAGE_TAG="gcr.io/jarvis-dev-268314/hackathon/gohockey-back:${SHORT_SHA}"

docker push $IMAGE_TAG
