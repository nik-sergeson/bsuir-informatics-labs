using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;

public class MyWathcer<Celltype> : IDisposable
    where Celltype : struct
{
    private FileSystemWatcher _watcher;
    private string _filename;
    private Matrix<Celltype> _matr;
    public MyWathcer(string path, string format, string name, Matrix<Celltype> matr, FileSystemEventHandler handler)
    {
        _matr = matr;
        _filename = name;
        _watcher = new FileSystemWatcher(path, format)
        {
            IncludeSubdirectories = true
        };
        if (handler != null)
        {
            _watcher.Created += handler;
            _watcher.Deleted += handler;
            _watcher.Changed += handler;
        }
        _watcher.EnableRaisingEvents = true;
    }

    public void Dispose()
    {
        _watcher.Dispose();
    }
}