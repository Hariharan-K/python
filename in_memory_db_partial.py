# Implementation of in memory db of key value stores
# The task is create a very simple in-memory database, which has a very limited command set. All of the commands are going to 
# be fed to you one line at a time via stdin, and your job is the process the commands and perform whatever operation the command 
#dictates. Here are the basic commands you need to handle:

set [name] [value]: Set a variable [name] to the value [value]. Neither variable names or values will ever contain spaces.
get [name]: Print out the value stored under the variable [name]. Print NULL if that variable name hasn't been set.
delete [name]: Unset the variable [name]
end [End the program]

So here is a sample input:

set a 10
get a
10
delete a
get a
NULL
end

###################3

import sys

cmd_list = ['SET', 'GET', 'DELETE', 'BEGIN', 'ROLLBACK', 'COMMIT', 'END']

db_store = {}


def set_val(key, val):
    #global db_store
    print ("key = ", key, "val = ", val)
    db_store[key] = val
    return True

    
def get_val (key):
        #global db_store
        if key in db_store:
            return (db_store[key])
        else:
            return None
        
def delete_key(key):
        #global db_store
        if key in db_store:
            del (db_store[key])
            return True
        else:
            return False

def cmd_process():
    #global db_store
    global cond
    query = input("Command: ")
    tokens = query.split(' ')
    token_length = len(tokens)
    #print("tokens : ", tokens)
    #print ("token_length", token_length)
    
    if token_length == 0 or token_length > 3:
            print ("Invalid Command")
            return None
    if token_length == 1:
        cmd = tokens[0]
        if cmd not in ['begin','commit','rollback','end']:
            print ("Invalid command")
            return None
        if cmd == 'end':
            print ("Code ends")
            sys.exit()
           
            
    if token_length == 2:
        cmd = tokens[0]
        key = tokens[1]
        if cmd not in ['get', 'delete']:
            print ("Invalid command")
            return None
        else:
            if cmd == 'get':
                val = get_val(key)
                if val == None:
                    print("NULL")
                else:
                    print(val)
            elif cmd == 'delete':
                delete_key(key)
                
    if token_length == 3:
        
        cmd = tokens[0]
        key = tokens[1]
        val = tokens[2]
        print ("cmd = ", cmd)
        if cmd == 'set':
            ret_val = set_val(key,val)
            if ret_val:
                print("value set successfully")
        else:
            print ("invalid command")
            return None
            
            
def execute_code():
    
    cond = True
    while cond:
        cmd_process()
        #print (db_store)
        
execute_code()
