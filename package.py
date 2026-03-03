#!/usr/bin/env python3
"""
网站打包脚本
将所有相关文件打包为zip压缩文件
"""


def create_package():
    """创建网站打包文件"""
    package_name = "stock_analysis_website.zip"
    
    # 明确指定需要打包的文件列表
    files_to_pack = [
        "index.html",
        "README.md", 
        "deploy.md",
        "server.py",
        "package.py"
    ]
    
    # 检查文件是否存在
    existing_files = []
    for file in files_to_pack:
        if os.path.exists(file):
            existing_files.append(file)
        else:
            print(f"警告: {file} 不存在，将跳过")
    
    if not existing_files:
        raise FileNotFoundError("没有找到任何需要打包的文件")
    
    # 创建zip文件
    with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in existing_files:
            zipf.write(file)
            print(f"已添加文件: {file}")
    
    print(f"\n打包完成！文件: {package_name}")
    print(f"包含文件数量: {len(existing_files)}")
    
    # 显示包内容
    print("\n包内文件列表:")
    with zipfile.ZipFile(package_name, 'r') as zipf:
        file_list = zipf.namelist()
        for filename in file_list:
            file_info = zipf.getinfo(filename)
            print(f"  {filename} ({file_info.file_size} bytes)")
    
    return package_name

if __name__ == "__main__":
    try:
        package_file = create_package()
        print(f"\n打包成功！请下载 {package_file} 文件进行部署。")
    except Exception as e:
        print(f"打包失败: {e}")
