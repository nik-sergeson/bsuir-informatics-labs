#include "archivercontroller.h"

ArchiverController::ArchiverController(QWidget* parent,QStandardItemModel* archive_file_tree,const QString& folder_icon_path,const QString& file_icon_path, const QString& default_path)
{
    archiver_=new HuffmanArchiver();
    parent_=parent;
    archive_file_tree_=archive_file_tree;
    folder_icon_path_=folder_icon_path;
    file_icon_path_=file_icon_path;
    default_path_=default_path;
}

void ArchiverController::OpenButtonClicked(){
    deque<pair<ArchiveDirectory *, QStandardItem*> > folder_queue;
    vector<ArchiveFile *> sub_files;
    vector<ArchiveDirectory *> sub_folders;
    ArchiveDirectory *curr_folder;
    QStandardItem *curr_item, *folder_item, *file_item;
    QVariant variant;
    Archive *archive;
    QString sel_filter=tr("Archive Files (*.nar)");
    QString fileName = QFileDialog::getOpenFileName(parent_, tr("Open File"), default_path_, tr("Archive Files (*.nar)"),&sel_filter, QFileDialog::DontUseNativeDialog);
    if(!fileName.isEmpty()){
        try{
            archive=archiver_->Open(fileName.toStdString());
        }
        catch(ArchiverException &exc){
            QMessageBox::information(parent_, "Error", exc.what(), QMessageBox::Ok);
            fileName="";
        }
    }
    if(!fileName.isEmpty()){
        archive_file_tree_->clear();
        curr_folder=archive->archive_root();
        folder_queue.push_back(make_pair(curr_folder, archive_file_tree_->invisibleRootItem()));
        while(!folder_queue.empty()){
            curr_folder=folder_queue.front().first;
            curr_item=folder_queue.front().second;
            folder_queue.pop_front();
            sub_folders=curr_folder->folders();
            for(vector<ArchiveDirectory *>::iterator folder=sub_folders.begin(); folder!=sub_folders.end(); ++folder){
                folder_item = new QStandardItem(QIcon(folder_icon_path_),QString::fromStdString((*folder)->name()));
                folder_item->setEditable(false);
                curr_item->appendRow(folder_item);
                variant=QVariant::fromValue(*folder);
                folder_item->setData(variant);
                folder_queue.push_back(make_pair(*folder, folder_item));
            }
            sub_files=curr_folder->files();
            for(vector<ArchiveFile *>::iterator file=sub_files.begin(); file!=sub_files.end(); ++file){
                file_item = new QStandardItem(QIcon(file_icon_path_),QString::fromStdString((*file)->name()));
                file_item->setEditable(false);
                curr_item->appendRow(file_item);
                variant=QVariant::fromValue(*file);
                file_item->setData(variant);
            }
        }
        current_item_=QModelIndex();
    }
}

void ArchiverController::ItemSelected(const QModelIndex &index){
    current_item_=index;
}

void ArchiverController::ExtractButtonClicked(){
    QStandardItem *item=archive_file_tree_->itemFromIndex(current_item_);
    QString dir_path;
    QVariant variant;
    deque<pair<ArchiveDirectory *, QString> > folder_queue;
    deque<pair<ArchiveFile *, QString> >file_queue;
    vector<ArchiveDirectory *> subfolders;
    vector<ArchiveFile *> subfiles;
    QString curr_path;
    ArchiveDirectory *curr_dir;
    ArchiveFile *curr_file;
    HuffmanExtract *huffman_thread;
    if(item!=NULL){
        dir_path = QFileDialog::getExistingDirectory(parent_, tr("Extract to"), default_path_, QFileDialog::ShowDirsOnly | QFileDialog::DontResolveSymlinks| QFileDialog::DontUseNativeDialog);
        variant=item->data();
        if(!dir_path.isEmpty()){
            if(variant.canConvert<ArchiveDirectory *>()){
                ArchiveDirectory *folder=variant.value<ArchiveDirectory *>();
                folder_queue.push_back(make_pair(folder, dir_path));
                while(!folder_queue.empty()){
                    curr_dir=folder_queue.front().first;
                    curr_path=folder_queue.front().second+"/"+QString::fromStdString(curr_dir->name());
                    folder_queue.pop_front();
                    QDir curr_qdir(curr_path);
                    if(curr_qdir.exists()){
                        subfiles=curr_dir->files();
                        subfolders=curr_dir->folders();
                        for(vector<ArchiveDirectory *>::iterator dir=subfolders.begin(); dir!=subfolders.end(); ++dir)
                            folder_queue.push_back(make_pair(*dir, curr_path));
                        for(vector<ArchiveFile *>::iterator file=subfiles.begin(); file!=subfiles.end(); ++file){
                            file_queue.push_back(make_pair(*file, curr_path));
                        }
                    }
                }
                while(!file_queue.empty()){
                    curr_file=file_queue.front().first;
                    curr_path=file_queue.front().second+"/"+QString::fromStdString(curr_file->name());
                    file_queue.pop_front();
                    QFileInfo file_info(curr_path);
                    if(file_info.exists()){
                        int reply;
                        QMessageBox msgBox(parent_);
                        msgBox.setText(QString::fromStdString(curr_file->name())+" exists.");
                        msgBox.setInformativeText("Overwrite?");
                        msgBox.setStandardButtons(QMessageBox::Yes|QMessageBox::No|QMessageBox::YesAll|QMessageBox::NoToAll);
                        reply = msgBox.exec();
                          if (reply == QMessageBox::No) {
                              curr_file->SetSkipOnExtract(true);
                          }
                          else if(reply==QMessageBox::YesToAll){
                              file_queue.clear();
                          }
                          else if(reply==QMessageBox::NoToAll){
                              curr_file->SetSkipOnExtract(true);
                              while(!file_queue.empty()){
                                  curr_file=file_queue.front().first;
                                  curr_path=file_queue.front().second+"/"+QString::fromStdString(curr_file->name());
                                  file_queue.pop_front();
                                  QFileInfo file_info(curr_path);
                                  if(file_info.exists()){
                                      curr_file->SetSkipOnExtract(true);
                                  }
                            }
                         }

                    }
                }
                QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
                progress_dialog.setWindowModality(Qt::WindowModal);
                disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
                huffman_thread=new HuffmanExtract(archiver_,folder,dir_path.toStdString());
                connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
                connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
                huffman_thread->start();
                progress_dialog.exec();
                huffman_thread->wait();
                delete huffman_thread;
            }
            else{
                ArchiveFile *file=variant.value<ArchiveFile *>();
                QFileInfo file_info(dir_path+"/"+QString::fromStdString(file->name()));
                bool extract=true;
                if(file_info.exists()){
                    int reply;
                    QMessageBox msgBox(parent_);
                    msgBox.setText(QString::fromStdString(file->name())+" exists.");
                    msgBox.setInformativeText("Overwrite?");
                    msgBox.setStandardButtons(QMessageBox::Yes|QMessageBox::No);
                    reply = msgBox.exec();
                      if (reply == QMessageBox::No) {
                          extract=false;
                      }
                }
                if(extract){
                    QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
                    progress_dialog.setWindowModality(Qt::WindowModal);
                    disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
                    huffman_thread=new HuffmanExtract(archiver_, file, dir_path.toStdString());
                    connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
                    connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
                    huffman_thread->start();
                    progress_dialog.exec();
                    huffman_thread->wait();
                    delete huffman_thread;
                }
            }
        }
    }
}

void ArchiverController::ExtractAllButtonClicked(){
    QString dir_path;
    HuffmanExtract *huffman_thread;
    deque<pair<ArchiveDirectory *, QString> > folder_queue;
    deque<pair<ArchiveFile *, QString> >file_queue;
    vector<ArchiveDirectory *> subfolders;
    vector<ArchiveFile *> subfiles;
    QString curr_path;
    ArchiveDirectory *curr_dir;
    ArchiveFile *curr_file;
    dir_path = QFileDialog::getExistingDirectory(parent_, tr("Extract to"), default_path_, QFileDialog::ShowDirsOnly | QFileDialog::DontResolveSymlinks| QFileDialog::DontUseNativeDialog);
    if(!dir_path.isEmpty()){
        ArchiveDirectory *folder=archiver_->openedarchive()->archive_root();
        subfolders=folder->folders();
        subfiles=folder->files();
        for(vector<ArchiveDirectory *>::iterator dir=subfolders.begin(); dir!=subfolders.end();++dir)
            folder_queue.push_back(make_pair(*dir, dir_path));
        for(vector<ArchiveFile *>::iterator file=subfiles.begin(); file!=subfiles.end(); ++file)
            file_queue.push_back(make_pair(*file, dir_path));
        while(!folder_queue.empty()){
            curr_dir=folder_queue.front().first;
            curr_path=folder_queue.front().second+"/"+QString::fromStdString(curr_dir->name());
            folder_queue.pop_front();
            QDir curr_qdir(curr_path);
            if(curr_qdir.exists()){
                subfolders=curr_dir->folders();
                subfiles=curr_dir->files();
                for(vector<ArchiveDirectory *>::iterator dir=subfolders.begin(); dir!=subfolders.end(); ++dir)
                    folder_queue.push_back(make_pair(*dir, curr_path));
                for(vector<ArchiveFile *>::iterator file=subfiles.begin(); file!=subfiles.end(); ++file){
                    file_queue.push_back(make_pair(*file, curr_path));
                }
            }
        }
        while(!file_queue.empty()){
            curr_file=file_queue.front().first;
            curr_path=file_queue.front().second+"/"+QString::fromStdString(curr_file->name());
            file_queue.pop_front();
            QFileInfo file_info(curr_path);
            if(file_info.exists()){
                int reply;
                QMessageBox msgBox(parent_);
                msgBox.setText(QString::fromStdString(curr_file->name())+" exists.");
                msgBox.setInformativeText("Overwrite?");
                msgBox.setStandardButtons(QMessageBox::Yes|QMessageBox::No|QMessageBox::YesAll|QMessageBox::NoToAll);
                reply = msgBox.exec();
                if (reply == QMessageBox::No) {
                    curr_file->SetSkipOnExtract(true);
                }
                else if(reply==QMessageBox::YesToAll){
                    file_queue.clear();
                }
                else if(reply==QMessageBox::NoToAll){
                    while(!file_queue.empty()){
                        curr_file=file_queue.front().first;
                        curr_path=file_queue.front().second+"/"+QString::fromStdString(curr_file->name());
                        file_queue.pop_front();
                        QFileInfo file_info(curr_path);
                        if(file_info.exists()){
                            curr_file->SetSkipOnExtract(true);
                        }
                    }
                }

            }
        }
        QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
        progress_dialog.setWindowModality(Qt::WindowModal);
        disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
        huffman_thread=new HuffmanExtract(archiver_,folder,dir_path.toStdString());
        connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
        connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
        huffman_thread->start();
        progress_dialog.exec();
        huffman_thread->wait();
        delete huffman_thread;
    }
}

void ArchiverController::AddFileButtonClicked(){
    ArchiveDirectory *dest;
    QVariant variant;
    QString fileName;
    QStandardItem *item=archive_file_tree_->itemFromIndex(current_item_); 
    QString sel_filter=tr("All Files (*.*)");
    HuffmanAddFile *huffman_thread;
    if(archiver_->ArchiveIsOpened()){
        fileName = QFileDialog::getOpenFileName(parent_, tr("Add File"), default_path_, tr("All Files (*.*)"),&sel_filter, QFileDialog::DontUseNativeDialog);
        if(!fileName.isEmpty()){
            QFileInfo file_info(fileName);
            if(item!=NULL){
                variant=item->data();
                if(variant.canConvert<ArchiveFile *>())
                    item=item->parent();
            }
            if(item==NULL){
                item=archive_file_tree_->invisibleRootItem();
                dest=archiver_->openedarchive()->archive_root();
            }
            else{
                variant=item->data();
                dest=variant.value<ArchiveDirectory *>();
            }
            QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
            progress_dialog.setWindowModality(Qt::WindowModal);
            disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
            if(!dest->HasFileName(file_info.fileName().toStdString())){
                ArchiveFile* file=new ArchiveFile(fileName.toStdString(), file_info.fileName().toStdString());
                QStandardItem* file_item = new QStandardItem(QIcon(file_icon_path_),file_info.fileName());
                file_item->setEditable(false);
                huffman_thread=new HuffmanAddFile(archiver_, dest, file);
                connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
                connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
                huffman_thread->start();
                progress_dialog.exec();
                huffman_thread->wait();
                delete huffman_thread;
                if(!archiver_->IsCancelled()){
                    item->appendRow(file_item);
                    variant=QVariant::fromValue(file);
                    file_item->setData(variant);
                }
                else{
                    delete file_item;
                }
            }
            else{
                QMessageBox::information(parent_, "File exists", "File exists in current folder", QMessageBox::Ok);
            }
            current_item_=QModelIndex();
        }
    }
}

void ArchiverController::NewButtonClicked(){
    QString filename;
    QString sel_filter=tr("Archive Files (*.nar)");
    while(true){
        filename = QFileDialog::getSaveFileName(parent_, tr("New Archive"),default_path_, tr("Archive Files (*.nar)"),&sel_filter, QFileDialog::DontUseNativeDialog);
        if(filename.isEmpty())
            break;
        filename+=".nar";
        QFileInfo file_info(filename);
        if(file_info.exists()){
            QMessageBox::StandardButton reply;
            reply = QMessageBox::question(parent_, "File exists", "File exists. Overwrite?", QMessageBox::Yes|QMessageBox::No);
              if (reply == QMessageBox::Yes) {
                  break;
              }
        }
        else
            break;
    }
    if(!filename.isEmpty()){
        archive_file_tree_->clear();
        archiver_->New(filename.toStdString());
        current_item_=QModelIndex();
    }
}

void ArchiverController::AddFolderClicked(){
    deque<QDir> qdir_queue;
    deque<pair<ArchiveDirectory *, QStandardItem *> > folder_queue;
    QVariant variant;
    QString curr_absolute_path;
    QDir curr_qdir;
    QStringList sub_folders;
    ArchiveDirectory *parent, *root_folder;
    HuffmanAddFolder *huffman_thread;
    deque<QFileInfo> files;
    if(archiver_->ArchiveIsOpened()){
        QStandardItem *item=archive_file_tree_->itemFromIndex(current_item_);
        if(item!=NULL){
            variant=item->data();
            if(variant.canConvert<ArchiveFile *>())
                item=item->parent();
        }
        if(item!=NULL){
            variant=item->data();
            parent=variant.value<ArchiveDirectory *>();
        }
        else{
            item=archive_file_tree_->invisibleRootItem();
            parent=archiver_->openedarchive()->archive_root();
        }
        QString dir_path = QFileDialog::getExistingDirectory(parent_, tr("Add folder"), default_path_, QFileDialog::ShowDirsOnly | QFileDialog::DontResolveSymlinks| QFileDialog::DontUseNativeDialog);
        if(!dir_path.isEmpty()){
            QDir root_qdir(dir_path);
            QStandardItem* root_folder_item;
            int row=0;
            if(!parent->HasFolderName(root_qdir.dirName().toStdString())){
                root_folder=new ArchiveDirectory(root_qdir.dirName().toStdString());
                root_folder_item=new QStandardItem(QIcon(folder_icon_path_),root_qdir.dirName());
                root_folder_item->setEditable(false);
                variant=QVariant::fromValue(root_folder);
                root_folder_item->setData(variant);
                QStandardItem *child=item->child(0);
                while(child!=NULL && child->hasChildren()){
                    ++row;
                    child=item->child(row);
                }
                qdir_queue.push_back(root_qdir);
                folder_queue.push_back(make_pair(root_folder, root_folder_item));
                while(!qdir_queue.empty()){
                    curr_qdir=qdir_queue.front();
                    qdir_queue.pop_front();
                    ArchiveDirectory *curr_folder=folder_queue.front().first;
                    QStandardItem* curr_folder_item=folder_queue.front().second;
                    folder_queue.pop_front();
                    sub_folders=curr_qdir.entryList(QDir::NoDotAndDotDot | QDir::Dirs | QDir::Files);
                    for(int i=0;i<sub_folders.size();i++){
                        curr_absolute_path=curr_qdir.absolutePath()+"/"+sub_folders.at(i);
                        QFileInfo curr_file_info(curr_absolute_path);
                        if(curr_file_info.isFile()){
                            files.push_back(curr_file_info);
                        }
                        else{
                            QDir qdir_it=QDir(curr_absolute_path);
                            ArchiveDirectory *dir=new ArchiveDirectory(qdir_it.dirName().toStdString());
                            curr_folder->AddFolder(dir);
                            QStandardItem* dir_item=new QStandardItem(QIcon(folder_icon_path_), qdir_it.dirName());
                            dir_item->setEditable(false);
                            curr_folder_item->appendRow(dir_item);
                            variant=QVariant::fromValue(dir);
                            dir_item->setData(variant);
                            qdir_queue.push_back(qdir_it);
                            folder_queue.push_back(make_pair(dir, dir_item));
                        }
                    }
                    while(!files.empty()){
                        QFileInfo curr_file_info=files.front();
                        files.pop_front();
                        ArchiveFile *file=new ArchiveFile(curr_file_info.absoluteFilePath().toStdString(), curr_file_info.fileName().toStdString());
                        curr_folder->AddFile(file);
                        QStandardItem* file_item=new QStandardItem(QIcon(file_icon_path_), curr_file_info.fileName());
                        file_item->setEditable(false);
                        variant=QVariant::fromValue(file);
                        file_item->setData(variant);
                        curr_folder_item->appendRow(file_item);
                    }
                }
                QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
                progress_dialog.setWindowModality(Qt::WindowModal);
                disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
                huffman_thread=new HuffmanAddFolder(archiver_, parent, root_folder);
                connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
                connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
                huffman_thread->start();
                progress_dialog.exec();
                huffman_thread->wait();
                if(!archiver_->IsCancelled())
                    item->insertRow(row, root_folder_item);
                else
                    delete root_folder_item;
                delete huffman_thread;
                current_item_=QModelIndex();
            }
            else{
                QMessageBox::information(parent_, "Folder exists", "Folder exists in current folder", QMessageBox::Ok);
            }
        }
    }
}

void ArchiverController::DeleteButtonClicked(){
    QStandardItem *item=archive_file_tree_->itemFromIndex(current_item_), *parent_item;
    ArchiveDirectory *parent_dir;
    QVariant variant, parent_variant;
    if(item!=NULL){
        variant=item->data();
        parent_item=item->parent();
        if(parent_item==NULL){
            parent_item=archive_file_tree_->invisibleRootItem();
            parent_dir=archiver_->openedarchive()->archive_root();
        }
        else{
            parent_variant=parent_item->data();
            parent_dir=parent_variant.value<ArchiveDirectory *>();
        }
        QProgressDialog progress_dialog("Task in progress...", "Cancel", 0, 0, parent_);
        progress_dialog.setWindowModality(Qt::WindowModal);
        disconnect(&progress_dialog, SIGNAL(canceled()), &progress_dialog, SLOT(cancel()));
        if(variant.canConvert<ArchiveDirectory *>()){
            ArchiveDirectory *folder=variant.value<ArchiveDirectory *>();
            HuffmanRemoveFolder *huffman_thread = new HuffmanRemoveFolder(archiver_, parent_dir, folder);
            connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
            connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
            huffman_thread->start();
            progress_dialog.exec();
            huffman_thread->wait();
            delete huffman_thread;
        }
        else{
            ArchiveFile *file=variant.value<ArchiveFile *>();
            HuffmanRemoveFile *huffman_thread=new HuffmanRemoveFile(archiver_, parent_dir, file);
            connect(&progress_dialog, SIGNAL(canceled()), huffman_thread, SLOT(Cancell()));
            connect(huffman_thread, SIGNAL(Finished()), &progress_dialog, SLOT(cancel()));
            huffman_thread->start();
            progress_dialog.exec();
            huffman_thread->wait();
            delete huffman_thread;
        }
        if(!archiver_->IsCancelled())
            parent_item->removeRow(item->row());
        current_item_=QModelIndex();
    }
}

ArchiverController::~ArchiverController(){
    delete archiver_;
    delete archive_file_tree_;
}
