#ifndef HUFFMANARCHIVER_H
#define HUFFMANARCHIVER_H
#include <deque>
#include <QDir>
#include <QProgressDialog>
#include <algorithm>
#include <QCoreApplication>
#include <atomic>
#include "huffmancode.h"
#include "../bufferedfile/bufferedinfile.h"
#include "../bufferedfile/bufferedoutfile.h"
#include "../archiver/archiver.h"
#include "../fileutils/fileposition.h"
#include "archiver/archivefile.h"
#include "archiverexception.h"
#include "huffmannode.h"
using namespace std;

#define CHARCOUNT 258
#define UCHAR_SIZE 256
#define SEP_CHAR 257
#define FOLDER_END_CHAR 256
#define BITS_IN_BYTE 8
#define LS16B_MASK 0xFFFF


class HuffmanArchiver:public Archiver
{
public:
    HuffmanArchiver();
    Archive* Open(const string& os_path);
    void Close();
    Archive* New(const string& os_path);
    void AddFile(ArchiveFile* file);
    void AddFolder(ArchiveDirectory *dir);
    void AddFile(ArchiveDirectory* destination, ArchiveFile* file);
    void AddFolder(ArchiveDirectory* destination, ArchiveDirectory* folder);
    void RemoveFile(ArchiveDirectory* destination, ArchiveFile* file);
    void RemoveFolder(ArchiveDirectory* destination, ArchiveDirectory* folder);
    void RemoveFile(ArchiveFile* file);
    void RemoveFolder(ArchiveDirectory* folder);
    void ExtractFile(ArchiveFile* file, const string& extract_path);
    void ExtractFolder(ArchiveDirectory* folder, const string& extract_path);
    bool ArchiveIsOpened();
    Archive* openedarchive() const;
    void Cancell();
    bool IsCancelled() const;
    ~HuffmanArchiver();
private:
    file_position_t InitializeFileSizeArray(BufferedOutFile* out_file, int size);
    void WriteFileStructure(HuffmanCode* huffman_codes[], BufferedOutFile* out_file, ArchiveDirectory* archive_structure, vector<ArchiveFile *>& file_strucutre);
    void WriteFrequencyArray(BufferedOutFile* out_file, HuffmanNode* freq_arr[]);
    HuffmanNode *BuildTree(HuffmanNode *node_list[], int count);
    void GenerateCodeList(HuffmanCode *code_list[], HuffmanNode *huffman_tree);
    void WriteFileSizeArray(BufferedOutFile*  out_file, vector<ArchiveFile *>& archive_content, const file_position_t& position);
    void ReadFrequencyArray(BufferedInFile* in_file, HuffmanNode *freqarr[]);
    vector<bit_size_t *> ReadFileSizeArray(BufferedInFile* in_file);
    Archive* ReadArchiveStructure(BufferedInFile* in_file, vector<bit_size_t *>& file_size_array, HuffmanNode* huffman_tree, const string& os_path);
    void MigrateFile(HuffmanCode *upd_huffman_codes[], BufferedOutFile* dest, BufferedInFile* source, ArchiveFile* file);

    Archive* opened_archive_;
    HuffmanNode *huffman_leaves_[CHARCOUNT], *huffman_tree_;
    BufferedInFile *archive_bit_file_;
    HuffmanCode *huffman_codes_[CHARCOUNT];
    atomic<bool> cancelled_;
};

#endif // HUFFMANARCHIVER_H
