# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.hostname = "web"
    web.vm.network "forwarded_port", guest: 80, host: 8084
    web.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/main.yml"
    end
  end

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    db.vm.hostname = "db"
    db.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/main.yml"
    end
  end

end
