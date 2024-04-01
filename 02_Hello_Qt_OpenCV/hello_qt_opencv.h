#ifndef HELLO_QT_OPENCV_H
#define HELLO_QT_OPENCV_H

#include <QMainWindow>
#include <QCloseEvent>


QT_BEGIN_NAMESPACE
namespace Ui { class Hello_Qt_OpenCV; }
QT_END_NAMESPACE

class Hello_Qt_OpenCV : public QMainWindow
{
    Q_OBJECT

public:
    Hello_Qt_OpenCV(QWidget *parent = nullptr);
    ~Hello_Qt_OpenCV();

protected:
    virtual void closeEvent(QCloseEvent* event);

private:
    void loadSettings();  // 加载上次用户退出时的状态
    void saveSettings();  // 保存用户退出时的状态

private slots:
    void on_btnInput_clicked();
    void on_btnOutput_clicked();

private:
    Ui::Hello_Qt_OpenCV *ui;
};
#endif // HELLO_QT_OPENCV_H
