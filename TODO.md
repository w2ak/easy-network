# What should be installed after the install

## Requirements

* openvpn, iptables, python3

## Rough structure of what you should find

* easy-network-root
  * environment variables                                         **json/shell**
    `config.js'
  * rsa
    * easy-rsa
    * helper script                                                   **python**
  * vpn
    * main start and stop script                                       **shell**
    * existing vpns                                                     **json**
    * helper script                                                   **python**
      should create config files, vpn folders (for multi-vpn),
      etc.
  * firewall
    * main start and stop script                                       **shell**
    * existing configuration                                            **json**
    * helper script                                                   **python**
      should allow to edit configuration (simplified cli)

# What we want to be able to do

* Have a config file with the locations of PKI, ROOT, etc.
* Be able to easily use the pki.
* Have a good pki configuration (openssl config).
* Have a script for openvpn configuration.
* Have an easy way to create .ovpn config files for clients.
* Have an easy way to manage firewall (simplified cli for iptables ?)
