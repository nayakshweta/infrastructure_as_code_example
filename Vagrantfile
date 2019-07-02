# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    db.vm.hostname = "db"
    db.vm.network "private_network", ip: "10.0.2.15"
    db.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/main.yml"
    end
  end

  config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.hostname = "web"
    web.vm.network "forwarded_port", guest: 80, host: 8084
    web.vm.network "private_network", ip: "10.0.2.14"
    web.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/main.yml"
    end
  end

end
