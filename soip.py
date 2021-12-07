from sys import argv
import requests,re
soip=argv
url='https://www.ip138.com/iplookup.asp?ip={0}&action=2'.format(soip[1])
header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
cookie={"Cookie":"PHPSESSID=n90ksaiimj1ao08g6g2sc86uot; ASPSESSIONIDASTBRSBS=IJEOAMMBPPPIBNFNKIBAMKCP; ASPSESSIONIDCQCASTBR=JGOAHLMBHIMLAHENHMAMPEIE"}
reponse=requests.get(url,cookies=cookie,headers=header)
reall=reponse.content.decode('GB2312')
find=str(re.findall("{(.*?)}",reall)[0]).split(',')

def qingxi(x):return re.findall("\"(.*?)\"",x)
fin=dict()
for i in range(len(find)):
	try:
		fin.update({qingxi(find[i])[0]:qingxi(find[i])[1]})
	except:
		pass
print('----------------李由制作-------------------')
print('归属地及其网络','\n---------------------------\n',fin['ASN归属地'])
print('************************')
print('iP段','\n---------------------------\n',fin['iP段'])
