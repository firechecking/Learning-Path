# Physical Web
## URI Beacon

<https://github.com/google/uribeacon>

1. Beacon模式
	
	广播且不可连接（ADV_NONCONN_IND）

1. 广播内容

	`<Service UUID>`:提供跨平台的后台扫描
	`<Service Data>`:用于广播URI，TX功率电平（测距），和flags

1. 广播数据格式

<img width=900 height=350 src=src/uribeacon-figure1.png></img>

<img width=500 height=350 src=src/uribeacon-figure2.png></img>

**CC2541为例**

url---<http://www.pingan.com/pw/11.htm>

	static uint8 advertData[] = 
	{
	  0x02,
	  GAP_ADTYPE_FLAGS,
	  GAP_ADTYPE_FLAGS_GENERAL|GAP_ADTYPE_FLAGS_BREDR_NOT_SUPPORTED,
  
	  0x03,  // length
	  0x03,  // Param: Service List
	  0xD8, 0xFE,  // URI Beacon ID
  
	  0x16,  // length
	  0x16,  // Service Data
	  0xD8, 0xFE, // URI Beacon ID
	  0x00,  // flags
	  0xC5,  // power
	  0x00,  // http://www.
	  'p','i','n','g','a','n',
	  0x00,  // .".com"
	  'p','w','/','1','1','.','h','t','m',
	};