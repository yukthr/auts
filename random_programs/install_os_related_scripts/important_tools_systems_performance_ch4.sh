#!/usr/bin/bash
echo "$(tput setaf 3)Installing tools which are recommended in systems perfomance 2nd edition - chapter 4 for troubleshooting"

echo Following Tools and packages will be cloned
echo "$(tput setaf 3)git procps,util-linux,sysstat,iproute2,numactl,linux-tools-common linux-tools-$(uname -r),bcc-tools(aka bpfcc-tools),
bpftrace,perf-tools-unstable,trace-cmd,nicstat,ethtool,tiptop,msr-tools,github.com/brendangregg/msr-cloud-tools,
github.com/brendangregg/pmc-cloud-tools"

# Installing
echo "$(tput setaf 2)Above listed packages will be installed now"
sudo apt-get update
sudo apt-get install git procps util-linux sysstat iproute2 numactl linux-tools-common linux-tools-$(uname -r) bpfcc-tools bpftrace perf-tools-unstable trace-cmd nicstat ethtool tiptop msr-tools -y

echo "$(tput setaf 3)Creating directory git_troubleshooting_packages"
sudo mkdir git_troubleshooting_packages
cd git_troubleshooting_packages/
sudo git clone https://github.com/brendangregg/msr-cloud-tools
sudo git clone https://github.com/brendangregg/pmc-cloud-tools


