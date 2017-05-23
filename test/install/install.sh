#!/bin/sh
apt-get update &&
apt-get install -y make &&
rm -rf /etc/easy-network &&
mkdir /etc/easy-network &&
tar -C /etc/easy-network -xf easy-network.tgz &&
rm easy-network.tgz &&
cd /etc/easy-network &&
make bootstrap
