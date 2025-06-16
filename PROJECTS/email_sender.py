import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()         #server start krne ke liye function

    #reciever email
    receiver_mail = input("Enter the receiver mail: ")

    ##mail credentials
    sender_email = "vnagpal2004@gmail.com"
    password = "jnuh zezw xhcp aeam"

    #login
    server.login(sender_email,password)

    #sending email
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")
    message = f"subject: {subject}\n\n{body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent seccessfully")

    server.quit()
    
except Exception as e:
    print("AN ERROR OCCURED",e)