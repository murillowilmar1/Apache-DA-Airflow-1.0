import smtplib 
from typing import Dict


def send_mail_f() -> Dict:
    return {
        "subject": "exitoso!",
       
    }



mail=send_mail_f() 


def send_mail (): 


    try:
     conexion = smtplib.SMTP(host="smtp.gmail.com", port = 587)
     conexion.ehlo ()


     conexion.starttls()


     conexion.login(user="murillowilmar1@gmail.com", password="iwsmlkevxcobbnne")

     
     body_text = mail["body"]
     subject = mail["subject"]
     message = "subject: {}\n\n".format(subject,body_text)
     conexion.sendmail(from_addr="murillowilmar1@gmail.com", to_addrs=["murillowilmar1@gmail.com", "fivemaths5@gmail.com"], msg=message)

     conexion.quit()

     print ("succes")
       

    except Exception as exception:

        print(exception)
        print("failure")   
if __name__ == '__main__':  
    send_mail()