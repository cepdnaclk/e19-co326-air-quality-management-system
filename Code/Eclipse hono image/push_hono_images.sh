#!/bin/bash
#*******************************************************************************
# Copyright (c) 2016 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0
#
# SPDX-License-Identifier: EPL-2.0
#*******************************************************************************

TAG=$1
CR=${2:-"docker.io"}
REPO=${3:-"eclipse"}

COMMAND_ROUTER_IMAGE_LEGACY_BASE="hono-service-command-router"
COMMAND_ROUTER_IMAGE_INFINISPAN_BASE="${COMMAND_ROUTER_IMAGE_LEGACY_BASE}-infinispan"

IMAGES="hono-adapter-amqp \
        hono-adapter-coap \
        hono-adapter-http \
        hono-adapter-lora \
        hono-adapter-mqtt \
        hono-adapter-sigfox \
        hono-service-auth \
        ${COMMAND_ROUTER_IMAGE_INFINISPAN_BASE} \
        ${COMMAND_ROUTER_IMAGE_LEGACY_BASE} \
        hono-service-device-registry-jdbc \
        hono-service-device-registry-mongodb"

NATIVE_IMAGES="hono-adapter-amqp-native \
        hono-adapter-coap-native \
        hono-adapter-http-native \
        hono-adapter-lora-native \
        hono-adapter-mqtt-native \
        hono-adapter-sigfox-native \
        hono-service-auth-native \
        ${COMMAND_ROUTER_IMAGE_INFINISPAN_BASE}-native \
        ${COMMAND_ROUTER_IMAGE_LEGACY_BASE}-native \
        hono-service-device-registry-jdbc-native \
        hono-service-device-registry-mongodb-native"

ME=$(basename "$0")
echo "called as $ME"

ECLIPSE_REPO="eclipse"

if [[ "push_hono_native_images.sh" == "$ME" ]]
then
  IMAGES=${NATIVE_IMAGES}
  ECLIPSE_COMMAND_ROUTER_INFINISPAN_IMAGE_NAME="${ECLIPSE_REPO}/${COMMAND_ROUTER_IMAGE_INFINISPAN_BASE}-native:${TAG}"
  ECLIPSE_COMMAND_ROUTER_LEGACY_IMAGE_NAME="${ECLIPSE_REPO}/${COMMAND_ROUTER_IMAGE_LEGACY_BASE}-native:${TAG}"
else
  ECLIPSE_COMMAND_ROUTER_INFINISPAN_IMAGE_NAME="${ECLIPSE_REPO}/${COMMAND_ROUTER_IMAGE_INFINISPAN_BASE}:${TAG}"
  ECLIPSE_COMMAND_ROUTER_LEGACY_IMAGE_NAME="${ECLIPSE_REPO}/${COMMAND_ROUTER_IMAGE_LEGACY_BASE}:${TAG}"
fi

# Tag the Infinispan Command Router image produced in the build with its legacy name for backwards compatibility.
# The Command Router will be published using both the new and legacy names when looping through the IMAGES array below.
echo "tagging existing command-router image (${ECLIPSE_COMMAND_ROUTER_INFINISPAN_IMAGE_NAME})" \
     " with legacy name (${ECLIPSE_COMMAND_ROUTER_LEGACY_IMAGE_NAME})"

if ! docker tag "${ECLIPSE_COMMAND_ROUTER_INFINISPAN_IMAGE_NAME}" "${ECLIPSE_COMMAND_ROUTER_LEGACY_IMAGE_NAME}"
then
    echo "re-tagging ${ECLIPSE_COMMAND_ROUTER_INFINISPAN_IMAGE_NAME} with legacy name failed. Exiting!"
    exit 1
fi

if [[ -n "$TAG" ]]
then
  IMAGES_TO_PUSH=()
  # Collect all images for pushing, re-tagging if necessary
  for image in $IMAGES
  do
    ECLIPSE_IMAGE_NAME="${ECLIPSE_REPO}/$image"
    if [[ "docker.io" != "${CR}" || "eclipse" != "${REPO}" ]]
    then
      IMAGE_NAME="${CR}/${REPO}/${image}"
      if ! docker tag "${ECLIPSE_IMAGE_NAME}:${TAG}" "${IMAGE_NAME}:${TAG}"
      then
          echo "re-tagging ${ECLIPSE_IMAGE_NAME}:${TAG} as ${IMAGE_NAME}:${TAG} failed. Exiting!"
          exit 1
      fi
    else
      IMAGE_NAME="${ECLIPSE_IMAGE_NAME}"
      if ! docker inspect "${IMAGE_NAME}:${TAG}" > /dev/null
      then
          echo "image ${IMAGE_NAME}:${TAG} does not exist. Exiting!"
          exit 1
      fi
    fi
    # Collect the image for pushing
    IMAGES_TO_PUSH+=("${IMAGE_NAME}:${TAG}")
  done

  # Now push all images that were collected
  for image in ${IMAGES_TO_PUSH[*]}
  do
    echo "pushing image ${image} ..."
    docker push "${image}"
  done
else
  echo "This script can be used to push Hono's images from"
  echo "the local Docker registry to a (remote) container registry."
  echo ""
  echo "usage: push_hono_images.sh TAG [CR [REPOSITORY]]"
  echo "TAG is the (already existing) TAG to push to the registry."
  echo "CR is the name of the container registry to push to."
  echo "REPOSITORY is the name of the repository within the registry to push to."
  echo "If only TAG is specified, then the images are pushed to 'docker.io' using repository name 'eclipse'."
fi
