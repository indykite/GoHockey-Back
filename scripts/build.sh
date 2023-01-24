#!/bin/bash
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPO_DIR=$(realpath ${SCRIPT_DIR}/..)
SHORT_SHA=$(git rev-parse --short HEAD)
IMAGE_TAG="gcr.io/jarvis-dev-268314/hackathon/gohockey-back:${SHORT_SHA}"

docker build -t $IMAGE_TAG $REPO_DIR
