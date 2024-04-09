#ifndef MEDIANFILTERPLUGIN_H
#define MEDIANFILTERPLUGIN_H

#include "MedianFilterPlugin_global.h"
#include "../CvPluginInterface/CvPluginInterface.h"

class MEDIANFILTERPLUGIN_EXPORT MedianFilterPlugin :
    public QObject, public CvPluginInterface
{
    Q_OBJECT  // 支持信号和槽
    Q_PLUGIN_METADATA(IID "com.amin.cvplugininterface")  // 用于在插件类定义中声明元数据，IID（Interface Identifier 接口标识符）
    Q_INTERFACES(CvPluginInterface)  // 声明插件中实现的接口

public:
    MedianFilterPlugin();
    ~MedianFilterPlugin() override;

    QString description() override;  // 可以增加 override 标识符，表明为重写
    void processImage(const cv::Mat &inputImage, cv::Mat &outputImage) override;
};

#endif // MEDIANFILTERPLUGIN_H
