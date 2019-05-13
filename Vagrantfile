# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.


Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
    vb.cpus = 1
  end

    config.vm.define "control02" do |webtier|
      webtier.vm.box = "bento/ubuntu-18.04"
      webtier.vm.hostname = "control02"
      webtier.vm.network "private_network", ip: "192.168.45.12"
      webtier.vm.network "forwarded_port", guest: 5000, host: 5000
      webtier.vm.provision "shell", inline: <<-SHELL
            # required for ansible pip module https://docs.ansible.com/ansible/latest/modules/pip_module.html#pip-module
            sudo apt-get install -y python-virtualenv
            virtualenv --version
            sudo apt-get install -y python-pip
            pip --version
            echo "================================="
            echo "control02 up && running"
            echo "================================="
      SHELL
      webtier.vm.provider "virtualbox" do |vb|
          vb.name = "control02"
      end
      webtier.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "deploy.yml"
      ansible.become = true
      end
      end


end
