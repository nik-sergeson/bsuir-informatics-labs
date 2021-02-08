#-------------------------------------------------
#
# Project created by QtCreator 2015-10-09T17:15:10
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Archiver
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    archivercontroller.cpp \
    archiver/archiver.cpp \
    archiver/archiveitem.cpp \
    archiver/archivefile.cpp \
    archiver/archivedirectory.cpp \
    huffman/huffmanarchiver.cpp \
    huffman/huffmancode.cpp \
    archiver/archive.cpp \
    huffman/huffmannode.cpp \
    bufferedfile/bufferedbitfile.cpp \
    bufferedfile/bufferedinfile.cpp \
    bufferedfile/bufferedoutfile.cpp \
    bufferedfile/bitsizet.cpp \
    bufferedfile/bufferposition.cpp \
    fileutils/fileposition.cpp \
    concurrenthuffman/huffmanextract.cpp \
    concurrenthuffman/huffmanaddfile.cpp \
    concurrenthuffman/huffmanaddfolder.cpp \
    concurrenthuffman/huffmanremovefile.cpp \
    concurrenthuffman/huffmanremovefolder.cpp

HEADERS  += mainwindow.h \
    archivercontroller.h \
    archiver/archiver.h \
    archiver/archiveitem.h \
    archiver/archivefile.h \
    archiver/archivedirectory.h \
    huffman/huffmanarchiver.h \
    huffman/huffmancode.h \
    archiver/archive.h \
    huffman/huffmannode.h \
    bufferedfile/bufferedbitfile.h \
    bufferedfile/bufferedinfile.h \
    bufferedfile/bufferedoutfile.h \
    bufferedfile/bitsizet.h \
    bufferedfile/bufferposition.h \
    fileutils/fileposition.h \
    archiverexception.h \
    concurrenthuffman/huffmanextract.h \
    concurrenthuffman/huffmanaddfile.h \
    concurrenthuffman/huffmanaddfolder.h \
    concurrenthuffman/huffmanremovefile.h \
    concurrenthuffman/huffmanremovefolder.h

FORMS    += mainwindow.ui

QMAKE_CXXFLAGS += -std=c++11
