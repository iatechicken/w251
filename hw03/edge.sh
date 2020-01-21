# Creating Bridge
docker network create --driver bridge tx-bridge

# Building Broker Docker
docker build -t tx-broker -f Dockerfile.broker .

# Building Forwarder Docker
docker build -t tx-forward -f Dockerfile.forward .

# Building Face Detection Docker
docker build -t tx-face -f Dockerfile.face .

# Running Broker Docker
docker run -d --name tx-broker -p 1883:1883 --network tx-bridge tx-broker

# Running Forwarder Docker
docker run -d --name tx-forward --network tx-bridge tx-forward

# Running Face Docker
docker run -d --name tx-face --network tx-bridge tx-face
