/********************************************************************************
** Form generated from reading UI file 'lrcfilehandle.ui'
**
** Created by: Qt User Interface Compiler version 5.1.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LRCFILEHANDLE_H
#define UI_LRCFILEHANDLE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LrcFileHandle
{
public:
    QAction *actionTest;
    QAction *actionQcFleHandle;
    QAction *actionRenameAllFile;
    QAction *actionRunNukeBat;
    QAction *actionFileTools;
    QWidget *centralWidget;
    QTabWidget *lrcTab;
    QWidget *tab;
    QFrame *qcFileHandlerFrame;
    QGroupBox *qcFileHandlerGB;
    QPushButton *srcFolderBtn;
    QGroupBox *groupBox;
    QPushButton *scanBtn;
    QPlainTextEdit *srcPathTxt;
    QCheckBox *isGenLogFile;
    QTextEdit *logFileTxt;
    QPushButton *doneBtn;
    QProgressBar *progressBar;
    QGroupBox *ResultGB;
    QTextBrowser *textBrowser;
    QWidget *tab_2;
    QLabel *label;
    QMenuBar *menuBar;
    QMenu *menuMenu1;
    QMenu *menuOper;

    void setupUi(QMainWindow *LrcFileHandle)
    {
        if (LrcFileHandle->objectName().isEmpty())
            LrcFileHandle->setObjectName(QStringLiteral("LrcFileHandle"));
        LrcFileHandle->resize(410, 593);
        actionTest = new QAction(LrcFileHandle);
        actionTest->setObjectName(QStringLiteral("actionTest"));
        actionQcFleHandle = new QAction(LrcFileHandle);
        actionQcFleHandle->setObjectName(QStringLiteral("actionQcFleHandle"));
        actionRenameAllFile = new QAction(LrcFileHandle);
        actionRenameAllFile->setObjectName(QStringLiteral("actionRenameAllFile"));
        actionRunNukeBat = new QAction(LrcFileHandle);
        actionRunNukeBat->setObjectName(QStringLiteral("actionRunNukeBat"));
        actionFileTools = new QAction(LrcFileHandle);
        actionFileTools->setObjectName(QStringLiteral("actionFileTools"));
        centralWidget = new QWidget(LrcFileHandle);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        lrcTab = new QTabWidget(centralWidget);
        lrcTab->setObjectName(QStringLiteral("lrcTab"));
        lrcTab->setGeometry(QRect(20, 10, 371, 531));
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        qcFileHandlerFrame = new QFrame(tab);
        qcFileHandlerFrame->setObjectName(QStringLiteral("qcFileHandlerFrame"));
        qcFileHandlerFrame->setEnabled(true);
        qcFileHandlerFrame->setGeometry(QRect(10, 10, 341, 501));
        qcFileHandlerFrame->setFrameShape(QFrame::StyledPanel);
        qcFileHandlerFrame->setFrameShadow(QFrame::Raised);
        qcFileHandlerGB = new QGroupBox(qcFileHandlerFrame);
        qcFileHandlerGB->setObjectName(QStringLiteral("qcFileHandlerGB"));
        qcFileHandlerGB->setGeometry(QRect(10, 0, 321, 491));
        srcFolderBtn = new QPushButton(qcFileHandlerGB);
        srcFolderBtn->setObjectName(QStringLiteral("srcFolderBtn"));
        srcFolderBtn->setGeometry(QRect(230, 70, 71, 31));
        groupBox = new QGroupBox(qcFileHandlerGB);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 60, 211, 91));
        scanBtn = new QPushButton(qcFileHandlerGB);
        scanBtn->setObjectName(QStringLiteral("scanBtn"));
        scanBtn->setGeometry(QRect(230, 110, 71, 31));
        srcPathTxt = new QPlainTextEdit(qcFileHandlerGB);
        srcPathTxt->setObjectName(QStringLiteral("srcPathTxt"));
        srcPathTxt->setGeometry(QRect(10, 20, 301, 31));
        isGenLogFile = new QCheckBox(qcFileHandlerGB);
        isGenLogFile->setObjectName(QStringLiteral("isGenLogFile"));
        isGenLogFile->setGeometry(QRect(20, 360, 91, 31));
        logFileTxt = new QTextEdit(qcFileHandlerGB);
        logFileTxt->setObjectName(QStringLiteral("logFileTxt"));
        logFileTxt->setGeometry(QRect(120, 360, 181, 31));
        doneBtn = new QPushButton(qcFileHandlerGB);
        doneBtn->setObjectName(QStringLiteral("doneBtn"));
        doneBtn->setGeometry(QRect(20, 410, 121, 61));
        progressBar = new QProgressBar(qcFileHandlerGB);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setGeometry(QRect(160, 460, 151, 23));
        progressBar->setValue(24);
        ResultGB = new QGroupBox(qcFileHandlerGB);
        ResultGB->setObjectName(QStringLiteral("ResultGB"));
        ResultGB->setGeometry(QRect(10, 160, 301, 181));
        textBrowser = new QTextBrowser(ResultGB);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(10, 20, 281, 151));
        lrcTab->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        lrcTab->addTab(tab_2, QString());
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(300, 550, 91, 20));
        LrcFileHandle->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(LrcFileHandle);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 410, 19));
        menuMenu1 = new QMenu(menuBar);
        menuMenu1->setObjectName(QStringLiteral("menuMenu1"));
        menuOper = new QMenu(menuBar);
        menuOper->setObjectName(QStringLiteral("menuOper"));
        LrcFileHandle->setMenuBar(menuBar);

        menuBar->addAction(menuMenu1->menuAction());
        menuBar->addAction(menuOper->menuAction());
        menuMenu1->addSeparator();
        menuMenu1->addAction(actionTest);
        menuOper->addAction(actionFileTools);

        retranslateUi(LrcFileHandle);

        lrcTab->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(LrcFileHandle);
    } // setupUi

    void retranslateUi(QMainWindow *LrcFileHandle)
    {
        LrcFileHandle->setWindowTitle(QApplication::translate("LrcFileHandle", "LrcFileHandle", 0));
        actionTest->setText(QApplication::translate("LrcFileHandle", "Exit", 0));
        actionQcFleHandle->setText(QApplication::translate("LrcFileHandle", "QcFleHandle", 0));
        actionRenameAllFile->setText(QApplication::translate("LrcFileHandle", "RenameAllFile", 0));
        actionRunNukeBat->setText(QApplication::translate("LrcFileHandle", "RunNukeBat", 0));
        actionFileTools->setText(QApplication::translate("LrcFileHandle", "FileTools", 0));
        qcFileHandlerGB->setTitle(QApplication::translate("LrcFileHandle", "QcFleHandler", 0));
        srcFolderBtn->setText(QApplication::translate("LrcFileHandle", "Folder", 0));
        groupBox->setTitle(QApplication::translate("LrcFileHandle", "FileInfo", 0));
        scanBtn->setText(QApplication::translate("LrcFileHandle", "Scan", 0));
        isGenLogFile->setText(QApplication::translate("LrcFileHandle", "isGenLogFile", 0));
        doneBtn->setText(QApplication::translate("LrcFileHandle", "Do", 0));
        ResultGB->setTitle(QApplication::translate("LrcFileHandle", "Result", 0));
        lrcTab->setTabText(lrcTab->indexOf(tab), QApplication::translate("LrcFileHandle", "qcFileHandleTab", 0));
        lrcTab->setTabText(lrcTab->indexOf(tab_2), QApplication::translate("LrcFileHandle", "RenameFiles", 0));
        label->setText(QApplication::translate("LrcFileHandle", "made by Lavenda", 0));
        menuMenu1->setTitle(QApplication::translate("LrcFileHandle", "File", 0));
        menuOper->setTitle(QApplication::translate("LrcFileHandle", "LRC", 0));
    } // retranslateUi

};

namespace Ui {
    class LrcFileHandle: public Ui_LrcFileHandle {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LRCFILEHANDLE_H
