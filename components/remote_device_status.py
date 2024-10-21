from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMenu, QToolButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class DeviceItem(QWidget):
    def __init__(self, device_name, status, icon):
        super().__init__()

        # 创建水平布局
        layout = QHBoxLayout()

        # 创建图标容器
        icon_container = QWidget()
        icon_layout = QVBoxLayout()
        icon_layout.setContentsMargins(0, 0, 0, 0)
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(icon).pixmap(24, 24))
        icon_layout.addWidget(icon_label)
        icon_container.setLayout(icon_layout)
        icon_container.setFixedSize(40, 40)  # 设置固定大小
        layout.addWidget(icon_container)

        # 创建设备名标签
        device_name_label = QLabel(device_name)
        device_name_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))  # 设置字体大小和加粗
        device_name_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)  # 垂直居中
        layout.addWidget(device_name_label)

        # 创建在线状态标签
        status_label = QLabel(status)
        status_label.setFont(QFont("Arial", 12))  # 设置字体大小
        status_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)  # 垂直居中和靠右对齐
        if status == "在线中":
            status_label.setStyleSheet("color: green;")
        else:
            status_label.setStyleSheet("color: red;")
        layout.addWidget(status_label)

        # 创建下拉按钮
        dropdown_button = QToolButton()
        dropdown_button.setText("...")
        dropdown_button.setFixedWidth(50)  # 设置按钮宽度
        dropdown_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        dropdown_menu = QMenu()
        dropdown_menu.addAction("立即连接")
        dropdown_menu.addAction("断开连接")
        dropdown_menu.addAction("删除设备")
        dropdown_button.setMenu(dropdown_menu)
        layout.addWidget(dropdown_button)

        # 设置下拉菜单样式
        dropdown_menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 1px solid #ccc;
                padding: 2px;
            }
            QMenu::item {
                padding: 2px 20px;
                border: none;
            }
            QMenu::item:selected {
                background-color: #f0f0f0;
            }
        """)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 2px;
                margin: 0px;
            }
            QLabel {
                border: none;
            }
            QToolButton {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 2px;
            }
        """)

class RemoteDeviceStatus(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建标题
        self.title_label = QLabel()
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(self.title_label)

        # 创建设备列表
        self.device_list = QListWidget()
        main_layout.addWidget(self.device_list)

        self.setLayout(main_layout)
        self.update_device_list()

    def update_device_list(self):
        remote_info = [
            ("设备1", "在线中", "icons/remote_info/online.svg"),
            ("设备2", "已断开连接", "icons/remote_info/offline.svg"),
            ("设备3", "在线中", "icons/remote_info/online.svg")
        ]
        self.device_list.clear()
        for device_name, status, icon in remote_info:
            item_widget = DeviceItem(device_name, status, icon)
            item = QListWidgetItem(self.device_list)
            item.setSizeHint(item_widget.sizeHint())
            self.device_list.setItemWidget(item, item_widget)
        self.title_label.setText(f"远程连接设备（{len(remote_info)}）")