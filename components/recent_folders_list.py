from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import datetime

class FolderItem(QWidget):
    def __init__(self, folder_name, icon_path, last_modified, sync_status):
        super().__init__()
        layout = QHBoxLayout()
        
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(icon_path).pixmap(24, 24))
        layout.addWidget(icon_label)
        
        name_label = QLabel(folder_name)
        layout.addWidget(name_label)
        
        last_modified_label = QLabel(last_modified)
        layout.addWidget(last_modified_label)
        
        sync_status_label = QLabel(sync_status)
        layout.addWidget(sync_status_label)
        
        self.setLayout(layout)

class RecentFoldersList(QWidget):
    def __init__(self, switch_to_file_management_page):
        super().__init__()

        self.switch_to_file_management_page = switch_to_file_management_page

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建标题
        self.title_label = QLabel()
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(self.title_label)

        # 创建文件夹列表
        self.folder_list = QListWidget()
        main_layout.addWidget(self.folder_list)

        # 创建操作按钮布局
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        # 创建操作按钮
        pause_button = QPushButton("暂停同步")
        rescan_button = QPushButton("重新扫描")
        add_sync_button = QPushButton("添加同步文件")
        add_sync_button.clicked.connect(self.switch_to_file_management_page)  # 连接按钮点击信号到切换页面的槽函数

        # 调整按钮宽度
        pause_button.setFixedWidth(100)
        rescan_button.setFixedWidth(100)
        add_sync_button.setFixedWidth(100)

        button_layout.addWidget(pause_button)
        button_layout.addWidget(rescan_button)
        button_layout.addWidget(add_sync_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.update_folder_list()

    def update_folder_list(self):
        folder_info = [
            ("文件夹1", "icons/recent_folders/folder.svg", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "正在同步"),
            ("文件夹2", "icons/recent_folders/folder.svg", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "5分钟前"),
            ("文件夹3", "icons/recent_folders/folder.svg", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "最新")
        ]
        self.folder_list.clear()
        for folder_name, icon, last_modified, sync_status in folder_info:
            item_widget = FolderItem(folder_name, icon, last_modified, sync_status)
            item = QListWidgetItem(self.folder_list)
            item.setSizeHint(item_widget.sizeHint())
            self.folder_list.setItemWidget(item, item_widget)
        self.title_label.setText(f"最近文件（{len(folder_info)}）")