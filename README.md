# Princess connection -zh改进版

[TOC]

## 简介

此项目为国服公主连结脚本，参照大佬https://github.com/SimonShi1994/Princess-connection-farm，详细配置见大佬地址，我在这做一点改进，主要为培养农场号服务，适用有一定技术能力，自己能修改调试代码的骑士们，小白请去找大佬，如果有问题和侵权联系QQ：894791523

目前改进的功能有

1.挑战刷第一章-第五章，对于引导剧情没有做检测，只能手动来




## 环境

需要安装下列python包:

```
pip install opencv-python==3.* -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install uiautomator2 -i https://mirrors.aliyun.com/pypi/simple/
```

**重要：夜神模拟器分辨率要求540*960**


## 使用方式

夜神模拟器adb环境配置，或者本地Android sdk 配置，要保证夜神adb版本与android studio版本一直

参考：https://www.yeshen.com/faqs/H15tDZ6YW

adb 启动再打开模拟器！！！！

adb devices 查看

```
class Automator:
    def __init__(self, auto_task=False, auto_policy=True,
                 auto_goods=False, speedup=True):
        """
        device: 如果是 USB 连接，则为 adb devices 的返回结果；如果是模拟器，则为模拟器的控制 URL 。
        """
        self.d = u2.connect('127.0.0.1:62025') #adb devices 里面模拟器的端口号
        self.dWidth, self.dHeight = self.d.window_size()
        self.appRunning = False
```