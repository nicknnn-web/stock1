#!/usr/bin/env python3
"""
本地开发服务器脚本
用于在本地测试股票分析网站
"""


PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

def start_server():
    """启动本地服务器"""
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"本地服务器启动成功！")
        print(f"访问地址: http://localhost:{PORT}")
        print(f"按 Ctrl+C 停止服务器")
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        # 尝试打开浏览器（可选）
        def open_browser():
            time.sleep(1)
            webbrowser.open(f"http://localhost:{PORT}")
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        start_server()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as e:
        print(f"服务器启动失败: {e}")
        print("请确保端口8000未被占用")
