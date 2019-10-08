CC=g++
CFLAGS=-I. -std=c++0x -W -Wall `pkg-config --cflags opencv` -Wno-unused-variable -g
LFLAGS=`pkg-config --libs opencv` 
#DEPS = hellomake.h

%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

generate_gt: generate_images_dataset.o 
	$(CC) -o generate_gt generate_images_dataset.o $(LFLAGS)

clean:
	rm *.o generate_gt
