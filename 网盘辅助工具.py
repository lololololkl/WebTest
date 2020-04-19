import os
import time
import tkinter as tk
from tkinter.filedialog import (askopenfilename, 
                                    askopenfilenames, 
                                    askdirectory, 
                                    asksaveasfilename)
#调用系统自带的GUI目录选择界面，选择要处理的文件的目录。
root = tk.Tk()
pth=askdirectory()

#将文件大小按照适当的单位表示。
def size_format(size):
    if size < 1000:
        return '%i' % size + 'B'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'
#主函数，由于是从我的其他程序复制过来的，函数名没有改。
def clear(path):
    # 先将生成的网页的头部内容添加到字符串。
    html='''<!-- CJH's 文件传输专用标识-->
<html><head>
        <title>CJH's 文件</title>
        <link rel="shortcut icon" href="https://cjh0613.gitee.io/cjh-doc-transfer/3/resources/themes/bootstrap/img/folder.png"> <!-- 网站LOGO -->
         <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.4/css/bootstrap.min.css"> <!-- CSS基本库 -->
        <link rel="stylesheet" href="https://cdn.bootcss.com/font-awesome/4.3.0/css/font-awesome.min.css"> <!-- 网站图标CSS式样 -->
        <link rel="stylesheet" href="https://cjh0613.gitee.io/cjh-doc-transfer/3/resources/themes/bootstrap/css/style.css"> <!-- 网站主要式样 -->
        <link rel="stylesheet" href="https://cdn.bootcss.com/prism/0.0.1/prism.css"> <!-- 代码高亮式样 -->
        <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script> <!-- JS基本库 -->
		<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.4/js/bootstrap.min.js"></script> <!-- JS基本库 -->
		<script src="https://cdn.bootcss.com/prism/0.0.1/prism.js"></script> <!-- 代码高亮JS依赖 -->
        <meta name=renderer  content=webkit>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <!--统计代码-->
   <script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? "https://" : "http://");</script>
<script type="text/javascript" src="https://js.users.51.la/20194229.js"></script>
        <script>
		//百度统计
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?3571f7725019f0e61870427684c3ce17";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
            </head>
    <body>
        <div id="page-navbar" class="path-top navbar navbar-default navbar-fixed-top">
            <div class="container">
                                <p class="navbar-text">
                                                                        CJH's 文件传输                                                            </p>
            </div>
        </div>
        <div class="path-announcement navbar navbar-default navbar-fixed-top">
            <div class="path-announcement2 container">
                <!-- 顶部公告栏 -->
		    <p><i class="fa fa-volume-down"></i>公告：可用Ctrl+f快捷键搜索。  本网页暂未完成全部适配，从窄屏设备访问可能无法看到文件大小、最后修改时间</p>
            	<!-- 顶部公告栏 -->
            </div>
        </div>
		<div class="container" id="container_top" style="">
		<div class="page-content container" id="container_page">
            <!--本文件可以放置 统计代码等。-->
                        <div id="directory-list-header">
                <div class="row">
                    <div class="col-md-7 col-sm-6 col-xs-10">文件</div>
                    <div class="col-md-2 col-sm-2 col-xs-2 text-right">大小</div>
                    <div class="col-md-3 col-sm-4 hidden-xs text-right">最后修改时间</div>
                </div>
            </div>
            <ul id="directory-listing" class="nav nav-pills nav-stacked">'''
    #获取目录中的所有文件和文件夹名字
    directoryListing=''
    dir_list = os.listdir(path)
    # 遍历循环每个目录
    for i in dir_list:
        # 拼接绝对路径
        abspath = os.path.join(os.path.abspath(path), i)
        a='./'+i
        # 判断是否是不为"index.html"及"文件列表.html"的文件，如果是，向存储网页源代码的字符串中添加显示此文件的代码。
        if os.path.isfile(abspath) and i!='index.html' and i!='文件列表.html':
            print(i)
	
            directoryListing = directoryListing+'''<li data-name="'''+i+'''" data-href="'''+a+'''">
                        <a href="'''+a+'''" class="clearfix" data-name="'''+i+'''">
                            <div class="row">
                                <span class="file-name col-md-7 col-sm-6 col-xs-9">
                                    <i class="fa '''
            #根据拓展名判断文件类型，添加文件列表中每个文件项目的开头的logo。
            if i.endswith(r'.py') or i.endswith(r'.c') or i.endswith(r'.class') or i.endswith(r'.cpp') or i.endswith(r'.css') or i.endswith(r'.erb') or i.endswith(r'.htm') or i.endswith(r'.html') or i.endswith(r'.java') or i.endswith(r'.js') or i.endswith(r'.php') or i.endswith(r'.pl') or i.endswith(r'.rb') or i.endswith(r'.xhtml') or i.endswith(r'.xml'):
                directoryListing +='fa-code'
            elif i.endswith(r'.7z') or i.endswith(r'.zip') or i.endswith(r'.gz') or i.endswith(r'.rar') or i.endswith(r'.tar') or i.endswith(r'.bz') :
                directoryListing +='fa-file-archive-o'
            elif i.endswith(r'.mp3') or i.endswith(r'.wma') or i.endswith(r'.wav') or i.endswith(r'.aac') or i.endswith(r'.flac') or i.endswith(r'.mid') or i.endswith(r'.midi') or i.endswith(r'.ogg'):
                directoryListing +='fa-music'
            elif i.endswith(r'.mdb') or i.endswith(r'.sql') or i.endswith(r'.db') or i.endswith(r'.accdb') or i.endswith(r'.dbf') or i.endswith(r'.pdb') :
                directoryListing +='fa-hdd-o'
            elif i.endswith(r'.pdf') or i.endswith(r'.xlsx') or i.endswith(r'.xls') or i.endswith(r'.docx') or i.endswith(r'.doc') or i.endswith(r'.csv') or i.endswith(r'.odt') :
                directoryListing +='fa-file-text'
            elif i.endswith(r'.apk') or i.endswith(r'.exe') or i.endswith(r'.app') or i.endswith(r'.msi') or i.endswith(r'.jar') or i.endswith(r'.vb') or i.endswith(r'.com'):
                directoryListing +='fa-list-alt'
            elif i.endswith(r'.ttf') or i.endswith(r'.otf') or i.endswith(r'.eot') or i.endswith(r'.woff'):
                directoryListing +='fa-font'
            elif i.endswith(r'.gam') or i.endswith(r'.nes') or i.endswith(r'.rom') or i.endswith(r'.sav'):
                directoryListing +='fa-gamepad'
            elif i.endswith(r'.jpg') or i.endswith(r'.gif') or i.endswith(r'.png') or i.endswith(r'.jpeg') or i.endswith(r'.psd') or i.endswith(r'.bmp') or i.endswith(r'.tga') or i.endswith(r'.tif'):
                directoryListing +='fa-picture-o'
            elif i.endswith(r'.deb') or i.endswith(r'.rpm') or i.endswith(r'.box'):
                directoryListing +='fa-archive'
            elif i.endswith(r'.sh') or i.endswith(r'.bat') or i.endswith(r'.cmd') :
                directoryListing +='fa-terminal'
            elif i.endswith(r'.txt') or i.endswith(r'.md') or i.endswith(r'.log') or i.endswith(r'.ini') or i.endswith(r'.rtf') or i.endswith(r'.cfg'):
                directoryListing +='fa-file-text'
            elif i.endswith(r'.ai') or i.endswith(r'.drw') or i.endswith(r'.eps') or i.endswith(r'.ps') or i.endswith(r'.svg'):
                directoryListing +='fa-picture-o'
            elif i.endswith(r'.mp4') or i.endswith(r'.mkv') or i.endswith(r'.rmvb') or i.endswith(r'.swf') or i.endswith(r'.flv') or i.endswith(r'.avi') or i.endswith(r'.mov') or i.endswith(r'.mpg') or i.endswith(r'.ogv') or i.endswith(r'.wmv') or i.endswith(r'.webm') :
                directoryListing +='fa-youtube-play'
            elif i.endswith(r'.bak'):
                directoryListing +='fa-floppy'
            elif i.endswith(r'.msg'):
                directoryListing +='fa-envelope'
            else:
                directoryListing +='fa-file'
            #添加文件列表的每个文件名的尾部源代码。
            directoryListing = directoryListing+''' fa-fw"></i>
                                    '''+i+'''                                </span>
                                <span class="file-size col-md-2 col-sm-2 col-xs-3 text-right">
                                    '''+size_format(os.path.getsize(abspath))+'''                                </span>
                                <span class="file-modified col-md-3 col-sm-4 hidden-xs text-right">
                                    '''+time.ctime(os.path.getatime(abspath))+'''                                </span>
                            </div>
                        </a>
                                                                                                </li>'''
        #如果是文件夹        
        if os.path.isdir(abspath):
            #如果文件夹名为.git就跳过，因为这是git的文件夹，如果对这个文件夹执行我们的函数生成文件，可能会导致严重的错误。
            if i=='.git':
                print('发现并pass ".git"')
            #为文件夹添加文件列表项目。
            else:
                directoryListing = directoryListing+'''<li data-name="'''+i+'''" data-href="'''+a+'''">
                        <a href="'''+a+'''" class="clearfix" data-name="'''+i+'''">
                            <div class="row">
                                <span class="file-name col-md-7 col-sm-6 col-xs-9">
                                    <i class="fa fa-folder fa-fw"></i>
                                    '''+i+'''                                </span>
                                <span class="file-size col-md-2 col-sm-2 col-xs-3 text-right">
                                    -                                </span>
                                <span class="file-modified col-md-3 col-sm-4 hidden-xs text-right">
                                    '''+time.ctime(os.path.getatime(abspath))+'''                                </span>
                            </div>
                        </a>
                                                                                                </li>'''
                #再次调用自身函数
                clear(abspath)
    html=html+directoryListing+''' </ul>
        </div>
		<!-- READMNE 说明 -->
				<!-- READMNE 说明 -->
        </div>
      <hr id="footer_hr" style="margin-bottom: 0px; margin-top: 40px;">
      <footer class="container">
  <div class="footer">
 © 2019.4.8-2020 <a href="https://cjh0613.gitee.io/blog" target="_blank">CJH</a> . All rights reserved.
   </div>
   
</footer>
<script type="text/javascript">
window.onload=function(){  
	changeDivHeight();  
}  
window.onresize=function(){  
	changeDivHeight();  
}  
function changeDivHeight(){
	if(document.getElementById("container_readme"))
	{
		container_readme.style.marginBottom = '0';
	}
	
  	ScrollHeight_body=document.body.offsetHeight;
	InnerHeight_window=window.innerHeight;
	container_top.style.minHeight = '0';
	ClientHeight_top=container_top.clientHeight+60;
	ClientHeight_top1=ClientHeight_top+69;
	ClientHeight_top2=ClientHeight_top1-60;
	
	//console.log(ScrollHeight_body, InnerHeight_window, container_top.clientHeight, ClientHeight_top, ClientHeight_top1, ClientHeight_top2, InnerHeight_window);
	container_top.style.minHeight = '';
	
	if (ScrollHeight_body > ClientHeight_top2)
	{
		footer_hr.style.marginTop = '0';
	}
	else
	{
		footer_hr.style.marginTop = '40px';
	}
	
	if (ScrollHeight_body > InnerHeight_window)
	{
		if (ClientHeight_top > InnerHeight_window)
		{
			container_top.style.marginBottom = '0';
			container_page.style.marginBottom = '0';
			if(document.getElementById("container_readme"))
			{
				container_readme.style.marginTop = '20px';
			}
		}
		else
		{
			footer_hr.style.marginTop = '40px';
			container_top.style.marginBottom = '';
			container_page.style.marginBottom = '';
			if(document.getElementById("container_readme"))
			{
				container_readme.style.marginTop = '';
			}
		}
	}
	else
	{
		if (ScrollHeight_body < ClientHeight_top1)
		{
			container_top.style.marginBottom = '0';
			container_page.style.marginBottom = '0';
			if(document.getElementById("container_readme"))
			{
				container_readme.style.marginTop = '20px';
			}
		}
		else
		{
			footer_hr.style.marginTop = '40px';
			container_top.style.marginBottom = '';
			container_page.style.marginBottom = '';
			if(document.getElementById("container_readme"))
			{
				container_readme.style.marginTop = '';
			}
		}
	}
}
</script>
    

</body></html>'''
    #拼合文件的绝对路径。
    filename = path+'/index.html'
    #my_file = Path("/path/to/file")
    #如果存在此文件。
    if os.path.isfile(filename):
        #filename = path+'/index.html'
        #检查文件内容是否有标识来判断这个文件是不是我们已经生成过的显示文件列表的html文件。
        with open(filename, 'r', encoding = "utf8") as f:
            flag=f.read(22)
            f.close()
        #如果有标识的话直接覆盖。
        if flag=="<!-- CJH's 文件传输专用标识-->":
            print('有标识')
            filename = path+'/index.html'
            with open(filename, 'wb') as f:
                f.write(bytes(html, encoding = "utf8"))
                f.close()
        #如果没有标识的话，新建一个名为文件列表的html文件。
        else:
            print('无标识')
            filename = path+'/文件列表.html'
            with open(filename, 'wb') as f:
                f.write(bytes(html, encoding = "utf8"))
                f.close()
    #没有index.html文件的话直接创建。
    else:
        print('无文件')
        filename = path+'/index.html'
        with open(filename, 'wb') as f:
            f.write(bytes(html, encoding = "utf8"))
            f.close()
    print('完成')
clear(pth)
##源码来自
####https://cjh0613.gitee.io/blog/github%E7%BD%91%E7%9B%98%E8%BE%85%E5%8A%A9%E5%B7%A5%E5%85%B7.html
