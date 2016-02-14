
image_name='temp.tar'
image_location='/home/pubudu/docker-images'
image_path=$image_location/$image_name
host_image_path='/home/core/temp.tar'

username='core'
node1='172.17.8.102'


echo "Creating image tar file....."
docker save $1 > $image_path

echo "SCP files to minions"

#sshpass -p $username scp $image_path $username@$node1:~/ 
scp $image_path $username@$node1:~/ 

echo "Loading docker images in minions"

#sshpass -p $username scp $image_path $username@$node1 "sudo docker load < /home/vagrant/temp.tar"
ssh $username@$node1 "docker load < $host_image_path"