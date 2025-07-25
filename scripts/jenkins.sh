#!bin/bash

sudo apt update

sudo apt install openjdk-8-jdk -y

https://pkg.jenkins.io

https://pkg.jenkins.io/debian-stable/

sudo systemct1 start jenkins

sudo systemct1 enable jenkins

sudo systemct1 status jenkins



# Installing Docker


curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

sudo usermod -aG docker jenkins


newgrp docker

sudo apt install awscli -y

sudo usermod -a -G docker jenkins


# AWS Configuration & restarts jenkins
aws configure

# Setup elastic IP on AWS

## For getting the admin password for jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword


