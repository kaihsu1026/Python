import paramiko
import datetime



def rdlog():
    """抓取EQ的RD_log"""
    now = datetime.datetime.now().strftime("%Y%m%d")    #設定當下時間(年月日)
    local_path = ( 'C:/Users/kai.hsu/Desktop/上班請開啟/夜班來臨/NGINX LOG/rdlog.log' 
                + '-' 
                +  now
                +  '_' )#本地位置
    remote_path = '/var/log/nginx/rdlog.log-' + now + '.gz'    #遠端linux主機  
     
    try:
        for i in range(191, 199):
            transport = paramiko.Transport(('10.11.2.' + str(i), 22))
            transport.connect(username=username, password=password)   #使用者登入帳密
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(remote_path, local_path  + str(i) + '.gz')  # 將遠端檔案下載到本地並重新命名
            transport.close()
            print(f"{i}下載完成")
            
    except Exception as e:
        print('LOG尚未生產', e)
            

if __name__ == '__main__':
    username = input("請輸入帳號: ")
    password = input("請輸入密碼: ")
    rdlog()






           
