#include "huffmanarchiver.h"
#include <iostream>
using namespace std;


HuffmanArchiver::HuffmanArchiver()
{
    opened_archive_=NULL;
    cancelled_=false;
}

HuffmanArchiver::~HuffmanArchiver(){
    Close();
}

Archive* HuffmanArchiver::Open(const string& os_path){
    vector<bit_size_t *> file_size_array;
    if(opened_archive_!=NULL)
        Close();
    archive_bit_file_=new BufferedInFile(os_path);
    for(int ch=0;ch<CHARCOUNT;ch++){
        huffman_leaves_[ch]=new HuffmanNode(ch);
        huffman_codes_[ch]=NULL;
    }
    ReadFrequencyArray(archive_bit_file_, huffman_leaves_);
    file_size_array=ReadFileSizeArray(archive_bit_file_);
    huffman_tree_=BuildTree(huffman_leaves_, CHARCOUNT);
    GenerateCodeList(huffman_codes_, huffman_tree_);
    opened_archive_=ReadArchiveStructure(archive_bit_file_, file_size_array, huffman_tree_, os_path);
    for(vector<bit_size_t *>::iterator f_size=file_size_array.begin();f_size!=file_size_array.end();++f_size)
        delete *f_size;
    return opened_archive_;
}

Archive* HuffmanArchiver::New(const string &os_path){
    if(opened_archive_!=NULL)
        Close();
    BufferedOutFile *out_file=new BufferedOutFile(os_path);
    file_position_t file_size_position;
    vector<ArchiveFile *> archive_contents;
    opened_archive_=new Archive(os_path);
    for(int ch=0;ch<CHARCOUNT;ch++){
        huffman_leaves_[ch]=new HuffmanNode(ch);
        huffman_codes_[ch]=NULL;
    }
    huffman_leaves_[FOLDER_END_CHAR]->IncreaseCount(1);
    WriteFrequencyArray(out_file, huffman_leaves_);
    file_size_position=InitializeFileSizeArray(out_file, opened_archive_->ItemQuantity());
    huffman_tree_=BuildTree(huffman_leaves_, CHARCOUNT);
    GenerateCodeList(huffman_codes_, huffman_tree_);
    WriteFileStructure(huffman_codes_, out_file, opened_archive_->archive_root(), archive_contents);
    out_file->Flush();
    WriteFileSizeArray(out_file, archive_contents, file_size_position);
    delete out_file;
    archive_bit_file_=new BufferedInFile(os_path);
    return opened_archive_;
}

void HuffmanArchiver::Close(){
    if(opened_archive_!=NULL){
        for(int i=0;i<CHARCOUNT;i++){
            if(huffman_codes_[i]!=NULL)
                delete huffman_codes_[i];
        }
        delete huffman_tree_;
        delete archive_bit_file_;
        delete opened_archive_;
        opened_archive_=NULL;
    }
}

bool HuffmanArchiver::ArchiveIsOpened(){
    return opened_archive_!=NULL;
}

void HuffmanArchiver::AddFile(ArchiveFile *file){
    AddFile(opened_archive_->archive_root(), file);
}

void HuffmanArchiver::AddFolder(ArchiveDirectory *dir){
    AddFolder(opened_archive_->archive_root(), dir);
}

void HuffmanArchiver::AddFile(ArchiveDirectory *destination, ArchiveFile *file){
    string tmp_archive_path=opened_archive_->ospath()+".temp";
    BufferedOutFile *out_file=new BufferedOutFile(tmp_archive_path);
    vector<ArchiveFile *> file_stucture;
    deque<pair<file_position_t, bit_size_t> > new_positions;
    HuffmanNode *upd_huffman_leaves[CHARCOUNT], *upd_huffman_tree=NULL;
    HuffmanCode *upd_huffman_codes[CHARCOUNT];
    size_t buffer_size=1000000,read_quantity;
    unsigned char *buffer;
    string os_path=file->ospath(), name=file->name();
    FILE *new_file_file;
    buffer=(unsigned char*)malloc(buffer_size*sizeof(unsigned char));
    file_position_t file_size_position, curr_position;
    cancelled_=false;
    opened_archive_->AddFile(destination, file);
    for(int ch=0;ch<CHARCOUNT;ch++){
        upd_huffman_leaves[ch]=new HuffmanNode(huffman_leaves_[ch]);
        upd_huffman_codes[ch]=NULL;
    }
    new_file_file=fopen(os_path.c_str(), "rb");
    while ((read_quantity=fread(buffer, sizeof(unsigned char), buffer_size, new_file_file)) == buffer_size)
    {
        for(size_t i=0;i<buffer_size;i++){
            upd_huffman_leaves[buffer[i]]->IncreaseCount(1);
        }
        if(cancelled_){
            break;
        }
    }
    if(!cancelled_){
        for(size_t i=0;i<read_quantity;i++)
            upd_huffman_leaves[buffer[i]]->IncreaseCount(1);
    }
    fclose(new_file_file);
    if(cancelled_){
        if(upd_huffman_tree!=NULL)
            delete upd_huffman_tree;
        delete out_file;
        free(buffer);
        for(int i=0;i<CHARCOUNT;i++){
            if(upd_huffman_codes[i])
                delete upd_huffman_codes[i];
        }
        opened_archive_->RemoveFile(destination, file);
        delete file;
        remove(tmp_archive_path.c_str());
        return;
    }
    for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
        unsigned char next_ch=*ch;
        upd_huffman_leaves[next_ch]->IncreaseCount(1);
    }
    upd_huffman_leaves[SEP_CHAR]->IncreaseCount(1);
    WriteFrequencyArray(out_file, upd_huffman_leaves);
    file_size_position=InitializeFileSizeArray(out_file, opened_archive_->ItemQuantity());
    upd_huffman_tree=BuildTree(upd_huffman_leaves, CHARCOUNT);
    GenerateCodeList(upd_huffman_codes, upd_huffman_tree);
    WriteFileStructure(upd_huffman_codes, out_file, opened_archive_->archive_root(), file_stucture);
    for(vector<ArchiveFile *>::iterator file_it=file_stucture.begin(); file_it!=file_stucture.end(); ++file_it){
        if(*file_it!=NULL){
            curr_position=out_file->CurrentPosition();
            if((*file_it)->iswriten())
                MigrateFile(upd_huffman_codes,out_file, archive_bit_file_, *file_it);
            else{
                new_file_file=fopen(os_path.c_str(), "rb");
                while ((read_quantity=fread(buffer, sizeof(unsigned char), buffer_size, new_file_file)) == buffer_size)
                {
                    for(size_t i=0;i<buffer_size;i++)
                        out_file->WriteCode(upd_huffman_codes[buffer[i]]);
                    if(cancelled_)
                        break;
                }
                for(size_t i=0;i<read_quantity;i++)
                    out_file->WriteCode(upd_huffman_codes[buffer[i]]);
                fclose(new_file_file);
                (*file_it)->setwriten();
            }
            if(cancelled_){
                delete upd_huffman_tree;
                delete out_file;
                free(buffer);
                for(int i=0;i<CHARCOUNT;i++){
                    if(upd_huffman_codes[i])
                        delete upd_huffman_codes[i];
                }
                opened_archive_->RemoveFile(destination, file);
                delete file;
                remove(tmp_archive_path.c_str());
                return;
            }
            new_positions.push_back(make_pair(curr_position, Substract(out_file->CurrentPosition(),curr_position)));
        }
    }
    out_file->Flush();
    for(vector<ArchiveFile *>::iterator file_it=file_stucture.begin(); file_it!=file_stucture.end(); ++file_it){
        if(*file_it!=NULL){
            (*file_it)->setposition(new_positions.front().first);
            (*file_it)->setsize(new_positions.front().second);
            new_positions.pop_front();
        }
    }
    WriteFileSizeArray(out_file, file_stucture, file_size_position);
    archive_bit_file_->Close();
    delete huffman_tree_;
    delete out_file;
    free(buffer);
    for(int i=0;i<CHARCOUNT;i++){
        if(huffman_codes_[i])
            delete huffman_codes_[i];
    }
    for(int i=0;i<CHARCOUNT;i++){
        huffman_leaves_[i]=upd_huffman_leaves[i];
        huffman_codes_[i]=upd_huffman_codes[i];
    }
    huffman_tree_=upd_huffman_tree;
    remove(opened_archive_->ospath().c_str());
    rename(tmp_archive_path.c_str(), opened_archive_->ospath().c_str());
    archive_bit_file_->Reopen();
}

void HuffmanArchiver::AddFolder(ArchiveDirectory *destination, ArchiveDirectory *folder){
    string tmp_archive_path=opened_archive_->ospath()+".temp";
    BufferedOutFile *out_file=new BufferedOutFile(tmp_archive_path);
    vector<ArchiveFile *> new_files=folder->AllFiles(), file_structure;
    vector<ArchiveDirectory *> new_folders=folder->AllFolders();
    deque<pair<file_position_t, bit_size_t> > new_positions;
    HuffmanNode *upd_huffman_leaves[CHARCOUNT], *upd_huffman_tree=NULL;
    HuffmanCode *upd_huffman_codes[CHARCOUNT];
    file_position_t file_size_position, curr_position;
    size_t buffer_size=1000000,read_quantity;
    unsigned char *buffer;
    string os_path, name;
    FILE *new_file_file;
    buffer=(unsigned char*)malloc(buffer_size*sizeof(unsigned char));
    cancelled_=false;
    opened_archive_->AddFolder(destination, folder);
    new_folders.push_back(folder);
    for(int ch=0;ch<CHARCOUNT;ch++){
        upd_huffman_leaves[ch]=new HuffmanNode(huffman_leaves_[ch]);
        upd_huffman_codes[ch]=NULL;
    }
    for(vector<ArchiveFile *>::iterator file_it=new_files.begin(); file_it!=new_files.end(); ++file_it){
        name=(*file_it)->name();
        new_file_file=fopen((*file_it)->ospath().c_str(), "rb");
        while ((read_quantity=fread(buffer, sizeof(unsigned char), buffer_size, new_file_file)) == buffer_size)
        {
            for(size_t i=0;i<buffer_size;i++){
                upd_huffman_leaves[buffer[i]]->IncreaseCount(1);
            }
            if(cancelled_)
                break;
        }
        if(!cancelled_){
            for(size_t i=0;i<read_quantity;i++)
                upd_huffman_leaves[buffer[i]]->IncreaseCount(1);
        }
        fclose(new_file_file);
        for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
            unsigned char next_ch=*ch;
            upd_huffman_leaves[next_ch]->IncreaseCount(1);
        }
        if(cancelled_){
            if(upd_huffman_tree!=NULL)
                delete upd_huffman_tree;
            delete out_file;
            for(int i=0;i<CHARCOUNT;i++){
                if(upd_huffman_codes[i])
                    delete upd_huffman_codes[i];
            }
            free(buffer);
            opened_archive_->RemoveFolder(destination, folder);
            delete folder;
            remove(tmp_archive_path.c_str());
            return;
        }
    }
    for(vector<ArchiveDirectory *>::iterator folder_it=new_folders.begin(); folder_it!=new_folders.end(); ++folder_it){
        name=(*folder_it)->name();
        for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
            unsigned char next_ch=*ch;
            upd_huffman_leaves[next_ch]->IncreaseCount(1);
        }
        if(cancelled_)
            break;
    }
    if(cancelled_){
        if(upd_huffman_tree!=NULL)
            delete upd_huffman_tree;
        delete out_file;
        for(int i=0;i<CHARCOUNT;i++){
            if(upd_huffman_codes[i])
                delete upd_huffman_codes[i];
        }
        free(buffer);
        opened_archive_->RemoveFolder(destination, folder);
        delete folder;
        remove(tmp_archive_path.c_str());
        return;
    }
    upd_huffman_leaves[SEP_CHAR]->IncreaseCount(new_files.size()+new_folders.size());
    upd_huffman_leaves[FOLDER_END_CHAR]->IncreaseCount(new_folders.size());
    WriteFrequencyArray(out_file, upd_huffman_leaves);
    file_size_position=InitializeFileSizeArray(out_file, opened_archive_->ItemQuantity());
    upd_huffman_tree=BuildTree(upd_huffman_leaves, CHARCOUNT);
    GenerateCodeList(upd_huffman_codes, upd_huffman_tree);
    WriteFileStructure(upd_huffman_codes, out_file, opened_archive_->archive_root(), file_structure);
    for(vector<ArchiveFile *>::iterator file_it=file_structure.begin(); file_it!=file_structure.end(); ++file_it){
        if(*file_it!=NULL){
            curr_position=out_file->CurrentPosition();
            if((*file_it)->iswriten()){
                MigrateFile(upd_huffman_codes,out_file, archive_bit_file_, *file_it);
            }
            else{
                os_path=(*file_it)->ospath();
                new_file_file=fopen(os_path.c_str(), "rb");
                while ((read_quantity=fread(buffer, sizeof(unsigned char), buffer_size, new_file_file)) == buffer_size)
                {
                    for(size_t i=0;i<buffer_size;i++)
                        out_file->WriteCode(upd_huffman_codes[buffer[i]]);
                    if(cancelled_)
                        break;
                }
                if(!cancelled_){
                    for(size_t i=0;i<read_quantity;i++)
                        out_file->WriteCode(upd_huffman_codes[buffer[i]]);
                }
                fclose(new_file_file);
                (*file_it)->setwriten();
            }
            if(cancelled_){
                delete upd_huffman_tree;
                delete out_file;
                for(int i=0;i<CHARCOUNT;i++){
                    if(upd_huffman_codes[i])
                        delete upd_huffman_codes[i];
                }
                free(buffer);
                opened_archive_->RemoveFolder(destination, folder);
                delete folder;
                remove(tmp_archive_path.c_str());
                return;
            }
            new_positions.push_back(make_pair(curr_position, Substract(out_file->CurrentPosition(),curr_position)));
        }
    }
    out_file->Flush();
    for(vector<ArchiveFile *>::iterator file_it=file_structure.begin(); file_it!=file_structure.end(); ++file_it){
        if(*file_it!=NULL){
            (*file_it)->setposition(new_positions.front().first);
            (*file_it)->setsize(new_positions.front().second);
            new_positions.pop_front();
        }
    }
    WriteFileSizeArray(out_file, file_structure, file_size_position);
    delete huffman_tree_;
    archive_bit_file_->Close();
    delete out_file;
    for(int i=0;i<CHARCOUNT;i++){
        if(huffman_codes_[i])
            delete huffman_codes_[i];
    }
    for(int i=0;i<CHARCOUNT;i++){
        huffman_leaves_[i]=upd_huffman_leaves[i];
        huffman_codes_[i]=upd_huffman_codes[i];
    }
    huffman_tree_=upd_huffman_tree;
    free(buffer);
    remove(opened_archive_->ospath().c_str());
    rename(tmp_archive_path.c_str(), opened_archive_->ospath().c_str());
    archive_bit_file_->Reopen();
}

void HuffmanArchiver::RemoveFile(ArchiveFile *file){
    RemoveFile(opened_archive_->archive_root(), file);
}

void HuffmanArchiver::RemoveFolder(ArchiveDirectory *folder){
    RemoveFolder(opened_archive_->archive_root(), folder);
}

void HuffmanArchiver::RemoveFile(ArchiveDirectory *destination, ArchiveFile *file){
    string tmp_archive_path=opened_archive_->ospath()+".temp";
    int bit, ch;
    BufferedOutFile *out_file=new BufferedOutFile(tmp_archive_path);
    vector<ArchiveFile *> file_sturcture;
    HuffmanNode *upd_huffman_leaves[CHARCOUNT], *upd_huffman_tree=NULL, *current_node;
    HuffmanCode *upd_huffman_codes[CHARCOUNT];
    deque<pair<file_position_t, bit_size_t> > new_positions;
    string name=file->name();
    file_position_t file_size_position, curr_position;
    opened_archive_->RemoveFile(destination, file);
    cancelled_=false;
    for(int ch=0;ch<CHARCOUNT;ch++){
        upd_huffman_leaves[ch]=new HuffmanNode(huffman_leaves_[ch]);
        upd_huffman_codes[ch]=NULL;
    }
    current_node=huffman_tree_;
    archive_bit_file_->ReadBlock(file->size(), file->position());
    for(;;){
        bit=archive_bit_file_->GetBit();
        if(bit==-1)
            break;
        else if(bit != 0)
            current_node=current_node->left();
        else
            current_node=current_node->right();
        if(current_node->value() != COMBINE_NODE){
            ch=current_node->value();
            upd_huffman_leaves[ch]->DecreaseCount(1);
            current_node=huffman_tree_;
            if(cancelled_)
                break;
        }
    }
    for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
        unsigned char next_ch=*ch;
        upd_huffman_leaves[next_ch]->DecreaseCount(1);
    }
    if(cancelled_){
        if(upd_huffman_tree!=NULL)
            delete upd_huffman_tree;
        delete out_file;
        for(int i=0;i<CHARCOUNT;i++){
            if(upd_huffman_codes[i])
                delete upd_huffman_codes[i];
        }
        opened_archive_->AddFile(destination, file);
        remove(tmp_archive_path.c_str());
        return;
    }
    upd_huffman_leaves[SEP_CHAR]->DecreaseCount(1);
    WriteFrequencyArray(out_file, upd_huffman_leaves);
    file_size_position=InitializeFileSizeArray(out_file, opened_archive_->ItemQuantity());
    upd_huffman_tree=BuildTree(upd_huffman_leaves, CHARCOUNT);
    GenerateCodeList(upd_huffman_codes, upd_huffman_tree);
    WriteFileStructure(upd_huffman_codes, out_file, opened_archive_->archive_root(), file_sturcture);
    for(vector<ArchiveFile *>::iterator file_it=file_sturcture.begin(); file_it!=file_sturcture.end(); ++file_it){
        if(*file_it!=0){
            curr_position=out_file->CurrentPosition();
            MigrateFile(upd_huffman_codes,out_file, archive_bit_file_, *file_it);
            if(cancelled_){
                delete upd_huffman_tree;
                delete out_file;
                for(int i=0;i<CHARCOUNT;i++){
                    if(upd_huffman_codes[i])
                        delete upd_huffman_codes[i];
                }
                opened_archive_->AddFile(destination, file);
                remove(tmp_archive_path.c_str());
                return;
            }
            new_positions.push_back(make_pair(curr_position, Substract(out_file->CurrentPosition(),curr_position)));
        }
    }
    out_file->Flush();
    for(vector<ArchiveFile *>::iterator file_it=file_sturcture.begin(); file_it!=file_sturcture.end(); ++file_it){
        if(*file_it!=NULL){
            (*file_it)->setposition(new_positions.front().first);
            (*file_it)->setsize(new_positions.front().second);
            new_positions.pop_front();
        }
    }
    WriteFileSizeArray(out_file, file_sturcture, file_size_position);
    delete huffman_tree_;
    archive_bit_file_->Close();
    delete out_file;
    for(int i=0;i<CHARCOUNT;i++){
        if(huffman_codes_[i])
            delete huffman_codes_[i];
    }
    for(int i=0;i<CHARCOUNT;i++){
        huffman_leaves_[i]=upd_huffman_leaves[i];
        huffman_codes_[i]=upd_huffman_codes[i];
    }
    delete file;
    huffman_tree_=upd_huffman_tree;
    remove(opened_archive_->ospath().c_str());
    rename(tmp_archive_path.c_str(), opened_archive_->ospath().c_str());
    archive_bit_file_->Reopen();
}

void HuffmanArchiver::RemoveFolder(ArchiveDirectory *destination, ArchiveDirectory *folder){
    string tmp_archive_path=opened_archive_->ospath()+".temp", name;
    BufferedOutFile *out_file=new BufferedOutFile(tmp_archive_path);
    vector<ArchiveFile *> files_to_delete=folder->AllFiles(),file_structure;
    vector<ArchiveDirectory *> folders_to_delete=folder->AllFolders();
    deque<pair<file_position_t, bit_size_t> > new_positions;
    HuffmanNode *upd_huffman_leaves[CHARCOUNT], *upd_huffman_tree=NULL, *current_node;
    HuffmanCode *upd_huffman_codes[CHARCOUNT];
    file_position_t file_size_position, curr_position;
    opened_archive_->RemoveFolder(destination, folder);
    cancelled_=false;
    int ch;
    folders_to_delete.push_back(folder);
    for(int ch=0;ch<CHARCOUNT;ch++){
        upd_huffman_leaves[ch]=new HuffmanNode(huffman_leaves_[ch]);
        upd_huffman_codes[ch]=NULL;
    }
    for(vector<ArchiveFile *>::iterator file_it=files_to_delete.begin(); file_it!=files_to_delete.end(); ++file_it){
        name=(*file_it)->name();
        current_node=huffman_tree_;
        archive_bit_file_->ReadBlock((*file_it)->size(), (*file_it)->position());
        for(;;){
            int bit=archive_bit_file_->GetBit();
            if(bit==-1)
                break;
            else if(bit != 0)
                current_node=current_node->left();
            else
                current_node=current_node->right();
            if(current_node->value() != COMBINE_NODE){
                ch=current_node->value();
                upd_huffman_leaves[ch]->DecreaseCount(1);
                current_node=huffman_tree_;
                if(cancelled_)
                    break;
            }
        }
        for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
            unsigned char next_ch=*ch;
            upd_huffman_leaves[next_ch]->DecreaseCount(1);
        }
        if(cancelled_){
            if(upd_huffman_tree!=NULL)
                delete upd_huffman_tree;
            delete out_file;
            for(int i=0;i<CHARCOUNT;i++){
                if(upd_huffman_codes[i])
                    delete upd_huffman_codes[i];
            }
            opened_archive_->AddFolder(destination, folder);
            remove(tmp_archive_path.c_str());
            return;
        }
    }
    for(vector<ArchiveDirectory *>::iterator folder_it=folders_to_delete.begin(); folder_it!=folders_to_delete.end(); ++folder_it){
        name=(*folder_it)->name();
        for(string::iterator ch=name.begin(); ch!=name.end(); ++ch){
            unsigned char next_ch=*ch;
            upd_huffman_leaves[next_ch]->DecreaseCount(1);
        }
    }
    upd_huffman_leaves[SEP_CHAR]->DecreaseCount(files_to_delete.size()+folders_to_delete.size());
    upd_huffman_leaves[FOLDER_END_CHAR]->DecreaseCount(folders_to_delete.size());
    WriteFrequencyArray(out_file, upd_huffman_leaves);
    file_size_position=InitializeFileSizeArray(out_file, opened_archive_->ItemQuantity());
    upd_huffman_tree=BuildTree(upd_huffman_leaves, CHARCOUNT);
    GenerateCodeList(upd_huffman_codes, upd_huffman_tree);
    WriteFileStructure(upd_huffman_codes, out_file, opened_archive_->archive_root(), file_structure);
    for(vector<ArchiveFile *>::iterator file_it=file_structure.begin(); file_it!=file_structure.end(); ++file_it){
        if(*file_it!=NULL){
            curr_position=out_file->CurrentPosition();
            MigrateFile(upd_huffman_codes,out_file, archive_bit_file_, *file_it);
            if(cancelled_){
                delete upd_huffman_tree;
                delete out_file;
                for(int i=0;i<CHARCOUNT;i++){
                    if(upd_huffman_codes[i])
                        delete upd_huffman_codes[i];
                }
                opened_archive_->AddFolder(destination, folder);
                remove(tmp_archive_path.c_str());
                return;
            }
            new_positions.push_back(make_pair(curr_position,Substract(out_file->CurrentPosition(),curr_position)));
        }
    }
    out_file->Flush();
    for(vector<ArchiveFile *>::iterator file_it=file_structure.begin(); file_it!=file_structure.end(); ++file_it){
        if(*file_it!=NULL){
            (*file_it)->setposition(new_positions.front().first);
            (*file_it)->setsize(new_positions.front().second);
            new_positions.pop_front();
        }
    }
    WriteFileSizeArray(out_file, file_structure, file_size_position);
    delete huffman_tree_;
    archive_bit_file_->Close();
    delete out_file;
    for(int i=0;i<CHARCOUNT;i++){
        if(huffman_codes_[i])
            delete huffman_codes_[i];
    }
    for(int i=0;i<CHARCOUNT;i++){
        huffman_leaves_[i]=upd_huffman_leaves[i];
        huffman_codes_[i]=upd_huffman_codes[i];
    }
    huffman_tree_=upd_huffman_tree;
    delete folder;
    remove(opened_archive_->ospath().c_str());
    rename(tmp_archive_path.c_str(), opened_archive_->ospath().c_str());
    archive_bit_file_->Reopen();
}

void HuffmanArchiver::MigrateFile(HuffmanCode *upd_huffman_codes[], BufferedOutFile* dest, BufferedInFile* source, ArchiveFile* file){
    HuffmanNode *current_node;
    int out_char;
    current_node=huffman_tree_;
    source->ReadBlock(file->size(), file->position());
    for(;;){
        int bit=source->GetBit();
        if(bit==-1)
            break;
        else if(bit != 0)
            current_node=current_node->left();
        else
            current_node=current_node->right();
        if(current_node->value() != COMBINE_NODE){
            out_char=current_node->value();
            dest->WriteCode(upd_huffman_codes[out_char]);
            current_node=huffman_tree_;
            if(cancelled_)
                return;
        }
    }    
}

void HuffmanArchiver::ExtractFile(ArchiveFile *file,const string& extract_path){
    HuffmanNode *current_node;
    string file_path=extract_path+"/"+file->name();
    FILE *out_file=fopen(file_path.c_str(), "wb");
    unsigned char ch;
    cancelled_=false;
    int bit;
    if(file->IsSkippedOnExtract()){
        file->SetSkipOnExtract(false);
    }
    else{
        current_node=huffman_tree_;
        archive_bit_file_->ReadBlock(file->size(), file->position());
        for(;;){
            bit=archive_bit_file_->GetBit();
            if(bit==-1)
                break;
            else if(bit != 0)
                current_node=current_node->left();
            else
                current_node=current_node->right();
            if(current_node->value() != COMBINE_NODE){
                ch=current_node->value();
                fwrite(&ch, sizeof(unsigned char), 1, out_file);
                current_node=huffman_tree_;
                if(cancelled_)
                    break;
            }
        }
        fclose(out_file);
        if(cancelled_)
            remove(file_path.c_str());
    }
}

void HuffmanArchiver::ExtractFolder(ArchiveDirectory *folder, const string &extract_path){
    vector<ArchiveFile *> files_to_extract;
    deque<pair<ArchiveFile *, string> > files_queue;
    vector<ArchiveDirectory *> folders_to_extract;
    deque<pair<ArchiveDirectory*, string> >folder_queue;
    ArchiveDirectory *curr_dir;
    ArchiveFile *curr_file;
    cancelled_=false;
    int bit;
    unsigned char ch;
    FILE *out_file;
    HuffmanNode *current_node;
    string curr_path;
    QDir parent_qdir;
    if(folder->parent()==NULL){
        folders_to_extract=folder->folders();
        for(vector<ArchiveDirectory *>::iterator folder_it=folders_to_extract.begin();folder_it!=folders_to_extract.end();++folder_it){
            folder_queue.push_back(make_pair(*folder_it, extract_path));
        }
        files_to_extract=folder->files();
        for(vector<ArchiveFile *>::iterator file_it=files_to_extract.begin(); file_it!=files_to_extract.end();++file_it){
            files_queue.push_back(make_pair(*file_it, extract_path));
        }
    }
    else{
        folder_queue.push_back(make_pair(folder, extract_path));
    }
    while(!folder_queue.empty()){
        curr_dir=folder_queue.front().first;
        curr_path=folder_queue.front().second;
        folder_queue.pop_front();
        parent_qdir=QDir(QString::fromStdString(curr_path));
        parent_qdir.mkdir(QString::fromStdString(curr_dir->name()));
        curr_path+="/"+curr_dir->name();
        folders_to_extract=curr_dir->folders();
        for(vector<ArchiveDirectory *>::iterator dir=folders_to_extract.begin(); dir!=folders_to_extract.end();++dir){
            folder_queue.push_back(make_pair(*dir, curr_path));
        }
        files_to_extract=curr_dir->files();
        for(vector<ArchiveFile *>::iterator file=files_to_extract.begin(); file!=files_to_extract.end(); ++file){
            files_queue.push_back(make_pair(*file, curr_path));
        }
    }
    while(!files_queue.empty()){
        curr_file=files_queue.front().first;
        curr_path=files_queue.front().second+"/"+curr_file->name();
        files_queue.pop_front();
        if(curr_file->IsSkippedOnExtract()){
            curr_file->SetSkipOnExtract(false);
        }
        else{
            out_file=fopen(curr_path.c_str(), "wb");
            current_node=huffman_tree_;
            archive_bit_file_->ReadBlock(curr_file->size(), curr_file->position());
            for(;;){
                bit=archive_bit_file_->GetBit();
                if(bit==-1)
                    break;
                else if(bit != 0)
                    current_node=current_node->left();
                else
                    current_node=current_node->right();
                if(current_node->value() != COMBINE_NODE){
                    ch=current_node->value();
                    fwrite(&ch, sizeof(unsigned char), 1, out_file);
                    current_node=huffman_tree_;
                    if(cancelled_)
                        break;
                }
            }
            fclose(out_file);
            if(cancelled_){
                remove(curr_path.c_str());
                break;
            }
        }
    }
}

HuffmanNode* HuffmanArchiver::BuildTree(HuffmanNode *node_list[], int count){
    int iter=0;
    deque<HuffmanNode *> huffman_queue;
    HuffmanNode *firstmin, *secondmin, *node_list_copy[CHARCOUNT];
    for(int i=0;i<CHARCOUNT; ++i){
        node_list_copy[i]=node_list[i];
    }
    qsort(node_list_copy, count, sizeof(HuffmanNode *), HuffmanNode::CompareNodes);
    while(iter<count && node_list_copy[iter]->count()==0)
        ++iter;
    if(iter>=count)
        return NULL;
    else if(iter==count-1)
        return node_list_copy[iter];
    for(;;){
        if(huffman_queue.size()==1 && iter>=count)
            break;
        if(huffman_queue.empty() || (iter<count && node_list_copy[iter]->count() < huffman_queue.front()->count())){
            firstmin=node_list_copy[iter];
            ++iter;
        }
        else{
            firstmin=huffman_queue.front();
            huffman_queue.pop_front();
        }
        if(huffman_queue.empty() || (iter<count && node_list_copy[iter]->count() < huffman_queue.front()->count())){
            secondmin=node_list_copy[iter];
            ++iter;
        }
        else{
            secondmin=huffman_queue.front();
            huffman_queue.pop_front();
        }
        huffman_queue.push_back(new HuffmanNode(firstmin,secondmin));
    }
    return huffman_queue.front();
}

void HuffmanArchiver::WriteFrequencyArray(BufferedOutFile* out_file, HuffmanNode *freq_arr[]){
    int count=0, arr_length=0, char_arr_length, ext_arr_length, merged_size;
    unsigned char value;
    HuffmanNode* filtered_freq_arr[CHARCOUNT];
    for(int i=0;i<UCHAR_SIZE;++i){
        if(freq_arr[i]->count()==0)
            continue;
        else{
            filtered_freq_arr[arr_length]=freq_arr[i];
            ++arr_length;
        }
    }
    char_arr_length=arr_length;
    for(int i=UCHAR_SIZE;i<CHARCOUNT;++i){
        if(freq_arr[i]->count()==0)
            continue;
        else{
            filtered_freq_arr[arr_length]=freq_arr[i];
            ++arr_length;
        }
    }
    ext_arr_length=arr_length-char_arr_length;
    FILE *fp=out_file->fp();
    merged_size=char_arr_length<<(sizeof(int)*BITS_IN_BYTE/2);
    merged_size|=ext_arr_length;
    fwrite(&merged_size, sizeof(int),1,fp);
    for(int i=0;i<arr_length;++i){
        count=filtered_freq_arr[i]->count();
        value=(unsigned char)filtered_freq_arr[i]->value();
        fwrite(&value, sizeof(unsigned char),1,fp);
        fwrite(&count, sizeof(int),1,fp);
    }
}

void HuffmanArchiver::ReadFrequencyArray(BufferedInFile* in_file, HuffmanNode *freqarr[]){
    int quantity, char_arr_length, ext_arr_length, i_value, merged_size;
    unsigned  char value;
    FILE *fp=in_file->fp();
    if(fread(&merged_size,sizeof(int),1,fp) != 1)
        throw ArchiverException("Archive is corrupted");
    char_arr_length=merged_size>>(sizeof(int)*BITS_IN_BYTE/2);
    ext_arr_length=merged_size & LS16B_MASK;
    if(char_arr_length<0 || ext_arr_length<0){
        throw ArchiverException("Archive is corrupted");
    }
    for(int i=0;i<char_arr_length;++i){
        if(fread(&value,sizeof(unsigned char),1,fp) != 1)
            throw ArchiverException("Archive is corrupted");
        if(fread(&quantity,sizeof(int),1,fp) !=1)
            throw ArchiverException("Archive is corrupted");
        if(quantity<=0)
            throw ArchiverException("Archive is corrupted");
        freqarr[value]->IncreaseCount(quantity);
    }
    for(int i=0;i<ext_arr_length;++i){
        if(fread(&value,sizeof(unsigned char),1,fp) != 1)
            throw ArchiverException("Archive is corrupted");
        if(fread(&quantity,sizeof(int),1,fp) !=1)
            throw ArchiverException("Archive is corrupted");
        i_value=value;
        i_value+=UCHAR_SIZE;
        if(quantity<=0)
            throw ArchiverException("Archive is corrupted");
        freqarr[i_value]->IncreaseCount(quantity);
    }
}

void HuffmanArchiver::GenerateCodeList(HuffmanCode *code_list[], HuffmanNode *huffman_tree){
    HuffmanNode *current_node;
    deque<HuffmanNode *> node_queue;
    deque<HuffmanCode *> code_queue;
    HuffmanCode *current_code=new HuffmanCode(), *right_code;
    node_queue.push_back(huffman_tree);
    code_queue.push_back(current_code);
    while(!node_queue.empty()){
        current_node=node_queue.front();
        node_queue.pop_front();
        current_code=code_queue.front();
        code_queue.pop_front();
        if(current_node->value()!=COMBINE_NODE){
            code_list[current_node->value()]=current_code;
        }
        else{
            right_code=new HuffmanCode(current_code);
            node_queue.push_back(current_node->left());
            current_code->AddBit(1);
            code_queue.push_back(current_code);
            node_queue.push_back(current_node->right());
            right_code->AddBit(0);
            code_queue.push_back(right_code);
        }
    }
}

file_position_t HuffmanArchiver::InitializeFileSizeArray(BufferedOutFile* out_file,int size){
    FILE *fp=out_file->fp();
    bit_size_t default_size;
    file_position_t position;
    fwrite(&size, sizeof(int),1,fp);
    position.byte_position=ftell(fp);
    position.bit_position=0;
    for(int i=0;i<size;++i){
        fwrite(&default_size.tail_size_bit, sizeof(char),1,fp);
        fwrite(&default_size.size_byte, sizeof(long int),1,fp);
    }
    return position;
}

void HuffmanArchiver::WriteFileStructure(HuffmanCode* huffman_codes[], BufferedOutFile* out_file,ArchiveDirectory* archive_structure, vector<ArchiveFile *>& file_strucutre){
    vector<ArchiveItem *> archive_contents;
    vector<ArchiveDirectory *> sub_folders;
    deque<ArchiveDirectory *> folder_queue, folder_stack;
    ArchiveDirectory *current_folder;
    string current_name;
    folder_stack.push_back(archive_structure);
    folder_queue.push_back(NULL);
    sub_folders=archive_structure->folders();
    reverse(sub_folders.begin(), sub_folders.end());
    for(vector<ArchiveDirectory *>::iterator folder=sub_folders.begin();folder!=sub_folders.end();++folder){
        folder_queue.push_front(NULL);
        folder_queue.push_front(*folder);
    }
    while(!folder_queue.empty()){
        current_folder=folder_queue.front();
        folder_queue.pop_front();
        if(current_folder==NULL){
            current_folder=folder_stack.back();
            folder_stack.pop_back();
            archive_contents.insert(archive_contents.end(), current_folder->files().begin(), current_folder->files().end());
            archive_contents.push_back(NULL);
            file_strucutre.insert(file_strucutre.end(), current_folder->files().begin(), current_folder->files().end());
        }
        else{
            archive_contents.push_back(current_folder);
            file_strucutre.push_back(NULL);
            folder_stack.push_back(current_folder);
            sub_folders=current_folder->folders();
            reverse(sub_folders.begin(), sub_folders.end());
            for(vector<ArchiveDirectory *>::iterator folder=sub_folders.begin();folder!=sub_folders.end();++folder){
                folder_queue.push_front(NULL);
                folder_queue.push_front(*folder);
            }
        }
    }
    for(vector<ArchiveItem *>::iterator item=archive_contents.begin();item!=archive_contents.end(); ++item)
    {
        if((*item)==NULL){
            out_file->WriteCode(huffman_codes[FOLDER_END_CHAR]);
        }
        else{
            current_name=(*item)->name();
            for(string::iterator ch=current_name.begin(); ch!=current_name.end(); ++ch){
                unsigned char uch=*ch;
                out_file->WriteCode(huffman_codes[uch]);
            }
            out_file->WriteCode(huffman_codes[SEP_CHAR]);
        }
    }
}

void HuffmanArchiver::WriteFileSizeArray(BufferedOutFile* out_file, vector<ArchiveFile*>& archive_content, const file_position_t& position){
    char dir_bit_size=DIR_SIZE;
    long int dir_byte_size=DIR_SIZE;
    FILE *fp=out_file->fp();
    fseek(fp, position.byte_position, SEEK_SET);
    for(vector<ArchiveFile *>::iterator file_it=archive_content.begin();file_it!=archive_content.end(); ++file_it){
        if((*file_it)!=NULL){
            bit_size_t size=(*file_it)->size();
            fwrite(&size.tail_size_bit, sizeof(char),1,fp);
            fwrite(&size.size_byte, sizeof(long int),1,fp);
        }
        else{
            fwrite(&dir_bit_size, sizeof(char),1,fp);
            fwrite(&dir_byte_size, sizeof(long int),1,fp);
        }
    }
}

vector<bit_size_t *> HuffmanArchiver::ReadFileSizeArray(BufferedInFile* in_file){
    FILE *fp=in_file->fp();
    vector<bit_size_t *> archive_content_size;
    bit_size_t *temp_size;
    int size_quantity;
    if(fread(&size_quantity,sizeof(int),1,fp) !=1)
        throw ArchiverException("Archive is corrupted");
    for(int i=0;i<size_quantity;++i){
        temp_size=CreateBitSize();
        if(fread(&temp_size->tail_size_bit,sizeof(char),1,fp) !=1)
            throw ArchiverException("Archive is corrupted");
        if(fread(&temp_size->size_byte,sizeof(long int),1,fp) !=1)
            throw ArchiverException("Archive is corrupted");
        if(temp_size->tail_size_bit<DIR_SIZE || temp_size->tail_size_bit>=BYTE_SIZE_BITS)
            throw ArchiverException("Archive is corrupted file size");
        if(temp_size->size_byte<DIR_SIZE)
            throw ArchiverException("Archive is corrupted");
        archive_content_size.push_back(temp_size);
    }
    return archive_content_size;
}

Archive* HuffmanArchiver::ReadArchiveStructure(BufferedInFile* in_file, vector<bit_size_t *>& file_size_array,HuffmanNode* huffman_tree, const string& os_path){
    deque<ArchiveDirectory *> folder_stack;
    Archive* archive=new Archive(os_path);
    vector<ArchiveFile *> files;
    HuffmanNode *current_node=huffman_tree;
    string current_name;
    int bit;
    int file_size_iter=0, current_char;
    file_position_t file_position;
    folder_stack.push_back(archive->archive_root());
    current_node=huffman_tree;
    in_file->ReadBlock();
    while(!folder_stack.empty()){
        bit=in_file->GetBit();
        if(bit==-1){
            in_file->ReadBlock();
            if(in_file->size().size_byte==0)
                throw ArchiverException("Archive is corrupted");
        }
        if(bit != 0)
            current_node=current_node->left();
        else
            current_node=current_node->right();
        if(current_node->value() != COMBINE_NODE){
            if(current_node->value() == SEP_CHAR){
                if(file_size_array[file_size_iter]->tail_size_bit==DIR_SIZE && file_size_array[file_size_iter]->size_byte==DIR_SIZE){
                    ArchiveDirectory *dir=new ArchiveDirectory(current_name);
                    dir->setsize(*file_size_array[file_size_iter]);
                    dir->setwriten();
                    archive->AddFolder(folder_stack.back(), dir);
                    folder_stack.push_back(dir);
                }
                else{
                    ArchiveFile *file=new ArchiveFile(current_name);
                    file->setsize(*file_size_array[file_size_iter]);
                    file->setwriten();
                    archive->AddFile(folder_stack.back(), file);
                    files.push_back(file);
                }
                current_name=string();
                ++file_size_iter;
            }
            else if(current_node->value()==FOLDER_END_CHAR){
                folder_stack.pop_back();
            }
            else{
                current_char=current_node->value();
                current_name+=current_char;
            }
            current_node=huffman_tree;
        }
    }
    if(file_size_iter<file_size_array.size()){
        throw ArchiverException("Archive is corrupted");
    }
    file_position=in_file->CurrentPosition();
    for(vector<ArchiveFile *>::iterator file=files.begin(); file!=files.end(); ++file){
        (*file)->setposition(file_position);
        file_position=Add(file_position, (*file)->size());
    }
    return archive;
}

Archive* HuffmanArchiver::openedarchive() const{
    return opened_archive_;
}


void HuffmanArchiver::Cancell(){
    cancelled_=true;
}

bool HuffmanArchiver::IsCancelled() const{
    return cancelled_;
}
