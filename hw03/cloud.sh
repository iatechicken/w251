# Shell script to build bridge and run dockers

# Create bridge on cloud
docker network create --driver bridge cbridge

# Build cloud broker container
docker build -t c-broker -f Dockerfile.cbroker .

# Build cloud face container
docker build -t c-face -f Dockerfile.cface .

# Run cloud broker container
docker run -d --name c-broker -p 1883:1883 --network cbridge c-broker

# Run cloud face container
docker run -d --name c-face -v /mnt/h3bkt:/data --network cbridge c-face
