# Shell Script to Mount a Cloud Object storage into my VSI

sudo apt-get update
sudo apt-get install automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
git clone https://github.com/s3fs-fuse/s3fs-fuse.git

cd s3fs-fuse
./autogen.sh
./configure
make
sudo make install

echo "l6MzPfwb0UCk1w3qZsGI:mlJEGDEewbPImLZHNYVCxOKQ1ewF7KxkhBaT7VLD" > $HOME/.cos_creds
chmod 600 $HOME/.cos_creds

sudo mkdir /mnt/h3bkt
sudo s3fs hw3disk /mnt/h3bkt -o nonempty -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=http://s3.us.cloud-object-storage.appdomain.cloud

