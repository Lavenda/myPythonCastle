#ifndef LRCFILEHANDLE_H
#define LRCFILEHANDLE_H

#include <QMainWindow>

namespace Ui {
class LrcFileHandle;
}

class LrcFileHandle : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit LrcFileHandle(QWidget *parent = 0);
    ~LrcFileHandle();
    
private:
    Ui::LrcFileHandle *ui;
};

#endif // LRCFILEHANDLE_H
