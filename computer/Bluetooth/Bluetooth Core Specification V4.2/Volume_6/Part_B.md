<h1 align=center>Link Layer Specification</h1>
##目录
1. 介绍
1. 数据传输包
1. 字节流
1. 数据传输协议
1. 连接层控制
	
##介绍
连接层操作可以描述为状态机，分别有5种状态：

* Standby State：待机状态。不发送和接收数据，可由另外4种状态进入待机状态* Advertising State：广播状态。在广播频道发送数据，也可以监听和回复对广播数据的响应。在这一状态称为广播者，可由待机状态进入广播状态。* Scanning State：扫描状态。扫描状态会监听广播频道的数据，这一状态称为扫描者，可由待机状态进入。
* Initiating State：发起状态。监听广播频道的数据并回应，以与广播者建立连接。这一状态称为创建者，可由待机状态进入。
* Connection State：已连接状态。可由广播状态或发起状态进入。在已连接状态由两类角色:Master Role(由发起者状态进入),Slave Role（由广播者状态进入）。Master Role设备会和Slave Role设备通信，并设置传输定时。Slave Role只会与一个Master Role通信
设备同一时间只能处于其中一种状态
<img width=400 height=300 src="src/state machine of Link Layer.png"></img>

### 状态与角色结合当设备支持连接层支持多种状态时：
1. 处于Connection State时，可以同时为Master Role和Slave Role
1. 处于Connection State时，处于Slave Role时可以有多个连接
1. 处于Connection State时，处于Master Role时可以有多个连接
1. 其他状态与角色的组合也可能实现
1. 两个Connection State状态之间最多只能有1个连接

以下组合可以部分满足，但当满足下表组合A时，必定也满足组合B（`最后一行表明当设备作为从机已连接时，仍然可以连接到更多的主机`）

<img width=400 height=200 src="src/Requirements on supported states and state combinations.png"></img>

### 设备地址

设备由设备地址标记，设备地址可以是公共设备地址或一个随机的设备地址，长度为48位，设备应该至少包括一个公共设备地址或一个随机设备地址。设备有私有地址时，同样应该至少包括一个公共设备地址或一个随机设备地址。

### 物理频道
在BLE的40个频道中，有3个频道（0，12，39）用于发现设备、广播数据和发起连接，另外37个频道用于已连接设备间传输数据

为解决多个通信在同一频道的冲突，每次传输都以一个Access Address开始，当连接层在时间、频率、access address上都同步时，就说连接层已连接到该频道

##数据传输包
###数据包格式

连接层发送的数据格式统一如下，其中PDU（Protocol Data Unit）为`协议数据单元`

<img width=400 height=80 src="src/Link Layer packet format.png"></img>

数据包最小长度为80bit，最大为2120bit

**Preamble**
8位Preamble用于接收器进行频率同步，定时估计和自动增益控制，广播频道的Preamble为10101010b，数据频道更具Access Address的最低有效位不同，Preamble为10101010b或01010101b。

**Access Address**
所有广播频道的Access Address应该为10001110100010011011111011010110b (0x8E89BED6)。
数据频道的Access Address是一个随机的32-bit数，由Initiating State的设备生成并在请求建立连接时发送给广播设备 and sent in a connection request as defined in Section 2.3.3.1. The initiator shall ensure that the Access Address meets the following requirements:**PDU***
广播频道和数据频道的PDU格式不同

**CRC**
校验位根据PDU内容生成

### 2.3 广播频道PDU

<img width=400 height=80 src="src/Advertising channel PDU.png"></img>

<img width=400 height=70 src="src/Advertising channel PDU Header.png"></img>

<img width=300 height=300 src="src/Advertising channel PDU Header’s PDU Type field encoding.png"></img>

1. 广播PDU
	* ADV_IND: 非定向可连接	* ADV_DIRECT_IND: 定向可连接	* ADV_NONCONN_IND: 非定向不可连接	* ADV_SCAN_IND: 非定向可扫描
由Advertising State发送，并由Scanning State或Initiating State接收

ADV_IND：Payload由6字节的Device Address和0-31字节的广播数据组成
ADV_DIRECT_IND：Payload由6字节的广播设备Device Address和接受的发起连接设备的Device Address组成

ADV_NONCONN_IND：Payload由6字节的Device Address和0-31字节的广播数据组成

ADV_SCAN_IND：Payload由6字节的Device Address和0-31字节的广播数据组成
1. 扫描PDU
	* SCAN_REQ: Scanning State发送，Advertising State接收，Payload由6字节扫描设备地址，6字节广播设备地址组成	* SCAN_RSP: Advertising State发送，Scanning State接受，Payload由6字节的广播设备地址和0-31字节的广播数据组成
1. 发起连接PDU
	* CONNECT_REQ：Initiating State发送，Advertising State接收，Payload由6字节发起者设备地址，6字节广播者设备地址，22字节LLData组成
	
	<img width=450 height=70 src="src/LLData field structure in CONNECT_REQ PDU’s payload.png"></img>
	
	发包间隔Interval，忽略次数Latency，超时Timeout均在LLData中	ChM用于标记0-36的数据频道中哪些可用，哪些不可用
	Hop用于指定跳频方法，取值应为5-16的随机数
	SCA用于指定主机的时钟精度（频率偏差）

### 2.4 数据频道PDU
<img width=450 height=80 src="src/Data Channel PDU.png"></img>
<img width=450 height=70 src="src/Data channel PDU header.png"></img>

