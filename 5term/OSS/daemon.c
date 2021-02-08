#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>
#include <dirent.h>

typedef struct dconfig{
    unsigned int sleeptime;
    char path[80];
}dconfig;

int ReadConfig(dconfig* conf);
int WriteFileList(char **flist,int size);
int GetChanges(dconfig conf);

int ReadConfig(dconfig* conf){
    FILE * config;
    char line[80];
    config = fopen("dconfig/config.cfg", "r");
    if(config == NULL) {
        return -1;
    }
    if(fgets(line, 80, config) != NULL){
        strcpy(conf->path,line);
    }
    else
        return -1;
    //conf->path[strlen(conf->path)-1]='\0';
   if(fgets(line, 80, config) != NULL)
   {
        sscanf (line, "%u", &conf->sleeptime);
   }
   else
        return -1;
   fclose(config);
   return 1;
}

int WriteFileList(char **flist,int size){
    FILE * filelist;
    char line[80];
    filelist = fopen("dconfig/files", "w");
    if(filelist == NULL) {
        return -1;
    }
    for(int i=0;i<size;i++){
        fputs(flist[i],filelist);
    }
    fclose(filelist);
    return 1;
}

int GetChanges(dconfig conf){
    FILE * oldfiles;
    char **oldflist,**newfiles,**created,**deleted;
    struct dirent *epdf;
    DIR *dpdf;
    char line[80];
    int ofcounter=0,nfcounter=0,creatcounter=0,deletcounter=0,j=0;
    bool found;
    oldfiles = fopen("dconfig/files", "r");
    if(oldfiles == NULL) {
        return -1;
    }
    oldflist=(char **)calloc(200,sizeof(char *));
    for(int i=0;i<200;i++){
        oldflist[i]=(char *)calloc(80,sizeof(char));
    }
    while(fgets(line, 80, oldfiles) != NULL){
        strcpy(oldflist[i],line);
        ++ofcounter;
    }
    newfiles=(char **)calloc(200,sizeof(char *));
    for(int i=0;i<200;i++){
        newfiles[i]=(char *)calloc(80,sizeof(char));
    }
    dpdf = opendir(conf.path);
    if (dpdf != NULL){
        while (epdf = readdir(dpdf))
            strcpy(newfiles[nfcounter++],epdf->d_name);
        closedir(dpdf);
   }
   else
        return -1;
    for(int i=0;i<nfcounter;i++){

    }

}

}
/*
int main(void) {
dconfig conf;
pid_t pid, sid;
/*pid = fork();
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
ReadConfig((&conf));
printf("%s\n",conf.path);
printf("%u\n",conf.sleeptime);

scanf("%s");
/*while (1) {

    sleep(conf.sleeptime);
}
exit(EXIT_SUCCESS);
}*/

