## W251 HW03

Objective: Capture facial images from a webcam that is attached to the Jetson TX-2. Then, send the captured facial iamges to the cloud object storage on IBM virtual servers using MQTT

1. Build Containers on Jetson TX-2 for the MQTT and Facial Image Capture
```
docker build --network=host -t mqtt -f Dockerfile.mqtt .
docker build --network=host -t tx2 -f Dockerfile.tx2 .
```

2. Create a Docker Network Bridge
```docker network create --driver bridge faces```

3. Run the Docker Containers on TX-2
```
docker run --name mosquitto --network faces -p :1883 -v "$PWD":/new_hw03 -d mqtt sh -c "mosquitto -c /new_hw03/mqtt_broker.conf"
docker run --name forwarder --network faces -v "$PWD":/new_hw03 -d mqtt sh -c "mosquitto -c /new_hw03/mqtt_forward.conf"
```

4. Run the shell script to run face capture container in bash mode

* Make sure that your script has access ```chmod +x tx2.sh```

```
./tx2.sh
```

5. Run the image capture python script in the bash container shell
```
python3 face.py 169.61.83.248
```

* 169.61.83.248 was the public IP address of the IBM VS that will be created in latter steps. This step can be repeated later.

6. Create an IBM VS
```
ibmcloud sl vs create --hostname=face-server --domain=w251-rryu.cloud --cpu=2 --memory=4096 --datacenter=wdc07 --san --os=UBUNTU_16_64 --disk=100 --key=your_ssh_key
```

7. Create a Cloud Object Storage Account and Bucket in the IBM cloud online platform

8. Setup the cloud VM
```
sed -i -e 's/\r$//' cloud.sh
chmod +x cloud.sh
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
```

9. Add cloud object storage credentials to the HOME Path
```
echo "<AccessKeyID>:<SecretAccesKey>" > $HOME/.cos_creds
chmod 600 $HOME/.cos_creds
```

10. Mount cloud object storage image
```
mkdir /mnt/face-images
s3fs face-images /mnt/hw3-bucket-app -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us.cloud-object-storage.appdomain.cloud
```

11. Build Containers on IBM Cloud VM
```
docker build -t cloud_ivs -f Dockerfile.cloud .
```

12. Run Docker containers on IBM Cloud VM
```
docker run --name mosquitto -p 1883:1883 -v "/root/w251/new_hw03":/hw03 -d cloud_ivs mosquitto
docker run --name subscriber -v "/root/w251/new_hw03":/hw03 -v "/mnt/face-app":/hw03-faces -ti cloud_ivs bash
```

* This should open up a new bash shell inside the cotainer

13. Run the python application inside the bash shell as follows:
```
python3 /hw03/cloudface.py 169.61.83.248 /hw03-faces/
```
