all: lastklines.so

lastklines.so: lastklines.o
	g++ -shared -Wl,-soname,lastklines.so -o lastklines.so lastklines.o

lastklines.o: lastklines.cpp
	g++ -Wall -fPIC -O2 -c lastklines.cpp -o lastklines.o

clean:
	rm -f *.o *.so

