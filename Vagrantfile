# -*- mode: ruby; -*-
require 'etc'

Vagrant.configure("2") do |config|
  config.vm.define :web do |web|
    # Ubuntu 12.04
    web.vm.box = "wheezy-rc1"
    web.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/debian-70rc1-x64-vbox4210-nocm.box"

    # Network
    web.vm.network :private_network, ip: "192.168.111.222"
    web.vm.hostname = "vagrant.bookkeeping.org"
    web.vm.network :forwarded_port, guest: 80, host: 8080, auto_correct: true
    web.vm.network :forwarded_port, guest: 5432, host: 5432

    # Share for masterless server
    #web.vm.synced_folder "salt/roots/", "/srv/"

    # Customize the box
    web.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--memory", 512]
    end
  end
end

