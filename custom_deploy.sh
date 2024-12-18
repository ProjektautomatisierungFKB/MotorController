# Use a docker_image_name.txt file to configure the Docker image name
source ./docker_image_name.txt
source ./deploy_secrets.txt

DOCKER_FILEPATH="./"
TAR_NAME="$DOCKER_IMAGE.tar"
TAR_FILEPATH="build/$TAR_NAME"
REMOTE_DIR="/home/$PI_USERNAME/robotX/"

echo "Building Docker Container..."
docker build -q -t $DOCKER_IMAGE --platform linux/arm64/v8 $DOCKER_FILEPATH

echo "Saving Docker File..."
docker save -o $TAR_FILEPATH $DOCKER_IMAGE

echo "Copying tar file to Pi..."
sshpass -p $PI_PASSWORD scp $TAR_FILEPATH $PI_USERNAME@$PI_HOSTNAME:$REMOTE_DIR

echo "Removing existing container and image on Pi if any..."
sshpass -p "$PI_PASSWORD" ssh "$PI_USERNAME@$PI_HOSTNAME" \
  "docker rm -f $DOCKER_IMAGE || true && docker rmi $DOCKER_IMAGE:latest || true"

echo "Loading Docker Image on Pi..."
sshpass -p $PI_PASSWORD ssh $PI_USERNAME@$PI_HOSTNAME \
  "docker load -i $REMOTE_DIR/$TAR_NAME"

echo "Running Docker Container on Pi..."
sshpass -p $PI_PASSWORD ssh $PI_USERNAME@$PI_HOSTNAME \
  "docker run -d --name $DOCKER_IMAGE --network host --privileged -v /sys/class/gpio:/sys/class/gpio -v /dev/mem:/dev/mem $DOCKER_IMAGE:latest"

echo "Deployment ended."
