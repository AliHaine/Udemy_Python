import smtplib, ssl


def gmail_send(target, msg):
	host = "smtp.gmail.com"
	port = 0
	mail="mail@gmail.com"
	key="key"
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(host, port, context=context) as serv:
		serv.login(mail, key)
		serv.sendmail(mail, target, msg)