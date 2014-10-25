#include "startgame.h"
#include "ui_startgame.h"

StartGame::StartGame(QWidget *parent) : QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

StartGame::~StartGame()
{
    delete ui;
}
