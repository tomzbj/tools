CC = gcc
SRC = crc32.c
DEFS = 
INC = 
LIB = 
BIN = $(SRC:.c=.exe)
CFLAGS = -Wall -O2

OBJ = $(SRC:.c=.o) $(ASRC:.S=.o) 

all: 
	$(CC) $(CFLAGS) $(INC) -c $(SRC)
	$(CC) $(OBJ) $(CFLAGS) $(LIB) -o $(BIN)

clean:
	-rm *.o *.exe *~
