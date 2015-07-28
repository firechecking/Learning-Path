#CSR Mesh
##CSR Mesh介绍

CSR Mesh协议使用Bluetooth Smart技术将信号传输至其他联网的Bluetooth Smart设备，这些Bluetooth Smart设备再将接收到的信号传回。信号可单独传输给单个设备也可同时传输至多个设备，甚至还可传输至分属多组的不同设备。

CSRmesh依靠设备本身，使设备不仅可以接收信息并进行操作，同时还将信号重复传输至周边设备，从而扩展Bluetooth Smart设备的信号覆盖范围并进一步转化为一个mesh网络。也就是说每个设备都是中继器，理论上只要设备足够，网络会扩展到无限大，实际上受到IP地址的限制每个网络可接入最多65535个设备（16位Device ID）。

其所采用一种广播技术，节点和节点之间的距离是30至50米，各节点间的最低传输延时为15ms，节点芯片具有中继功能，当控制信号到达第一波被控设备后，它们会将信号再次广播出去，到第二波、第三波乃至更远设备，也可以将这些设备所采集到的温度、红外等信号回传。

CSRmesh的泛洪式网络无路由表，也无需添加集线器、AP等外置设备，即可通过支持Bluetooth Smart Ready的终端，如智能手机，实现直接控制。Mesh网络采用128位加密传输以防网络监听，提供可选验证步骤防止中间人攻击，可预先生成网络秘钥并提供不同使用者授权等级来确保网络及应用安全。网络通过3个独立信道传输信息，信道可与WiFi良好共存，以确保可靠。

与Zigbee协议相比，CSRmesh令智能设备更易控制，简化用户体验，无需复杂设置和配对，也不需要通过网络路由就可连网。其控制功能可通过市面上配备标准Bluetooth Smart的任意智能手机或标准控制装置，如照明开关或控制面板等实现。而且网络覆盖面大，即使某节点出现问题也不影响其他节点，支持设备分组、子分组及设备关联以及从Mesh中移除设备

CSR’s Mesh protocol enables BLE devices not only to receive and act upon messages, but also to repeat those messages to surrounding devices thus extending the range of Bluetooth Smart and turning it into a mesh network.

•The protocol encompasses different software models to support different end device types.

•The concepts of device grouping, sub-grouping, association and device removal from a network are also supported.

•It is possible to support up to 64K devices and 64K groups per network.

• Devices may also belong to more than one network.

##工作过程

>CSRmesh association state machine

<img src="http://git.oschina.net/164049406/Intelligent-Hardware-Group-at-PATech/raw/master/资料阅读/祖/Bluetooth/src/CSRmesh association state machine.png" width=500 height=450></img>

##Features
1. 利用智能手机就能对网络中任意位置的设备进行简单、直接的控制和配置
	1. 无需访问集线器、路由器或其它设备
	1. 无单点故障
1. 成熟的 BT 智能技术。 与 Wi-fi 和谐共存
	1. 不会相互干扰
1. 安全、可靠
	1. 可防窃听和中间人攻击
	1. 三个载波信道
1. 使智能蓝牙的覆盖范围超越无线链路
	1. 网状网泛洪算法

1. Freedom of Control - CSRmesh works directly with your existing devices. You can collect data and control devices with existing tablets and smartphones. There is no need for a special hub to connect your devices. You can configure and control devices with existing tablets and smartphones.

1. Simple Setup - CSRmesh is simple and easy to setup. Just switch on the device. Discovery and control is then handled by the app on your smart device.
1. Safe and Secure - CSRmesh uses high-level banking-like encryption to ensure safe and secure transmission of messages throughout your network. There is an additional authentication mode for enhanced security. Simplicity is maintained with a network passcode that is provided to authorised users and devices to enable them to participate in the mesh.

1. Applications - CSRmesh has been initially developed to support wireless lighting control, but the protocol supports models for additional applications. Full home automation models enabling Heating, ventilation and Air Conditioning (HVAC), as well as security and sensing will be rolled out in the future.

1. Technology - CSRmesh is a protocol layer that runs on top of the Bluetooth 4.0 standard. It is supported on single mode Bluetooth Smart devices as well as dual-mode Bluetooth Smart Ready devices. By using the existing Bluetooth standard it enables consumer products such as smartphones, tablets, TVs and set-top boxes to interact directly with devices within the CSRmesh network. CSR is actively working to standardise the technology and enable wide participation from many manufacturers.

1. Resources - The CSRmesh development kit provides three development boards, a programmer and access to a full SDK to enable you to develop wireless switches and lights and evaluate the CSRmesh technology. Additional CSRmesh development boards can be purchased to expand your network

##CSR Mesh开发套件

`In addition to the CSRmesh development kit, CSRmesh will run on any of CSR's μEnergy products. However, for access to the CSRmesh libraries, users must purchase a CSRmesh development kit.`

The CSRmesh Development Kit provides a complete set of tools for evaluation and software development.

1. Development Boards (x3)
1. CSR xIDE software development environment
1. USB programmer (x1) and interface cables (x2)
1. Example CSRmesh applications for the Development Board
1. Example host applications and source code for Smartphones, supporting
	1. Google Android
	1. Apple iOS (in development)

The CSRmesh Development Board features:

* CSR1010 IC with size EEPROM
* PCB antenna
* 1x RGB LED
* 2x user pushbuttons
* 1x user slide switch
* Power switch
* SPI programming connector
* 2x AA battery holders on reverse
* Pads to connect IO to external devices

Applications 

* Lighting
* Home Automation
* Sensor network

###下载

**CSR uEnergy SDK 2.4.3.26**
<http://pan.baidu.com/s/1c04b7Le> 提取密码:7l8m

`下面三种工具需要付费才能下载，网上没找到共享资源`

**CSRmesh V1.1 lighting** 
<https://www.csrsupport.com/download/51485/CSRmesh%201.1%20Examples.zip>

**iOS application**
<https://www.csrsupport.com/agree.php?did=51199&returnto=/BluetoothLowEnergyproductinformation>

**android application**
<https://www.csrsupport.com/agree.php?did=51198&returnto=/BluetoothLowEnergyproductinformation>


###应用举例
网上搜索到的一个借组CSRMesh的项目：SmartBeacon Mesh。介绍得还算详细

[AIRcable SmartBeacon in the CSRmesh™ 1.1](http://www.aircable.net/online/index.php?route=information/information&information_id=13)(需翻墙)

[AIRcable SmartBeacon in the CSRmesh™ 1.1](src/SmartBeacon Mesh.pdf)(本地pdf)

###参考资料
<https://wiki.csr.com/wiki/Main_Page>

<https://wiki.csr.com/wiki/CSRmesh>

<https://wiki.csr.com/wiki/CSRmesh_Installation>

[CSRmesh Development Kit User Guide](https://www.csrsupport.com/download/49148/CS-313116-UG-1%20CSRmesh%20Development%20Kit%20User%20Guide.pdf)

[CSRmesh™ Application 1.1 Release Note](https://www.csrsupport.com/download/51204/CS-318925-RN-1%20CSRmesh%201.1%20Release%20Note.pdf)

[CSRmesh™ 1.1 Sniffer Application Application Note](https://www.csrsupport.com/download/51202/CS-320704-AN-1%20CSRmesh%201.1%20Sniffer%20Application%20Note.pdf)
