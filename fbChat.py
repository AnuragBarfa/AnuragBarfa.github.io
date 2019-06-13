#import mechanize
#br=mechanize.Browser()
#br.set_handle_robots(False)
#br.addheaders=[('User-agent','Firefox')]
#br.open('https://www.linkedin.com/uas/login-submit')
#br.select_form(nr=0)
#br.form['session_key']='anuragbarfa64@gmail.com'
#br.form['session_password']='anurag123'
#sub=br.submit()
#print(sub.geturl())
import mechanize
br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','Firefox')]
br.open('https://www.facebook.com/login.php')
br.select_form(nr=0)
br.form['email']='100012889366759'
br.form['pass']='rama123'
sub=br.submit()
print(sub.geturl())

