# HyperLPR Tornado WebAPI
基于HyperLPR搭建的中文车牌识别WebAPI，使用的Tornado提供WebAPI的服务。



- HTTP方法：post
> - 提交数据（Post Body）：
{
	"pic": "BASE64编码的图片，包含头部data:image/jpg;base64,部分"
}
> - 返回：
{
"result": "[{\"Name\": \"车牌\", \"Type\": \"车牌颜色\", \"Confidence\": 置信度, \"x\": 59, \"y\": 101, \"w\": 72, \"h\": 31}]",
"status":"ok" 或 "error"
}

- 示例1：

> 成功返回：
{
    "result": "[{\"Name\": \"云A127VT\", \"Type\": \"蓝牌\", \"Confidence\": 0.8350605836936406, \"x\": 59, \"y\": 101, \"w\": 72, \"h\": 31}]",
    "status": "ok"
}
