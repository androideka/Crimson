#ifndef STARTGAME_H
#define STARTGAME_H

#include <QWidget>

namespace Ui {
class Widget;
}

class StartGame : public QWidget
{
    Q_OBJECT

public:
    explicit StartGame(QWidget *parent = 0);
    ~StartGame();

private:
    Ui::Widget *ui;
};

#endif // STARTGAME_H
