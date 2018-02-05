CC = gcc
SRC = uuidgen.c
DEFS = # -DUSE_CPU
INC = #-I c:/mingw/amd/include
LIB = -lole32
BIN = $(SRC:.c=.exe)
CFLAGS = -Wall -O2

OBJ = $(SRC:.c=.o) $(ASRC:.S=.o) 

all: 
	$(CC) $(CFLAGS) $(INC) -c $(SRC)
	$(CC) $(OBJ) $(CFLAGS) $(LIB) -o $(BIN)

clean:
	-rm *.o *.exe *~
