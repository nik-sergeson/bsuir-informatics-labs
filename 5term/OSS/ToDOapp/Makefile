cmpld=Compiled
g=g++
c=-c
App: main.o meeting.o user.o
	@echo $@ $(cmpld)
main.o:main.cpp
	$(g) $(c) main.cpp
meeting.o:meeting.h user.h meeting.cpp
	g++ -c meeting.cpp
user.o:user.h user.cpp
	g++ -c user.cpp
	make Test
Test:
	@echo Checked
