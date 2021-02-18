#include <sys/types.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <time.h>
#include <string.h>
#include <dirent.h>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <signal.h>
#include <vector>
using namespace std;

typedef struct dconfig{
    unsigned int sleeptime;
    string path;
    string logpath;
    string filelistpath;
    time_t last_run;
}dconfig;

int ReadConfig(dconfig &conf);
int WriteFileList(vector<string> &flist,dconfig conf);
int GetChanges(dconfig conf);

int ReadConfig(dconfig &conf){
    time_t rawtime;
    rawtime = time (NULL);
    cout<<rawtime;
    ifstream config("/windows/Labs/labs.5term/OSS/DaemonProj/dconfig/config.cfg");
    if(config == NULL) {
        return -1;
    }
    if(config.eof())
        return -1;
    getline(config,conf.path);
     getline(config,conf.logpath);
      getline(config,conf.filelistpath);
    if(!(config>>conf.sleeptime))
        return -1;
    conf.last_run=rawtime;
   return 0;
}

int WriteFileList(vector<string> &flist,dconfig conf){
    ofstream files(conf.filelistpath.c_str());
    if(files == NULL) {
        return -1;
    }
    for(int i=0;i<flist.size()-1;i++){
        files<<flist[i]<<endl;
    }
    files<<flist[flist.size()-1];
    return 0;
}

vector<string> ReadFileList(dconfig conf){
    ifstream files(conf.filelistpath.c_str(),ios::in);
    string line;
    vector<string> flist;
    if(files == NULL) {
        return flist;
    }
    while(getline(files,line)){
        flist.push_back(string(line));
    }
    return flist;
}

int WriteLog(vector<string> created,vector<string> deleted,vector<string> modified,dconfig conf){
     ofstream log(conf.logpath.c_str(),ios::app);
     time_t rawtime;
    rawtime = time (NULL);
     if(log==NULL){
        log.close();
        ofstream logn("dconfig/filelog.log");
        log.open("dconfig/filelog.log",ios::app);
     }
     log<<"Started   "<<ctime(&rawtime)<<endl;
     for(int i=0;i<created.size();i++)
        log<<created[i]<<"   "<<"created"<<endl;
    for(int i=0;i<deleted.size();i++)
        log<<deleted[i]<<"   "<<"deleted"<<endl;
    for(int i=0;i<modified.size();i++)
        log<<modified[i]<<"   "<<"modified"<<endl;
    return 0;
}

int GetChanges(dconfig conf){
    struct dirent *epdf;
    struct stat st;
    DIR *dpdf;
    vector<string> oldfiles,newfiles,deleted,created,modified;
    oldfiles=ReadFileList(conf);
    dpdf = opendir(conf.path.c_str());
    if (dpdf != NULL){
        while (epdf = readdir(dpdf)){
            if(strcmp(epdf->d_name,".")!=0&&strcmp(epdf->d_name,"..")!=0)
                newfiles.push_back(string(epdf->d_name));
        }
        closedir(dpdf);
   }
   else
        return -1;
    for(int i=0;i<oldfiles.size();i++){
        if(find(newfiles.begin(),newfiles.end(),oldfiles[i])==newfiles.end())
            deleted.push_back(oldfiles[i]);
    }
    for(int i=0;i<newfiles.size();i++){
        if(find(oldfiles.begin(),oldfiles.end(),newfiles[i])==oldfiles.end())
            created.push_back(newfiles[i]);
    }
    for(int i=0;i<newfiles.size();i++){
        stat((conf.path+"/"+newfiles[i]).c_str(), &st);
        if(st.st_mtim.tv_sec>conf.last_run){
            modified.push_back(string(newfiles[i]));
            }
    }
    WriteFileList(newfiles,conf);
    WriteLog(created,deleted,modified,conf);
    return 0;
}

int SetPidFile()
{
    FILE* f;

    f = fopen("/var/run/mydaemon/mydaemon.pid", "w+");
    if (f)
    {
        fprintf(f, "%u", getpid());
        fclose(f);
    }
    else
        return -1;
    return 0;
}

void term_handler(int i)
{
    unlink("/var/run/mydaemon/mydaemon.pid");
    exit(EXIT_SUCCESS);
}

int main(void) {
dconfig conf;
struct sigaction sa;
pid_t pid, sid;
FILE *file = fopen("/var/run/mydaemon/mydaemon.pid","r");
if(file!=NULL){
    fclose(file);
    exit(EXIT_FAILURE);
}
pid = fork();
if (pid ==-1) {
    exit(EXIT_FAILURE);
}
if (pid > 0) {
    exit(EXIT_SUCCESS);
}
umask(0);
sid = setsid();
if (sid == -1) {
    exit(EXIT_FAILURE);
}
if ((chdir("/")) ==-1) {
    exit(EXIT_FAILURE);
}
close(STDIN_FILENO);
close(STDOUT_FILENO);
close(STDERR_FILENO);
SetPidFile();
sa.sa_handler = term_handler;
sigaction(SIGTERM, &sa, 0);
ReadConfig(conf);
while (1) {
    time_t rawtime;
    GetChanges(conf);
    rawtime = time (NULL);
    conf.last_run=rawtime;
    sleep(conf.sleeptime);
}
exit(EXIT_SUCCESS);
}

