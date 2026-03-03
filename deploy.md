# 网站部署配置说明

## 静态网站部署（推荐）

### GitHub Pages
1. 将整个网站文件夹上传到GitHub仓库
2. 在仓库Settings → Pages中启用GitHub Pages
3. 选择main分支和根目录
4. 等待几分钟后即可通过 `https://username.github.io/repository-name/` 访问

### Netlify
1. 注册Netlify账号
2. 点击"New site from Git"，连接GitHub仓库
3. 选择对应的仓库和分支
4. 构建设置保持默认（因为是纯静态网站）
5. 点击"Deploy site"，等待部署完成

### Vercel
1. 注册Vercel账号
2. 导入GitHub仓库
3. 选择项目根目录（包含index.html的目录）
4. 等待自动部署完成

## 传统服务器部署

### Apache/Nginx服务器
1. 将整个网站文件夹上传到Web服务器的网站根目录
   - Apache: 通常为 `/var/www/html/`
   - Nginx: 通常为 `/usr/share/nginx/html/`
2. 确保index.html文件可被访问
3. 通过服务器IP地址或域名访问网站

### Windows IIS
1. 在IIS管理器中创建新网站
2. 设置物理路径为网站文件夹所在位置
3. 绑定域名或IP地址
4. 启动网站

## 域名绑定
- 购买域名后，在域名提供商控制面板设置A记录指向服务器IP
- 或设置CNAME记录指向GitHub Pages/Netlify/Vercel提供的域名

## 注意事项
1. **CDN依赖**：网站使用了外部CDN资源，确保服务器能正常访问以下域名：
   - cdn.tailwindcss.com
   - image.uc.cn  
   - cdn.staticfile.net
   
2. **HTTPS支持**：建议启用HTTPS以获得更好的安全性和性能

3. **缓存策略**：静态资源可设置长期缓存，HTML文件建议设置较短缓存时间

4. **移动端适配**：网站已响应式设计，支持各种设备访问

5. **浏览器兼容性**：支持现代浏览器（Chrome、Firefox、Safari、Edge最新版本）
