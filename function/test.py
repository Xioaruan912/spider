# 启动浏览器-开始★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
def launchBrowser(self):
    self.loadingOverlay.show_message("正在启动浏览器....", color='white')
    QApplication.processEvents()
    try:
        # 关闭所有 Chrome 实例
        try:
            subprocess.run(["taskkill", "/IM", "chrome.exe", "/F"], check=True)
            print("Closed all existing Chrome instances.")
        except subprocess.CalledProcessError as e:
            print(f"No existing Chrome instances or unable to close: {e}")
        # 设置Chrome的选项
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")  # 隐藏"Chrome正受到自动测试软件的控制"的通知
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 防止显示该信息
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 不使用自动化扩展
        chrome_options.add_experimental_option("detach", True)

        if self.browser_path:
            chrome_options.binary_location = self.browser_path
        # 可以添加其它启动参数来满足你的需求
        chrome_options.add_argument("window-size=1500,1400")  # 设置窗口大小为宽 * 高
        # 设置用户数据目录
        user_data_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data')
        profile_directory = "Default"  # 保持不变，除非你需要从输入框获取不同的配置文件

        chrome_options.add_argument(f"user-data-dir={user_data_dir}")
        chrome_options.add_argument(f"profile-directory={profile_directory}")

        # 设置Chrome的启动参数
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-background-networking")
        chrome_options.add_argument("--remote-debugging-port=9255")
        chrome_options.add_argument("--window-position=1050,0")  # 设置窗口起始位置为屏幕坐标(100,100)
        chrome_options.add_argument("--excludeswitches=enable-automation")
        chrome_options.add_argument("--useautomationextension=false")

        # 检查驱动是否存在于指定路径
        chromedriver_executable_path = self.chromedriver_path + 'chromedriver.exe'
        if not os.path.exists(chromedriver_executable_path):
            os.makedirs(self.chromedriver_path)
            # 1.使用ChromeDriverManager自动管理ChromeDriver，如果没有则自动下载
            driver_path = ChromeDriverManager().install()
            # 2.把下载的驱动文件，复制到指定位置
            shutil.copy(driver_path, self.chromedriver_path)

        # 设置ChromeDriver
        service = Service(chromedriver_executable_path)

        # 初始化WebDriver并赋值给self.driver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        # 打开目标网页
        self.driver.get('https://myseller.taobao.com/home.htm/QnworkbenchHome/')
        self.loadingOverlay.show_message("启动成功！", color='#00FA9A')
    except Exception as e:
        print(f'An error occurred: {e}')
        self.loadingOverlay.show_message("启动失败！", color='red')
    finally:
        # 短暂延迟后隐藏提示
        QTimer.singleShot(500, self.loadingOverlay.hide_overlay)