# Copy Image to Kubernetes Nodes

This script save the docker image, scp the image to the k8 host and load the docker file.

Use following command.

	sh copy.sh {Full Image name}
	eg: sh copy.sh wso2/esb:4.9.0:4.1.3