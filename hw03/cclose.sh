# script to kill everything and remove in cloud vsi

docker kill c-face
docker kill c-broker

docker rm c-face
docker rm c-broker

docker network rm cbridge
