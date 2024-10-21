from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSplitter, QGraphicsBlurEffect, QMenuBar, QMenu, QToolButton, QStackedWidget
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt

from components.recent_folders_list import RecentFoldersList
from components.local_device_info import LocalDeviceInfo
from components.remote_device_status import RemoteDeviceStatus
from layouts.file_management_page import FileManagementPage  # 文件管理页面的组件

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("设备信息展示")
        self.resize(1000, 600)  # 调整窗口大小

        # 设置窗口透明度
        self.setWindowOpacity(0.9)

        # 创建菜单栏
        menu_bar = self.menuBar()

        # 创建文件菜单
        file_menu = menu_bar.addMenu("文件")

        # 创建设置菜单
        settings_menu = menu_bar.addMenu("设置")

        # 创建帮助菜单
        help_menu = menu_bar.addMenu("帮助")

        # 添加菜单项
        open_action = QAction("打开", self)
        save_action = QAction("保存", self)
        exit_action = QAction("退出", self)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        preferences_action = QAction("首选项", self)
        settings_menu.addAction(preferences_action)

        about_action = QAction("关于", self)
        help_menu.addAction(about_action)

        # 创建主题切换按钮
        self.theme_switch_button = QToolButton(self)
        self.theme_switch_button.setIcon(QIcon("icons/theme_switch/moon.svg"))  # 初始图标为月亮
        self.theme_switch_button.setCheckable(True)
        self.theme_switch_button.toggled.connect(self.toggle_theme)
        menu_bar.setCornerWidget(self.theme_switch_button, Qt.Corner.TopRightCorner)

        # 创建堆叠窗口
        self.stacked_widget = QStackedWidget()

        # 创建设备信息页面
        device_info_widget = QWidget()
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # 左侧部分：最近打开的文件夹列表
        self.recentFoldersList = RecentFoldersList(self.switch_to_file_management_page)
        splitter.addWidget(self.recentFoldersList)

        # 右侧部分：本地设备信息和远程设备在线情况
        rightWidget = QWidget()
        rightLayout = QVBoxLayout()

        # 上半部分：本地设备信息
        self.localDeviceInfo = LocalDeviceInfo()
        rightLayout.addWidget(self.localDeviceInfo)

        # 下半部分：远程设备在线情况
        self.remoteDeviceStatus = RemoteDeviceStatus()
        rightLayout.addWidget(self.remoteDeviceStatus)

        rightWidget.setLayout(rightLayout)
        splitter.addWidget(rightWidget)

        # 设置左侧部分的比例为 3，右侧部分的比例为 2
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        device_info_layout = QVBoxLayout()
        device_info_layout.addWidget(splitter)
        device_info_widget.setLayout(device_info_layout)

        # 添加设备信息页面到堆叠窗口
        self.stacked_widget.addWidget(device_info_widget)

        # 创建文件管理页面
        self.file_management_page = FileManagementPage()
        self.stacked_widget.addWidget(self.file_management_page)

        self.setCentralWidget(self.stacked_widget)

        # 设置暗色主题样式表
        self.set_dark_theme()

    def switch_to_file_management_page(self):
        # 实现切换到文件管理页面的逻辑
        self.stacked_widget.setCurrentWidget(self.file_management_page)

    def set_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QListWidget {
                background: rgba(43, 43, 43, 0.5);  /* 半透明背景 */
                border: none;
                color: #ffffff;
            }
            QListWidget::item {
                padding: 2px;  /* 设置内边距 */
                margin: 0px;   /* 设置外边距 */
                border: none;
                font-size: 14px;
                vertical-align: middle;  /* 垂直居中 */
            }
            QListWidget::item:selected {
                background-color: #3a3a3a;  /* 设置选中时的背景颜色 */
                color: #ffffff;  /* 设置选中时的文字颜色 */
            }
            QPushButton {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
                padding: 3px;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QToolButton {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
                padding: 3px;
            }
            QToolButton:hover {
                background-color: #4a4a4a;
            }
            QMenu {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #555555;
            }
            QMenu::item {
                padding: 5px 20px;
                border: none;
            }
            QMenu::item:selected {
                background-color: #4a4a4a;
            }
        """)

    def set_light_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
                color: #000000;
            }
            QWidget {
                background-color: #ffffff;
                color: #000000;
            }
            QLabel {
                color: #000000;
            }
            QListWidget {
                background: rgba(255, 255, 255, 0.5);  /* 半透明背景 */
                border: none;
                color: #000000;
            }
            QListWidget::item {
                padding: 2px;  /* 设置内边距 */
                margin: 0px;   /* 设置外边距 */
                border: none;
                font-size: 14px;
                vertical-align: middle;  /* 垂直居中 */
            }
            QListWidget::item:selected {
                background-color: #e0e0e0;  /* 设置选中时的背景颜色 */
                color: #000000;  /* 设置选中时的文字颜色 */
            }
            QPushButton {
                background-color: #e0e0e0;
                color: #000000;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                padding: 3px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QToolButton {
                background-color: #e0e0e0;
                color: #000000;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                padding: 3px;
            }
            QToolButton:hover {
                background-color: #d0d0d0;
            }
            QMenu {
                background-color: #e0e0e0;
                color: #000000;
                border: 1px solid #aaaaaa;
            }
            QMenu::item {
                padding: 5px 20px;
                border: none;
            }
            QMenu::item:selected {
                background-color: #d0d0d0;
            }
        """)

    def toggle_theme(self, checked):
        if checked:
            self.set_light_theme()
            self.theme_switch_button.setIcon(QIcon("icons/theme_switch/sun.svg"))  # 切换为太阳图标
        else:
            self.set_dark_theme()
            self.theme_switch_button.setIcon(QIcon("icons/theme_switch/moon.svg"))  # 切换为月亮图标