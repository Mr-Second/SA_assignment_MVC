import pymysql
import socket
import json


def connect_get(stored_procedure_name, args, dataBaseAddr, userName, passWord, dataBaseName):
    conn = pymysql.connect(host=dataBaseAddr, user=userName, password=passWord, database=dataBaseName, port=1433)
    cursor = conn.cursor()

    cursor.callproc(stored_procedure_name, (args[0], args[1]))
    res = cursor.fetchall()
    print(list(res))
    _list = ["{}-{}-{}&{}".format(str(x[0].year), str(x[0].month), str(x[0].day), str(x[1])) for x in res]
    print(_list)
    return _list


if __name__ == "__main__":
    HOST = ''
    PORT = 8080
    BUFSIZE = 1024*1024  # 缓冲区大小1M
    ADDR = (HOST, PORT)
    UdpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UdpSocket.bind(ADDR)
    dataBaseAddr = 'mydb.cuwkero2hta9.us-east-1.rds.amazonaws.com'
    userName = 'admin'
    passWord = '123456789'
    dataBaseName = 'MyDataBase'
    port = 1433

    while True:
        recvData, addr = UdpSocket.recvfrom(BUFSIZE)
        recvData = str(recvData.decode())
        print(recvData)
        datalist = recvData.split('&')
        stored_procedure_name = None
        if datalist:
            if int(datalist[0]) == 1:
                stored_procedure_name = 'getTradingVolume'
            elif int(datalist[0]) == 2:
                stored_procedure_name = 'getMarketMoney'
            elif int(datalist[0]) == 3:
                stored_procedure_name = 'getTopValue'
            elif int(datalist[0]) == 4:
                stored_procedure_name = 'getMinValue'
            elif int(datalist[0]) == 5:
                stored_procedure_name = 'getTheRateOfRiseAndFall'
            args = (datalist[1], datalist[2])
            valueSet = connect_get(stored_procedure_name, args, dataBaseAddr, userName, passWord, dataBaseName)
            data = json.dumps(valueSet)
            print(type(data))
            UdpSocket.sendto(data.encode(), addr)

