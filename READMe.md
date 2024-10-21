# 设备信息展示与文件管理系统

## 项目简介

本项目是一个设备信息展示与文件管理系统，旨在提供一个直观的界面来查看本地和远程设备的信息，并管理文件。项目采用 `PyQt6` 作为图形用户界面框架，提供了暗色和明亮主题切换功能。

## 功能特性

### 设备信息展示

- **最近打开的文件夹列表**：显示用户最近访问的文件夹。
- **本地设备信息**：展示本地设备的详细信息，包括 CPU、内存、存储等。
- **远程设备在线情况**：显示远程设备的在线状态。

### 文件管理

- **左侧菜单栏**：包含多个可以展开的菜单项和功能按钮。
  - 我的文件
  - 共享文件
  - 外接存储
  - 远程挂载
  - 终端
  - 应用文件
  - 最近访问
  - 我的收藏
  - 回收站
- **右侧内容展示区域**：根据左侧菜单项的选择展示相应的页面内容。

### 主题切换

- 提供暗色和明亮主题的切换功能，用户可以根据喜好选择不同的主题。

## 安装与运行

### 环境要求

- Python 3.8 及以上版本
- `PyQt6` 库
- `sip` 库

### 使用 `Poetry` 安装依赖

1. 克隆项目到本地

2. 使用 Poetry 安装依赖：

   ```bash
   poetry install
   ```
运行项目：
    
    ```bash
    poetry run python main.py
    ```

项目结构

```
project_root/
│
├── components/
│   ├── recent_folders_list.py
│   ├── local_device_info.py
│   └── remote_device_status.py
│
├── layouts/
│   ├── file_management_page.py
│   └── start_page.py
│
├── icons/
│   └── file_manage/
│       ├── my_files.svg
│       ├── shared_files.svg
│       ├── external_storage.svg
│       ├── remote_mount.svg
│       ├── terminal.svg
│       ├── app_files.svg
│       ├── recent_access.svg
│       ├── my_favorites.svg
│       └── recycle_bin.svg
│
├── main.py
├── README.md
└── pyproject.toml
```

使用说明

...