Title: vpn client and server on same machine
Date: 2015-09-21
Category: technology
Tags:
Slug: 
Author:
Summary: 

some ref [iptable](http://www.111cn.net/sys/linux/53011.htm)  [之前openvpn的nat规则不好使，配置了pptp之后，反而策略路由好使了,而且这个教程完整的在ubuntu上搭建pptp](http://blog.chinaunix.net/uid-7944836-id-3247311.html) [ufw 设置nat，仅作参考，这个ref好像有点问题](http://rainbird.blog.51cto.com/211214/394403/) [openvpn server 和 client 在同一台机器上转发规则， 仅供参考](http://unix.stackexchange.com/questions/205347/forward-vpn-traffic-to-another-vpn-server)
##############################config openvpn server ###########################

install openvpn, unzib

wget https://github.com/OpenVPN/easy-rsa/archive/release/2.x.zip


unzip 2.x.zip

cp -R easy-rsa-release-2.x/easy-rsa /etc/openvpn/

cd /etc/openvpn/easy-rsa

source ./vars
./clean-all
./build-ca gateway323
./build-key-server gateway323
./build-key user1
./build-dh
vim /etc/openvpn/server.conf

# add following content
port 8080 #openvpn连接端口
proto udp6 #使用ipv6的udp协议
dev tun
ca /etc/openvpn/easy-rsa/2.0/keys/ca.crt
cert /etc/openvpn/easy-rsa/2.0/keys/gateway323.crt
key /etc/openvpn/easy-rsa/2.0/keys/gateway323.key
dh /etc/openvpn/easy-rsa/2.0/keys/dh2048.pem
server 172.16.18.0 255.255.255.0# Openvpn适配器使用的地址
push "redirect-gateway def1"
push "dhcp-option DNS 166.111.8.28" #使用Tsinghua的DNS
client-to-client 
keepalive 10 120
comp-lzo
persist-key
persist-tun
cipher AES-128-CBC #加密方式
verb 3

vim /etc/sysctl.conf  # change ipv4_forwading to 1
sysctl -p
iptables -t nat -A POSTROUTING -s 172.16.18.0/24 -o eth0 -j SNAT --to-source 104.131.83.206
openvpn --config server.conf

##############################config openvpn client ###########################

mkdir client
cd client
# get crt from my remote vps

client
dev tun
proto udp
remote 166.111.68.22 8080
resolv-retry infinite
nobind
persist-key
persist-tun
ca ./keys/ca.crt
cert ./keys/user1.crt
key ./keys/user1.key
ns-cert-type server
comp-lzo
cipher AES-128-CBC
verb 3
######################## how to connect openvpn client and openvpn server at the smae machine #########

TBC