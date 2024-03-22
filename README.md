<div align="center">
<p>
 <img width="100px" src="https://raw.githubusercontent.com/NekoSilverFox/NekoSilverfox/403ab045b7d9adeaaf8186c451af7243f5d8f46d/icons/silverfox.svg" align="center" alt="NekoSilverfox" />
 <p align="center"><b><font size=6>OpenCV</font></b></p>
 <p align="center"><b>基于 Qt 和 C++ 的计算机视觉示例实现</b></p>
</p>



[![License](https://img.shields.io/badge/license-Apache%202.0-brightgreen)](LICENSE)
![Qt](https://img.shields.io/badge/Qt-Qt--6-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-OpenCV--3-orange)
![Language](https://img.shields.io/badge/Language-C++/Python-blue)



<div align="left">
<!-- 顶部至此截止 -->
<!-- SPbSTU 报告起始 -->

[toc]



# 前言

> 参考：
>
> 原文：[Computer Vision with OpenCV 3 and Qt5](https://1lib.org/book/3427589/3c1476)
>
> https://github.com/apachecn/apachecn-cv-zh/blob/0f2e14ca582d398ba3be22a1fff949077f4c85c0/docs/cv-opencv3-qt5
>
> 
>
> 原文：[Qt 5 and OpenCV 4 Computer Vision Projects](https://1lib.org/book/5220725/d23493)
>
> https://github.com/apachecn/apachecn-cv-zh/tree/0f2e14ca582d398ba3be22a1fff949077f4c85c0/docs/qt5-opencv4-cv-proj

成为软件开发人员的时间比以往任何时候都没有。 只要环顾四周，就很可能会看到至少两个不同的设备，例如计算机，智能手机，智能手表或平板电脑，上面运行着一些应用，可以帮助您完成各种日常任务或娱乐音乐，看电影 ，视频游戏等。 每年，市场上都会引入数百种新设备，并且需要新版本的操作系统来跟上它们，以便为应用开发人员提供更好的界面，以创建可更好地利用诸如高分辨率等基础资源的软件。 显示器，各种传感器等。 结果，软件开发框架必须适应并支持不断增长的平台。 考虑到这一点，Qt 可能是同时提供功能，速度，灵活性和易用性的最成功的**跨平台**软件开发框架之一，在创建需要以下功能的软件时，它是首选。 在各种平台上都具有吸引力和一致性。

近年来，特别是随着功能更强大的处理器以较低的价格出现，台式计算机及其手持式对等设备的角色已转向执行更苛刻和更复杂的任务，例如计算机视觉。 无论是用于智能电影或照片编辑，保护敏感建筑物，对生产线中的物体计数，还是通过自动驾驶汽车检测交通标志，车道或行人，计算机视觉正越来越多地用于解决此类实时问题。 曾经只能由人类解决的问题。 这是 OpenCV 框架进入现场的地方。 在过去的几年中，OpenCV 已成长为功能完善的跨平台计算机视觉框架，其重点是速度和性能。 在世界各地，开发人员和研究人员都在使用 OpenCV 来实现其计算机视觉应用的思想和算法。

本书旨在帮助您掌握 Qt 和 OpenCV 框架的基本概念，使您轻松地自己继续开发和交付跨多种平台的计算机视觉应用。 能够轻松遵循本书所涵盖主题的唯一假设是，您熟悉并熟悉 C++ 编程概念，例如类，模板，继承等。 即使整本书中涵盖的教程，屏幕截图和示例都是基于 Windows 操作系统的，但仍会在必要时提及 MacOS 和 Linux 操作系统的区别。



**这本书是给谁的**

本书面向有兴趣构建计算机视觉应用的读者。 期望具备 C++ 编程的中级知识。 即使没有 Qt5 和 OpenCV 3 知识，但如果您熟悉这些框架，您也会受益



**本书涵盖的内容**

- **第1章，OpenCV和Qt简介**
介绍了所有必要的初始化步骤。从在哪里以及如何获取Qt和OpenCV框架开始，本章将描述如何安装、配置，以及确保你的开发环境设置正确。

- **第2章，创建我们的第一个Qt和OpenCV项目**
带领你通过Qt Creator IDE，我们将使用它开发我们所有的应用程序。在本章中，你将学习如何创建和运行你的应用程序项目。

- **第3章，创建一个全面的Qt+OpenCV项目**
通过最常见的功能需求，为一个全面的应用程序，包括样式、国际化、支持各种语言、插件等。通过这个过程，我们将自己创建一个全面的计算机视觉应用程序。

- **第4章，Mat和QImage**
奠定基础并教你编写计算机视觉应用程序所需的基本概念。在这一章中，你将了解所有关于OpenCV Mat类和Qt QImage类，如何在两个框架之间转换和传递它们，以及更多。

- **第5章，图形视图框架**
教你如何使用Qt Graphics View框架及其底层类，以便在应用程序中轻松高效地显示和操作图形。

- **第6章，OpenCV中的图像处理**
带你了解OpenCV框架提供的图像处理功能。你将学习关于变换、过滤器、颜色空间、模板匹配等。

- **第7章，特征和描述符**
全面讲解从图像中检测关键点，从关键点提取描述符，并将它们相互匹配。在本章中，你将学习各种关键点和描述符提取算法，并使用它们来检测和定位图像中的已知对象。

- **第8章，多线程**
教你Qt框架提供的所有关于多线程的能力。你将学习关于互斥锁、读写锁、信号量和各种线程同步工具。这章还会教你关于Qt中低级（QThread）和高级（QtConcurrent）多线程技术。

- **第9章，视频分析**
覆盖了使用Qt和OpenCV框架正确处理视频的方法。你将学习使用MeanShift和CAMShift算法进行对象跟踪等视频处理功能。本章还包括视频处理的所有基本和必要概念的综合概述，如直方图和反向投影图像。

- **第10章，调试和测试**
带你了解Qt Creator IDE的调试功能，以及它是如何配置和设置的。在本章中，你还将学习Qt框架提供的单元测试能力，通过编写示例单元测试，这些测试可以手动或每次项目构建时自动运行。

- **第11章，链接和部署**
教你动态或静态地构建OpenCV和Qt框架。在这一章中，你还将学习在各种平台上部署Qt和OpenCV应用程序。在本章的最后，我们将使用Qt Installer Framework创建一个安装程序。

- **第12章，Qt Quick应用程序**
介绍你Qt Quick应用程序和QML语言。在本章中，你将学习QML语言语法，以及如何与Qt Quick Designer一起使用它来为桌面和移动平台创建漂亮的Qt Quick应用程序。你还将学习在本章中整合QML和C++。



**为了充分利用本书**

尽管书的初章已经涵盖了每一个所需的工具和软件、正确的版本，以及它们是如何被安装和配置的，以下是一个可以作为快速参考的列表：

- 一台安装了最新版本Windows、macOS或Linux（例如Ubuntu）操作系统的常规计算机。
- 微软Visual Studio（在Windows上）
- Xcode（在macOS上）
- CMake
- Qt框架
- OpenCV框架

要了解这些天什么是常规计算机，你可以在线搜索或询问当地商店；然而，你已经拥有的计算机很可能已经足够让你开始了。



**下载示例代码文件**

你可以从你在www.packtpub.com的账户下载本书的示例代码文件。如果你是在别处购买的这本书，你可以访问www.packtpub.com/support并注册，以直接将文件通过电子邮件发送给你。
你可以按照以下步骤下载代码文件：

1. 在www.packtpub.com登录或注册。
2. 选择SUPPORT标签。
3. 点击Code Downloads & Errata。
4. 在搜索框中输入书名并按照屏幕上的指示操作。

一旦文件下载完成，请确保你使用最新版本的以下软件解压或提取文件夹：

- 对于Windows，使用WinRAR/7-Zip
- 对于Mac，使用Zipeg/iZip/UnRarX
- 对于Linux，使用7-Zip/PeaZip

本书的代码包也托管在GitHub上 https://github.com/PacktPublishing/Computer-Vision-with-OpenCV-3-and-Qt5。我们也在https://github.com/PacktPublishing/ 上提供了我们丰富的图书和视频目录中的其他代码包。去看看吧！



**下载彩色图片**

我们还提供了一个PDF文件，其中包含了本书使用的截图/图表的彩色图片。你可以在这里下载它：[https://www.packtpub.com/sites/default/files/downloads/ComputerVisionwithOpenCV3andQt5_ColorImages.pdf](https://www.packtpub.com/sites/default/files/downloads/ComputerVisionwithOpenCV3andQt5_ColorImages.pdf)



**使用的约定**

本书中使用了多种文本约定。

- `CodeInText`：表示文中的代码词汇、数据库表名、文件夹名称、文件名、文件扩展名、路径名、虚构的URL、用户输入和Twitter句柄。这里有一个例子："`QApplication`类是负责控制应用程序的控制流、设置等的主类。"

- 代码块如下所示：
    ```cpp
    #include "mainwindow.h"
    #include <QApplication>
    int main(int argc, char *argv[])
    {
        QApplication a(argc, argv);
        MainWindow w;
        w.show();
        return a.exec();
    }
    ```

- 当我们希望把你的注意力吸引到代码块的特定部分时，相关的行或项将以**加粗**形式展示：
    ```cpp
    #include "mainwindow.h"
    #include <QApplication>
    int main(int argc, char *argv[])
    {
        QApplication a(argc, argv);
        MainWindow w;
        **w.show();**
        return a.exec();
    }
    ```

- 任何命令行输入或输出如下所写：
    ```
    binarycreator -p packages -c config.xml myinstaller
    ```

- **加粗**：表示一个新术语、一个重要词汇或你在屏幕上看到的词汇。例如，菜单或对话框中的词汇在文本中如此显示。这里有一个例子："点击`Next`按钮将你移动到下一个屏幕。"



# 第一章、OpenCV 和 Qt 简介







































