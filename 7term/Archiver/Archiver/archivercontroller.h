#ifndef ARCHIVERCONTROLLER_H
#define ARCHIVERCONTROLLER_H
#include <QObject>
#include <map>
#include <QStandardItemModel>
#include <QFileDialog>
#include <QMessageBox>
#include <QModelIndex>
#include <QVariant>
#include <QDirIterator>
#include <QProgressDialog>
#include "huffman/huffmanarchiver.h"
#include "archiver/archive.h"
#include "concurrenthuffman/huffmanextract.h"
#include "concurrenthuffman/huffmanaddfile.h"
#include "concurrenthuffman/huffmanaddfolder.h"
#include "concurrenthuffman/huffmanremovefile.h"
#include "concurrenthuffman/huffmanremovefolder.h"
using namespace std;

class ArchiverController : public QObject
{
    Q_OBJECT
public:
   ArchiverController(QWidget* parent,QStandardItemModel* archive_file_tree,const QString& folder_icon_path,const QString& file_icon_path, const QString& default_path);
   ~ArchiverController();
public slots:
   void OpenButtonClicked();
   void ExtractButtonClicked();
   void AddFileButtonClicked();
   void NewButtonClicked();
   void AddFolderClicked();
   void DeleteButtonClicked();
   void ExtractAllButtonClicked();
   void ItemSelected(const QModelIndex& index);
private:
   QModelIndex current_item_;
   QStandardItemModel* archive_file_tree_;
   HuffmanArchiver *archiver_;
   QWidget* parent_;
   QString folder_icon_path_, file_icon_path_, default_path_;
};



#endif // ARCHIVERCONTROLLER_H
