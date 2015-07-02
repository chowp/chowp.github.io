Title: 开心学术
Date: 2015-07-02
Category: computer
Tags:
Slug:
Author:
Summary: use ipv6 to access google  google scholar

我们前一段时间给清华的同学抽奖了路由器，ipv6.google.com可以上了，但是有的同学问我为什么scholar.google.com不能上。这是因为学校的DNS默认先给scholar.google.com解析ipv4的地址，所以，你懂得。。。

废话少说，还是有别的方法的，既然已经能上ipv6了。方法就是hosts。 当前这个的前提是你得能上ipv6.

修改hosts方法很多，网上一搜一大把，简单来说：

* windows： 在C盘->window->System32->driver->etc 下面，有的电脑不能直接打开编辑，可以先把hosts拷贝到桌面，编译完拷贝回来。

* MAC： 比较简单 ,terminal 里面 sudo vim /etc/hosts 就可以了。

建议把下面的不用全部拷贝进去，只需要拷贝需要网站的那一行就可以了。比如
<pre><code>
2607:f8b0:4007:804::1002 scholar.google.com

（hosts其实一直在变，感谢lennylxx@github的工作，这是目前我能看到的最新的,scholar亲测可以。原文太长了，我摘录其中了一段：（https://github.com/lennylxx/ipv6-hosts/blob/master/snippets/01_google.txt）


############分割线:下面的都是可以直接拷贝到hosts中的#####################

## Google.com

2001:4860:4860::8888 google-public-dns-a.google.com
2001:4860:4860::8844 google-public-dns-b.google.com

2607:f8b0:4007:804::1008 google.com
2607:f8b0:4007:804::1014 www.google.com
2607:f8b0:4007:804::1009 admin.google.com
2607:f8b0:4007:808::200d accounts.google.com #accounts.l.google.com
2607:f8b0:4007:804::1009 bpui0.google.com #www3.l.google.com
2607:f8b0:4007:804::1000 clients1.google.com #clients.l.google.com
2607:f8b0:4007:804::1000 clients2.google.com #clients.l.google.com
2607:f8b0:4007:804::1000 clients3.google.com #clients.l.google.com
2607:f8b0:4007:804::1000 clients4.google.com #clients.l.google.com
2607:f8b0:4007:804::1000 clients5.google.com #clients.l.google.com
2607:f8b0:400e:c04::c0 supl.google.com
2607:f8b0:4007:804::1009 support.google.com #www3.l.google.com
2607:f8b0:400e:c02::74 upload.google.com #large-uploads.l.google.com
2607:f8b0:4007:804::1002 client-channel.google.com
2607:f8b0:4007:804::101e googletagmanager.com
2607:f8b0:4007:804::101e www.googletagmanager.com

## 谷歌香港
2607:f8b0:4007:804::100f google.com.hk
2607:f8b0:4007:804::100f www.google.com.hk
2607:f8b0:4007:808::2003 accounts.google.com.hk #accounts-cctld.l.google.com
2607:f8b0:4007:804::101f clients1.google.com.hk #clients-cctld.l.google.com
2607:f8b0:4007:808::200b m.google.com.hk #mobile.l.google.com
2607:f8b0:4007:804::1009 gxc.google.com.hk #www3.l.google.com
2607:f8b0:400e:c02::5e id.google.com.hk #id.l.google.com
2607:f8b0:4007:804::1009 ipv6.google.com.hk #ipv6.l.google.com
2607:f8b0:4007:804::1014 mobile.google.com.hk #www.google.com
2607:f8b0:4007:804::1009 picasaweb.google.com.hk #picasaweb.l.google.com
2607:f8b0:4007:804::1013 www.googlechinawebmaster.com

## 谷歌中国
2607:f8b0:400e:c04::a0 g.cn
2607:f8b0:400e:c04::a0 google.cn
2607:f8b0:400e:c04::a0 www.google.cn
2607:f8b0:4007:804::1009 ipv6.google.cn #ipv6.l.google.com
2607:f8b0:400e:c04::a0 m.google.cn #www.google.cn
2607:f8b0:400e:c04::a0 news.google.cn #www.google.cn
2607:f8b0:400e:c04::a0 video.google.cn #www.google.cn
2607:f8b0:4007:804::100b music.googleusercontent.cn #music-china.l.google.com
2607:f8b0:400e:c04::a0 www.265.com #265.com
2607:f8b0:400e:c04::a0 265.com

## Google 台湾
2607:f8b0:4007:804::101f www.google.com.tw
2607:f8b0:4007:804::101f clients1.google.com.tw #clients-cctld.l.google.com
2607:f8b0:4007:804::1009 picasaweb.google.com.tw #picasaweb.l.google.com

## Google 日本
2607:f8b0:4007:804::1017 www.google.co.jp
2607:f8b0:4007:804::1009 ipv6.google.co.jp #ipv6.l.google.com


## Scholar 学术搜索
2607:f8b0:4007:804::1002 scholar.google.com
2607:f8b0:4007:804::1002 scholar.google.com.hk
2607:f8b0:4007:804::1002 scholar.google.com.tw
2607:f8b0:400e:c04::a0 scholar.google.cn #www.google.cn

## Sites 协作平台
2607:f8b0:4007:804::1009 sites.google.com #www3.l.google.com
2607:f8b0:400e:c04::79 gsamplemaps.googlepages.com #ghs.googlehosted.com
