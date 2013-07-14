#include "lrcfilehandle.h"
#include "ui_lrcfilehandle.h"

LrcFileHandle::LrcFileHandle(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LrcFileHandle)
{
    ui->setupUi(this);
}

LrcFileHandle::~LrcFileHandle()
{
    delete ui;
}
