import smtplib
try:
    server = smtplib.SMTP(host="smtp.gmail.com", port = 587)                # starttls is used to start the program
    server.starttls()
    reciever_email=input("enter your email: ")
    sender_email='kumawatak1015@gmail.com'
    password='ifid vmnr aztl ahgo'
    server.login(sender_email,password=password)
    subject=input("what is your problem")
    body=input("thoda details me btaoa")
    message=f"subject:{subject}\n\n{body}"
    server.sendmail(sender_email,reciever_email,message)
    print("maine mail send krdi hai")
    server.quit()
except Exception as e:
    print("mail send nai hui ❌")