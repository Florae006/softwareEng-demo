from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class LocalDeviceInfo(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建标题
        self.title_label = QLabel("此设备")
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(self.title_label)

        # 创建设备信息列表
        self.device_list = QListWidget()
        self.device_list.setStyleSheet("""
            QListWidget::item {
                padding: 0px;  /* 设置内边距 */
                margin: 3px;   /* 设置外边距 */
                border: none;
                font-size: 14px;
                vertical-align: middle;  /* 垂直居中 */
            }
            QListWidget::item:selected {
                background-color: #f0f0f0;  /* 设置选中时的背景颜色 */
                color: black;  /* 设置选中时的文字颜色 */
            }
        """)
        local_info = [
            ("CPU: 4核", "icons/local_info/cpu.svg"),
            ("内存: 8GB", "icons/local_info/memory.svg"),
            ("存储: 256GB", "icons/local_info/storage.svg"),
            ("上传速率: 100Mbps", "icons/local_info/upload.svg"),
            ("下载速率: 200Mbps", "icons/local_info/download.svg"),
            ("启动时间: 2023-01-01 08:00:00", "icons/local_info/uptime.svg"),
            ("标志: Windows", "icons/local_info/flag.svg"),
            ("操作系统: Windows 10", "icons/local_info/os.svg"),
            ("命名: MyComputer", "icons/local_info/name.svg")
        ]
        for text, icon in local_info:
            item = QListWidgetItem(QIcon(icon), text)
            self.device_list.addItem(item)

        main_layout.addWidget(self.device_list)
        self.setLayout(main_layout)