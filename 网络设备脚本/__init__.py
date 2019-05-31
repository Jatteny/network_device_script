#===============================================================================
# 脚本基础
#===============================================================================
#操作
from .基础接口 import 操作
E操作 = 操作.E操作
E方向 = 操作.E方向
E自动提交 = 操作.E自动提交
#协议
from .基础接口 import 协议
E协议 = 协议.E协议
#===============================================================================
# 设备基础
#===============================================================================
#接口
from .基础接口 import 接口
S接口 = 接口.S接口
E接口 = 接口.E接口
E接口分类 = 接口.E接口分类
#时间范围
from .基础接口 import 时间范围
E日子 = 时间范围.E日子
S时间范围 = 时间范围.S时间范围
#用户
from .基础接口 import 用户
E服务类型 = 用户.E服务类型
#登录
from .基础接口 import 登录
E登录方式 = 登录.E登录方式
E登录认证方式 = 登录.E登录认证方式
E登录协议 = 登录.E登录协议
#访问控制列表
from .基础接口 import 访问控制列表
E访问控制列表类型 = 访问控制列表.E类型
S访问控制列表规则 = 访问控制列表.S规则
S端口号 = 访问控制列表.S端口号
S统一序号 = 访问控制列表.S统一序号
#前缀列表
from .基础接口 import 前缀列表
S前缀列表规则 = 前缀列表.S规则
#===============================================================================
# 路由
#===============================================================================
#路由基础
from .基础接口 import 路由
E路由协议 = 路由.E路由协议
S路由条目 = 路由.S路由条目
#开放最短路径优先
from .基础接口 import 开放最短路径优先
E开放最短路径优先链路状态通告类型 = 开放最短路径优先.E链路状态通告类型
E开放最短路径优先邻居状态 = 开放最短路径优先.E邻居状态
E开放最短路径优先选举状态 = 开放最短路径优先.E选举状态
#中间系统到中间系统
from .基础接口 import 中间系统到中间系统
E中间系统到中间系统级别 = 中间系统到中间系统.E级别
S中间系统到中间系统网络标识 = 中间系统到中间系统.S网络标识
#边界网关协议
from .基础接口 import 边界网关协议
E边界网关协议地址族 = 边界网关协议.E地址族
#===============================================================================
# 交换
#===============================================================================
#虚拟局域网
from .基础接口 import 虚拟局域网
E链路类型 = 虚拟局域网.E链路类型