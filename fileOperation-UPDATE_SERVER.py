"""
-----Usage of list operations(to update or read files)----
1.To update server configuration file when a metric/alert is met
2.To update application properties automatically

--------2 types of operations-------
1.Read
2.Write

TASK (Update server.conf file when connections reach to maximum level of 200)
1.Open and read the file
2.Store inside variable
3.Write mode
4.Updating maximum connection file---->if condition
"""



def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key +"="+ value +"\n")
            else:
                file.write(line)

update_server_config("server-UPDATE_SERVER.conf","MAX_CONNECTIONS", "1000")


#After run this, check whether the MAX_CONNECTIONS of server.conf file has changed(600 to 1000)