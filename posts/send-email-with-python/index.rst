.. title: Send email with python
.. slug: send-email-with-python
.. date: 2014-09-25 11:20:32 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

This is a simple snippets for sending an email with a gmail smtp server.

If you want to send emails from localhost, you will have to first enable an smtp server.

So, the simplest is to use gmail smtp server:

.. code:: python

  import smtplib
 
  # define the method
  def sendemail(from_addr, to_addr_list, cc_addr_list,
                subject, message,
                login, password,
                smtpserver='smtp.gmail.com:587'):
      header  = 'From: %s\n' % from_addr
      header += 'To: %s\n' % ','.join(to_addr_list)
      header += 'Cc: %s\n' % ','.join(cc_addr_list)
      header += 'Subject: %s\n\n' % subject
      message = header + message
 
      server = smtplib.SMTP(smtpserver)
      server.starttls()
      server.login(login,password)
      problems = server.sendmail(from_addr, to_addr_list, message)
      server.quit()

  #execute the method
  sendemail('me@domain.com', ['you@yourdomain.com'], ['andyou@yourdomain.com'], 
            'test subject', 'test message', 'mylogin@gmail.com', 'mypassword')


Source:

- http://rosettacode.org/wiki/Send_an_email#Python

- http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email
