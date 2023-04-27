#!/usr/bin/env bash

#clean codedeploy-agent files for a fresh install
sudo rm -rf /home/ec2-user/install

#install CodeDeploy agent
sudo yum -y update
sudo yum -y install ruby
sudo yum -y install wget
cd /home/ec2-user
wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto

#update os & install python3
sudo yum update -y
sudo yum install -y python3 python3-pip  python3-devel
pip3 install --user --upgrade virtualenv

#delete app
sudo rm -rf /home/ec2-user/Blood_Bank