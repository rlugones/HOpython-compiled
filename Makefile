.PHONY: default help object executable all clean
CC = gcc

FOLDER = src
SOURCE = $(wildcard $(FOLDER)/*.c)
OBJECTS = $(patsubst %.c, %.o, $(SOURCE))

LIBRARY = libmymath.so

default: help

help:
	@echo "\
Options:\n\n\
  make objects:       compiler makes objects for every *.c\n\
  make library:       compiler makes dynamic library\n\
  make all:           build all previous\n\
  make clean:         delete output files\n\
  make help:          display this help"

objects: $(OBJECTS)

library: $(LIBRARY)

all: objects library

%.o: %.c
	$(CC) -c -fPIC $^ -o $@

%.so: $(OBJECTS)
	$(CC) -shared $^ -o $@

clean:
	rm -rfv $(OBJECTS) $(LIBRARY)
