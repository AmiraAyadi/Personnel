import email.message
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders




liste_mail=[]
liste_nom=[]

e=input("Votre addresse mail\n")
mdp=input("Votre mot de passe\n")

numero=int(input("combien d'expediteur ?\n"))
for i in range(0,numero):
    liste_mail.append(input("entrer l'adresse\n"))
    print("Quel est le nom de la personne ( que l'on va voir apres le bonjour dans le mail!")
    liste_nom.append(input())
print("recap : \n")
for i,j in (zip(liste_nom,liste_mail)):
	print(i,j)

ob=input("Quel est l'objet ? \n")

for i in range(numero):

    msg = MIMEMultipart()
    
    msg.attach(MIMEText(u"""
Bonjour %s,

Je me permets de vous faire parvenir mon CV dans le cas où vous seriez à la recherche d’une assistante mise en scene.
    
Je trouve les candidatures spontanées assez intrusives et très peu fructueuses mais c'est essentiellement grâce à ce genre de mail que je suis engagée si je tombe au bon moment :) 

Je suis une jeune femme extremement efficace, reactive et motivée et je serai ravie de vous rencontrer dans le  cadre d’un entretien.

Bien à vous, 
Imène AYADI
0781956633

    """ % str(liste_nom[i]), "plain", _charset="utf-8"))
    filename="CV_Imene_AYADI.pdf"
    attachment=open("C:/Users/Amira AYADI/Desktop/CV (2).pdf","rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

   
    msg['Subject'] = ob
    msg['From'] = e
    msg['To'] = liste_mail[i]

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(e, mdp)
    
    server.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("envoyé")
