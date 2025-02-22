# 微步爬虫过拖拽验证码

分为linux与windows的

## linux

`run.sh` 用于设置环境 适用全新的linux环境

```shell
#/bin/sh
echo "开始初始化环境"
sudo apt update -y
sudo apt install libgl1-mesa-glx -y
apt install python3-pip -y
apt install unzip -y
sudo apt-get install libatk1.0-0 -y
apt --fix-broken install -y 
echo "配置基础环境结束"

```

`main.py` 开启项目 可选择本地或者Flask

```
    app.config['JSON_SORT_KEYS'] = False  #禁止排序
    app.run(host='0.0.0.0', port=5000)
```

`function/openChrome.py`

此处为主要Linux环境配置

```python
	chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # 共享内存问题
    chrome_options.add_argument("--single-process")
    temp_dir = os.environ.get('TMPDIR', '/tmp')  # 支持 Linux/macOS 和 Windows
    user_data_dir = os.path.join(temp_dir, f'chrome_dev_data_{os.getpid()}')
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    #反反爬虫
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")  # 浏览器窗口最大化
```

次处为主要环境监测 用于处理 linux的ChromeDriver

```
chrome_driver_path = r"""./Chorme_driver/"""
    chrome_driver = chrome_driver_path + 'chromedriver'

    if not os.path.exists(chrome_driver):
        if not os.path.exists(chrome_driver_path):
            logger.info("下载Chromedriver")
            os.mkdir(chrome_driver_path)
            os.system("chmod 777 " + chrome_driver_path)
        driver_path = ChromeDriverManager().install()
        logger.info("driver_path : " + driver_path)
        shutil.copy(driver_path, chrome_driver)
        logger.info("下载至:" + chrome_driver + "成功")
```

`function/Cvcheck.py`

```
def get_track(distance):
    track = []
    current = 0
    while current < distance:
        move = min(10, distance - current)  # 每次移动的最大步长为 10
        track.append(move)
        current += move
    return track
```

用于模拟人为拖拽 为关键 绕过拖拽验证码的

Windows如上 只是个别配置不同

## Flask请求方式

```
POST /search HTTP/1.1
Host:127.0.0.1:5000
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Type: application/json
Content-Length: 91

{
"username" :"xxx",
"password" : "xxxx",
"search_url" : "xxxx"
}
```

```shell
curl -X POST http://localhost:5000/search \
-H "Content-Type: application/json" \
-d '{
    "username": "your_username",
    "password": "your_password",
    "search_url": "baidu.com"
}'
```

