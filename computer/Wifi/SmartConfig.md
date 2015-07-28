#SmartConfig
* Smart Config flow - AES encryption enabled

![AES加密](http://processors.wiki.ti.com/images/a/ae/Procedure_smart_config.PNG)

* Smart Config flow - AES encryption disabled

![AES加密](http://processors.wiki.ti.com/images/9/92/Procedure_smart_config1.PNG)

**APIs**

**nvmem_create_entry(NVMEM_AES128_KEY_FILEID, AES128_KEY_SIZE)** – Create an entry at field ID 12 to store the AES key. (Only when AES encryption is enabled)

**aes_write_key(key)**- write the key to EEPROM - fileID 12. (Only when AES encryption is enabled)

**wlan_smart_config_set_prefix(aucCC3000_prefix)**– Set CC3000 prefix. Currently this API has to be called with the value ‘TTT’.

**wlan_smart_config_start()** – Send command to CC3000 to start the Smart config process.

**wlan_smart_config_process(1)** – Call this API with value 1 when AES encryption is enabled, otherwise 0. Brief process the acquired data and store it as a profile.

**wlan_ioctl_set_connection_policy(DISABLE, DISABLE, ENABLE)**– sets the connection policy, Set parameters to use Auto connect in order to connect to a stored profile.

**References**

[请问 SmartLink 技术的原理是什么？](http://www.zhihu.com/question/24513232)

基本思想就是利用广播包，我们知道以太网在最底层是以太网数据包，无线则更是广播包，天线发送数据包到空中，接收端接收到数据包，然后处理，供各层使用。

汉枫的模块SmartLink的实现细节；
协议用了UDP广播数据包，手机向本地广播地址，端口49999，发送特定编码的数据包；

将每一个密码字符编码为UDP包负载的字节数，一个回车，一个换行以及密码字节数；

[BroadLink 智能插座的一键无线配置是如何实现的？](http://www.zhihu.com/question/21783165)

不要使用长度编码,丢包率会影响成功率,基本不可能成功.
因为IPv4组播地址和Mac地址之间的关系(后23位一样),
推荐将信息编码进不同的组播地址中,然后创建不同的socket发送任意长度任意内容;接收端只需要捕获组播包获取组播地址就可以解析出信息.
这样做比TI还是其他人采用的长度编码信息好处太多了,适配所有无线协议,规避丢包率的影响.

[CC3000 Smart Config - transmitting SSID and keyphrase](http://depletionregion.blogspot.ch/2013/10/cc3000-smart-config-transmitting-ssid.html)
 
  we want to send two pieces of information, an SSID and the keyphrase, from one party that is already a member of the wifi network to an external party **who can monitor all the encrypted wifi traffic but who cannot decrypt it**.
 
  Someone who cannot decrypt the wifi traffic can still see quite a lot of information, e.g. **the source and receiver MAC addresses of every packet sent**. **the length of the data portion of the packets**. if one sends n bytes of data in a given packet then the encrypted packet will contain (n + x) bytes where x is constant across all packets.
  
[CC3000 advertises presence on network via DNS-SD](http://depletionregion.blogspot.ch/2013/10/cc3000-advertises-presence-on-network.html)