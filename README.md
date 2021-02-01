# 颜如玉
yry（颜如玉）—— 一个实现人脸融合的算法，可以接近腾讯天天P图疯狂变脸功能的效果


## 接口

地址：http://172.18.16.32:5000

### 上传

`POST /files/`

```json
{
    "file": <file>
}
```

Response 200:

```json
{
    "filename": "uploads/<filename>",
    "url": "http://<ip>:<port>/uploads/<filename>"
}
```

### 换脸

`POST /face-swap/`

```json
{
    "src_image": <filename>,
    "face_image": <filename>
}
```

Response:

```json
{
    "code": 200,
    "msg": "success",
    "image_url": "http://{HOST}:{PORT}/{ofn}",
}
```

# 效果
国际惯例先放效果对照图，左边为天天p图融合效果，右边为颜如玉融合效果：
![](http://curzbin.oss-cn-shenzhen.aliyuncs.com/compare.jpg)

# 使用
python 安装 requirements.txt 依赖后运行 ModuleTest.py

