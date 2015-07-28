# BLE介绍

![BLE 协议栈](http://s8.sinaimg.cn/mw690/a67a99d74dfaa11fe8467&690)

`PHY物理层`：在2.4GHz的ISM频段中跳频识别。

`LL连接层`：控制设备的状态。设备可能有5中状态：就绪standby，广播advertising，搜索scanning，初始化initiating和连接connected。广播者传播数据，使得浏览者可以接收到。initiator就是一个对广播者回复连接请求的设备。如果广播者接受请求，广播者和initiator初始者就会进入connected连接状态。一个处于连接状态的设备会有一个角色：master和slave。初始化这个连接的为master，接受这个连接请求的为slave。

`HCI层`：host和controller之间通过一个标准接口进行通信提供了一些方法。这一层可以通过一个软件API或者是硬件接口如UART，SPI和USB。

`L2CAP`：为上层数据提供封装服务。

`SM`：定义了建立连接和KEY的方法。

`GAP`：直接与profile和app进行接触，解决设备的发现和连接相关的服务，此外GAP也会初始化安全相关的特色。

`ATT协议`：允许一个设备去显示一些数据，对于其他设备称之为“Attribute属性”，在ATT中，那些显示这些属性的设备被称为server，同等的另一个设备称为client。LL层的状态master和slave和ATT层的这两个状态无关。

`GATT层`：是一个服务框架定义了对ATT应用的子程序。GATT指定了profile的结构。在BLE中，由profile或者是服务所使用的所有类型的数据都称为characteristic。发生于两个设备间通过BLE连接进行交换的数据都需经过GATT子程序处理。因此，app和profile会直接使用GATT。

**开发app，真正接触的是GAP和GATT，GAP用来建立连接，GATT用来数据传送**
