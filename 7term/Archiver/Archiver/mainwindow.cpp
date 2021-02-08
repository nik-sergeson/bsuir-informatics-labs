#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileSystemModel>
#include <QStandardItemModel>
#include "huffman/huffmanarchiver.h"
#include "archiver/archive.h"
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QStandardItemModel* archive_file_tree=new QStandardItemModel();
    archiver_controller=new ArchiverController(this, archive_file_tree,"/home/nik/labs.7term/Archiver/Archiver/icons/Folder-256.png","/home/nik/labs.7term/Archiver/Archiver/icons/File.png","/home/nik/archiver_test");
    ui->archiveTree->setModel(archive_file_tree);
    connect(ui->openButton, SIGNAL(clicked()), archiver_controller, SLOT(OpenButtonClicked()));
    connect(ui->archiveTree, SIGNAL(clicked(QModelIndex)), archiver_controller, SLOT(ItemSelected(QModelIndex)));
    connect(ui->extractButton, SIGNAL(clicked()), archiver_controller, SLOT(ExtractButtonClicked()));
    connect(ui->addFileButton, SIGNAL(clicked()), archiver_controller, SLOT(AddFileButtonClicked()));
    connect(ui->newButton, SIGNAL(clicked()), archiver_controller, SLOT(NewButtonClicked()));
    connect(ui->addFolderButton, SIGNAL(clicked()), archiver_controller, SLOT(AddFolderClicked()));
    connect(ui->deleteButton, SIGNAL(clicked()), archiver_controller, SLOT(DeleteButtonClicked()));
    connect(ui->extractAllButton, SIGNAL(clicked()), archiver_controller, SLOT(ExtractAllButtonClicked()));
}

MainWindow::~MainWindow()
{
    delete archiver_controller;
    delete ui;
}

