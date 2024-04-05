#include "hello_qt_opencv.h"
#include "ui_hello_qt_opencv.h"
#include "opencv2/opencv.hpp"

#include <QFileDialog>
#include <QPushButton>
#include <QMessageBox>
#include <QSettings>


Hello_Qt_OpenCV::Hello_Qt_OpenCV(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Hello_Qt_OpenCV)
{
    ui->setupUi(this);

    loadSettings();  // 加载上次用户退出时的状态

    translator_ru = new QTranslator(this);
    translator_ru->load(":/lanugage/translation_ru.qm");

    translator_zh_CN = new QTranslator(this);
    translator_zh_CN->load(":/lanugage/translation_zh_CN.qm");

    // connect(ui->btnInput, &QPushButton::clicked, this, &Hello_Qt_OpenCV::on_btnInput_clicked);


}

Hello_Qt_OpenCV::~Hello_Qt_OpenCV()
{
    delete ui;
}


void Hello_Qt_OpenCV::on_btnInput_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this, "Open Input Image", QDir::currentPath(), "Images (*.jpg *.png *.bmp)");

    if (QFile::exists(fileName))
    {
        ui->leInput->setText(fileName);
    }
}



void Hello_Qt_OpenCV::on_btnOutput_clicked()
{
    QString fileName = QFileDialog::getSaveFileName(this, "Select output image", QDir::currentPath(), "*.jpg *.png *.bmp");

    if (!fileName.isEmpty())
    {
        ui->leOutput->setText(fileName);
        cv::Mat img_in = cv::imread(ui->leInput->text().toStdString());

        cv::Mat img_out;
        if (ui->rbtnMedianBlur->isChecked())
        {
            cv::medianBlur(img_in, img_out, 5);
        }
        else if (ui->rbtnGaussianBlur->isChecked())
        {
            cv::GaussianBlur(img_in, img_out, cv::Size(5, 5), 1.25);
        }

        cv::imwrite(fileName.toStdString(), img_out);
        if (ui->cbDisplayAfterSave->isChecked())
        {
            cv::imshow("Output image", img_out);
        }
    }
}


void Hello_Qt_OpenCV::closeEvent(QCloseEvent* event)
{
    QMessageBox::StandardButton result =
        QMessageBox::warning(this,
                            tr("Exit"),
                            tr("Are you sure you want to close this program?"),
                            QMessageBox::No | QMessageBox::Yes,
                            QMessageBox::No);

    if (QMessageBox::Yes == result)
    {
        event->accept();
        QWidget::closeEvent(event);  // 向上传递，关闭事件交给父对象处理（直接调用这一句就会导致窗口关闭）
    }
    else
    {
        event->ignore();
    }

    saveSettings();  // 保存用户退出时的状态



}


void Hello_Qt_OpenCV::changeEvent(QEvent *event)
{
    if (event->type() == QEvent::LanguageChange)
    {
        ui->retranslateUi(this);
    }
    else
    {
        QMainWindow::changeEvent(event); // 否则，一切应该像平时一样进行
    }
}


/** 保存用户设置
 * @brief Hello_Qt_OpenCV::saveSettings
 */
void Hello_Qt_OpenCV::saveSettings()
{
    QSettings settings("Packt", "Hello_OpenCV_Qt", this);

    settings.setValue("leInput", ui->leInput->text());
    settings.setValue("Fox/leOutput", ui->leOutput->text());
    settings.setValue("rbtnMedianBlur", ui->rbtnMedianBlur->isChecked());
    settings.setValue("rbtnGaussianBlur", ui->rbtnGaussianBlur->isChecked());
    settings.setValue("cbDisplayAfterSave", ui->cbDisplayAfterSave->isChecked());
}

/** 加载用户设置
 * @brief Hello_Qt_OpenCV::loadSettings
 */
void Hello_Qt_OpenCV::loadSettings()
{
    QSettings settings("Packt", "Hello_OpenCV_Qt", this);
    ui->leInput->setText(settings.value("leInput", "").toString());
    ui->leOutput->setText(settings.value("Fox/leOutput", "").toString());
    ui->rbtnMedianBlur->setChecked(settings.value("rbtnMedianBlur", true).toBool());
    ui->rbtnGaussianBlur->setChecked(settings.value("rbtnGaussianBlur", false).toBool());
    ui->cbDisplayAfterSave->setChecked(settings.value("cbDisplayAfterSave", false).toBool());
}



void Hello_Qt_OpenCV::on_actionChinese_triggered()
{
    qApp->installTranslator(this->translator_zh_CN);
}


void Hello_Qt_OpenCV::on_actionRussia_triggered()
{
    qApp->installTranslator(this->translator_ru);
}


void Hello_Qt_OpenCV::on_actionEnglish_triggered()
{
    qApp->removeTranslator(this->translator_zh_CN);
    qApp->removeTranslator(this->translator_ru);
}

