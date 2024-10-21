from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QStackedWidget, QHBoxLayout
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class FileManagementPage(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主布局
        main_layout = QHBoxLayout()

        # 创建左侧菜单栏
        self.menu_tree = QTreeWidget()
        self.menu_tree.setHeaderHidden(True)
        self.menu_tree.setFixedWidth(250)  # 设置固定宽度
        self.menu_tree.setStyleSheet("""
            QTreeWidget {
                font-size: 14px;
                font-weight: bold;
                color: #000000;  /* 设置文字颜色 */
            }
            QTreeWidget::item {
                padding: 5px;
                margin: 2px;
                transition: background-color 0.3s ease;  /* 添加过渡效果 */
            }
            QTreeWidget::item:selected {
                background-color: #d3d3d3;  /* 设置选中时的背景颜色 */
                color: #000000;  /* 设置选中时的文字颜色 */
                border: none;  /* 去掉边框高亮 */
            }
            QTreeWidget::item:focus {
                outline: none;  /* 去掉虚线效果 */
            }
        """)

        # 添加菜单项
        my_files = QTreeWidgetItem(["我的文件"])
        my_files.setIcon(0, QIcon("icons/file_manage/my_files.svg"))
        shared_files = QTreeWidgetItem(["共享文件"])
        shared_files.setIcon(0, QIcon("icons/file_manage/shared_files.svg"))
        external_storage = QTreeWidgetItem(["外接存储"])
        external_storage.setIcon(0, QIcon("icons/file_manage/external_storage.svg"))
        remote_mount = QTreeWidgetItem(["远程挂载"])
        remote_mount.setIcon(0, QIcon("icons/file_manage/remote_mount.svg"))

        terminal = QTreeWidgetItem(["终端"])
        terminal.setIcon(0, QIcon("icons/file_manage/terminal.svg"))
        app_files = QTreeWidgetItem(["应用文件"])
        app_files.setIcon(0, QIcon("icons/file_manage/app_files.svg"))
        recent_access = QTreeWidgetItem(["最近访问"])
        recent_access.setIcon(0, QIcon("icons/file_manage/recent_access.svg"))
        my_favorites = QTreeWidgetItem(["我的收藏"])
        my_favorites.setIcon(0, QIcon("icons/file_manage/my_favorites.svg"))
        recycle_bin = QTreeWidgetItem(["回收站"])
        recycle_bin.setIcon(0, QIcon("icons/file_manage/recycle_bin.svg"))

        self.menu_tree.addTopLevelItem(my_files)
        self.menu_tree.addTopLevelItem(shared_files)
        self.menu_tree.addTopLevelItem(external_storage)
        self.menu_tree.addTopLevelItem(remote_mount)
        self.menu_tree.addTopLevelItem(terminal)
        self.menu_tree.addTopLevelItem(app_files)
        self.menu_tree.addTopLevelItem(recent_access)
        self.menu_tree.addTopLevelItem(my_favorites)
        self.menu_tree.addTopLevelItem(recycle_bin)

        # 添加子菜单项
        my_files.addChild(QTreeWidgetItem(["子菜单项1"]))
        my_files.addChild(QTreeWidgetItem(["子菜单项2"]))
        shared_files.addChild(QTreeWidgetItem(["子菜单项1"]))
        shared_files.addChild(QTreeWidgetItem(["子菜单项2"]))
        external_storage.addChild(QTreeWidgetItem(["子菜单项1"]))
        external_storage.addChild(QTreeWidgetItem(["子菜单项2"]))
        remote_mount.addChild(QTreeWidgetItem(["子菜单项1"]))
        remote_mount.addChild(QTreeWidgetItem(["子菜单项2"]))

        # 创建右侧页面
        self.stacked_widget = QStackedWidget()

        # 创建并添加右侧页面
        self.my_files_page = self.create_page("我的文件页面")
        self.shared_files_page = self.create_page("共享文件页面")
        self.external_storage_page = self.create_page("外接存储页面")
        self.remote_mount_page = self.create_page("远程挂载页面")
        self.terminal_page = self.create_page("终端页面")
        self.app_files_page = self.create_page("应用文件页面")
        self.recent_access_page = self.create_page("最近访问页面")
        self.my_favorites_page = self.create_page("我的收藏页面")
        self.recycle_bin_page = self.create_page("回收站页面")

        self.stacked_widget.addWidget(self.my_files_page)
        self.stacked_widget.addWidget(self.shared_files_page)
        self.stacked_widget.addWidget(self.external_storage_page)
        self.stacked_widget.addWidget(self.remote_mount_page)
        self.stacked_widget.addWidget(self.terminal_page)
        self.stacked_widget.addWidget(self.app_files_page)
        self.stacked_widget.addWidget(self.recent_access_page)
        self.stacked_widget.addWidget(self.my_favorites_page)
        self.stacked_widget.addWidget(self.recycle_bin_page)

        # 连接菜单项点击事件
        self.menu_tree.itemClicked.connect(self.on_menu_item_clicked)

        main_layout.addWidget(self.menu_tree)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

    def create_page(self, title):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(title)
        label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def on_menu_item_clicked(self, item, column):
        text = item.text(0)
        if text == "我的文件":
            self.stacked_widget.setCurrentWidget(self.my_files_page)
        elif text == "共享文件":
            self.stacked_widget.setCurrentWidget(self.shared_files_page)
        elif text == "外接存储":
            self.stacked_widget.setCurrentWidget(self.external_storage_page)
        elif text == "远程挂载":
            self.stacked_widget.setCurrentWidget(self.remote_mount_page)
        elif text == "终端":
            self.stacked_widget.setCurrentWidget(self.terminal_page)
        elif text == "应用文件":
            self.stacked_widget.setCurrentWidget(self.app_files_page)
        elif text == "最近访问":
            self.stacked_widget.setCurrentWidget(self.recent_access_page)
        elif text == "我的收藏":
            self.stacked_widget.setCurrentWidget(self.my_favorites_page)
        elif text == "回收站":
            self.stacked_widget.setCurrentWidget(self.recycle_bin_page)

        # 折叠其他展开的项
        for i in range(self.menu_tree.topLevelItemCount()):
            top_item = self.menu_tree.topLevelItem(i)
            if top_item != item and top_item.isExpanded():
                top_item.setExpanded(False)

        # 展开当前项
        if item.childCount() > 0:
            item.setExpanded(True)