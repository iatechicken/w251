# Script to kill everything and remove
docker kill tx-broker
docker kill tx-forward
docker kill tx-face

docker rm tx-broker
docker rm tx-forward
docker rm tx-face
