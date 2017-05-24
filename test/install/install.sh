#!/bin/sh
apt-get update &&
apt-get install -y make &&
rm -rf /etc/easy-network &&
mkdir /etc/easy-network &&
tar -C /etc/easy-network -xf easy-network.tgz &&
rm easy-network.tgz &&
cd /etc/easy-network &&
chown -R vagrant:vagrant . &&
su vagrant -c sh << EOF
export EASYNETWORKROOT=/home/vagrant/easy-network-install
rm -rf /home/vagrant/easy-network-install
make install
EOF
