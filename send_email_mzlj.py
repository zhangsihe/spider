import smtplib
import mysql.connector
import datetime
import var_dump

from email.mime.text import MIMEText
from pprint import pprint

mydb = mysql.connector.connect(host="121.4.191.75", user="root", passwd="!Zz1995711", database="spider")
mycursor = mydb.cursor(dictionary=True)

sql = "SELECT * FROM cnforex_bjdp where (author=%s or author=%s) and send_email=%s limit 1"
mycursor.execute(sql, ('墨竹言金', '陈招锡', '0',))
articleData = mycursor.fetchall()

if len(articleData) > 0:
    updateSql = "UPDATE cnforex_bjdp SET send_email=1 WHERE id=%s"
    mycursor.execute(updateSql, (articleData[0]['id'],))
    mydb.commit()

    var_dump.var_dump(articleData)

    mailserver    = "smtp.qq.com"           # 邮箱服务器地址
    username_send = '1611729317@qq.com'     # 邮箱用户名
    password      = 'mejfjzyymhjxbcec'      # 邮箱密码：需要使用授权码
    username_recv = 'zhangsihe1995@qq.com'  # 收件人，多个收件人用逗号隔开

    mail = MIMEText("<p>" + articleData[0]['title'] + '&nbsp;&nbsp;&nbsp;<b>' + articleData[0]['author'] + "</b></p>" +
                    articleData[0]['body'], 'html', 'utf-8')

    mail['Subject'] = datetime.datetime.now().strftime("%m%d") + '日墨竹论金爬取数据'
    mail['From']    = username_send  # 发件人
    mail['To']      = username_recv  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工

    smtp = smtplib.SMTP(mailserver, port=25)  # 连接邮箱服务器，smtp的端口号是25
    smtp.login(username_send, password)       # 登录邮箱
    smtp.sendmail(username_send, username_recv, mail.as_string())  # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    smtp.quit()  # 发送完毕后退出smtp
else:
    print('no data need send mail')