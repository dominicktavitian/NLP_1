#Scraper for BBC 

#import packages
import requests 
import pandas as pd
from bs4 import BeautifulSoup


allLinks = ['http://www.bbc.com/news/world-middle-east-41775948', 'http://www.bbc.com/news/world-africa-41790476', 
        'http://www.bbc.com/news/business-41779341', 'http://www.bbc.com/news/technology-41776215',
        'http://www.bbc.com/news/entertainment-arts-41790781', 'http://www.bbc.com/news/world-europe-41791446',
        'http://www.bbc.com/news/world-asia-41791842', 'http://www.bbc.com/news/world-us-canada-40050607',
        'http://www.bbc.com/news/uk-england-cambridgeshire-41775910', 'http://www.bbc.com/news/magazine-41757047',
        'http://www.bbc.com/news/entertainment-arts-41692370', 'http://www.bbc.com/news/world-us-canada-41792432',
        'http://www.bbc.com/news/technology-41775968', 'http://www.bbc.com/news/world-asia-41757232',
        'http://www.bbc.com/news/health-41724994', 'http://www.bbc.com/news/science-environment-41665459',
        'http://www.bbc.com/news/uk-41744344', 'http://www.bbc.com/news/science-environment-41740076',
        'http://www.bbc.com/news/science-environment-41724022', 'http://www.bbc.com/news/uk-scotland-north-east-orkney-shetland-41669774',
        'http://www.bbc.com/news/uk-england-cambridgeshire-41748336', 'http://www.bbc.com/news/business-41775963',
        'http://www.bbc.com/news/business-41769488', 'http://www.bbc.com/news/business-41779505',
        'http://www.bbc.com/news/business-41772926', 'http://www.bbc.com/news/uk-politics-41774817',
        'http://www.bbc.com/news/business-41773714', 'http://www.bbc.com/news/business-41771089', 
        'http://www.bbc.com/news/business-41773706', 'http://www.bbc.com/news/business-41762464', 
        'http://www.bbc.com/news/business-41766782', 'http://www.bbc.com/news/business-41771088', 
        'http://www.bbc.com/news/uk-scotland-41788247', 
        'http://www.bbc.com/news/uk-41792997', 'http://www.bbc.com/news/uk-england-merseyside-41736600',
        'http://www.bbc.com/news/uk-41787710', 'http://www.bbc.com/news/uk-england-41682481', 
        'http://www.bbc.com/news/uk-scotland-glasgow-west-41787786', 'http://www.bbc.com/news/uk-england-cumbria-41788514',
        'http://www.bbc.com/news/uk-scotland-edinburgh-east-fife-41789888',
        'http://www.bbc.com/news/uk-41788417',  
        'http://www.bbc.com/news/world-latin-america-41792593', 'http://www.bbc.com/news/world-us-canada-41786470',
        'http://www.bbc.com/news/world-us-canada-41787046', 'http://www.bbc.com/news/world-us-canada-41780916',
        'http://www.bbc.com/news/world-us-canada-41774066', 'http://www.bbc.com/news/technology-41785158',
        'http://www.bbc.com/news/world-us-canada-41784227',
        'http://www.bbc.com/news/world-middle-east-41793103', 'http://www.bbc.com/news/world-europe-41787919',
        'http://www.bbc.com/news/world-africa-41789118', 'http://www.bbc.com/news/world-europe-41789240',
        'http://www.bbc.com/news/world-latin-america-41791591', 'http://www.bbc.com/news/world-latin-america-41779491',
        'http://www.bbc.com/news/entertainment-arts-41786923', 'http://www.bbc.com/news/world-us-canada-41768859',
        'http://www.bbc.com/news/magazine-41595585', 'http://www.bbc.com/news/magazine-41748485', 
        'http://www.bbc.com/news/magazine-40731751', 'http://www.bbc.com/news/magazine-41715839', 
        'http://www.bbc.com/news/magazine-41569900', 'http://www.bbc.com/news/magazine-41271418', 
        'http://www.bbc.com/news/magazine-41698293', 'http://www.bbc.com/news/magazine-41504285', 
        'http://www.bbc.com/news/magazine-41640746', 'http://www.bbc.com/news/magazine-41510293', 
        'http://www.bbc.com/news/magazine-41588548', 'http://www.bbc.com/news/magazine-41533411', 
        'http://www.bbc.com/news/entertainment-arts-41763131', 'http://www.bbc.com/news/entertainment-arts-41770018',
        'http://www.bbc.com/news/entertainment-arts-41780962', 'http://www.bbc.com/news/entertainment-arts-41779731',
        'http://www.bbc.com/news/entertainment-arts-41775030', 'http://www.bbc.com/news/entertainment-arts-41776559',
        'http://www.bbc.com/news/entertainment-arts-41774701', 'http://www.bbc.com/news/uk-41783898', 
        'http://www.bbc.com/news/uk-politics-41783238', 'http://www.bbc.com/news/uk-41785235',
        'http://www.bbc.com/news/uk-politics-41780876', 'http://www.bbc.com/news/uk-scotland-scotland-politics-41775222',
        'http://www.bbc.com/news/uk-politics-41775307', 'http://www.bbc.com/news/uk-politics-41774991', 
        'http://www.bbc.com/news/uk-politics-41332364', 'http://www.bbc.com/news/uk-politics-32810887',
        'http://www.bbc.com/news/uk-politics-40249644', 'http://www.bbc.com/news/uk-politics-40243782',
        'http://www.bbc.com/news/world-asia-india-41772987', 'http://www.bbc.com/news/health-41666563', 
        'http://www.bbc.com/news/health-41763958', 'http://www.bbc.com/news/health-41724992', 
        'http://www.bbc.com/news/health-41724996', 'http://www.bbc.com/news/technology-41735104', 
        'http://www.bbc.com/news/health-41692815', 'http://www.bbc.com/news/uk-41696236', 
        'http://www.bbc.com/news/world-africa-41713919', 'http://www.bbc.com/news/health-41678533', 
        'http://www.bbc.com/news/health-41644020', 'http://www.bbc.com/news/health-41720867', 
        'http://www.bbc.com/news/world-europe-41777785', 'http://www.bbc.com/news/health-41693229', 
        'http://www.bbc.com/news/world-us-canada-41701718', 'http://www.bbc.com/news/health-41725082', 
        'http://www.bbc.com/news/uk-england-41736960', 'http://www.bbc.com/news/world-middle-east-41764156',
        'http://www.bbc.com/news/world-europe-41742857', 'http://www.bbc.com/news/world-africa-41388419', 
        'http://www.bbc.com/news/world-us-canada-41766627', 'http://www.bbc.com/news/uk-england-york-north-yorkshire-41787870',
        'http://www.bbc.com/news/uk-england-derbyshire-41726836', 'http://www.bbc.com/news/uk-wales-south-east-wales-41723244',
        'http://www.bbc.com/news/uk-england-lancashire-41673733', 'http://www.bbc.com/news/uk-wales-north-west-wales-41564414',
        'http://www.bbc.com/news/world-us-canada-41274060', 'http://www.bbc.com/news/world-us-canada-40879870', 
        'http://www.bbc.com/news/world-us-canada-40812196', 'http://www.bbc.com/news/technology-41761262',
        'http://www.bbc.com/news/business-40487639', 'http://www.bbc.com/news/technology-41775010', 
        'http://www.bbc.com/news/technology-40170652', 'http://www.bbc.com/news/health-41724994', 
        'http://www.bbc.com/news/world-us-canada-40053163', 'http://www.bbc.co.uk/news/business-39559232',
        'http://www.bbc.com/news/uk-england-devon-41444530', 'http://www.bbc.com/news/business-33147278',
        'http://www.bbc.com/news/uk-england-cornwall-36481936', 'http://www.bbc.com/news/uk-england-38516961',
        'http://www.bbc.com/news/business-38688939', 'http://www.bbc.com/news/business-41718026',
        'http://www.bbc.com/news/uk-england-hampshire-41684280', 'http://www.bbc.com/news/uk-scotland-south-scotland-41514313',
        'http://www.bbc.com/news/uk-scotland-north-east-orkney-shetland-41317098', 'http://www.bbc.com/news/business-36822363',
        'http://www.bbc.com/news/business-41335004', 'http://www.bbc.co.uk/news/uk-northern-ireland-36478967',
        'http://www.bbc.co.uk/news/uk-northern-ireland-41280204', 'http://www.bbc.com/news/uk-england-tyne-36353205',
        'http://www.bbc.com/news/world-europe-17405415', 'http://www.bbc.co.uk/news/world-europe-36931851',
        'http://www.bbc.com/news/world-europe-36937346', 'http://www.bbc.co.uk/news/world-europe-32309044',
        'http://www.bbc.com/news/science-environment-34539056', 'http://www.bbc.com/news/uk-england-norfolk-14031585',
        'http://www.bbc.com/news/12858580', 'http://www.bbc.com/news/uk-scotland-scotland-business-41746035',
        'http://www.bbc.com/news/world-europe-41788898', 'http://www.bbc.com/news/uk-scotland-scotland-politics-41627216',
        'http://www.bbc.com/news/world-us-canada-41780916', 'http://www.bbc.com/news/uk-scotland-edinburgh-east-fife-41735392',
        'http://www.bbc.com/news/uk-scotland-highlands-islands-41722101', 'http://www.bbc.com/news/uk-northern-ireland-41713045',
        'http://www.bbc.com/news/uk-england-manchester-41736409', 'http://www.bbc.com/news/uk-england-manchester-41683625', 
        'http://www.bbc.co.uk/news/business-41633941', 'http://www.bbc.com/news/uk-england-humber-41787871',
        'http://www.bbc.com/news/uk-scotland-edinburgh-east-fife-41789888', 'http://www.bbc.co.uk/news/uk-wales-south-east-wales-41582508',
        'http://www.bbc.com/news/world-africa-41773919', 'http://www.bbc.com/news/world-africa-41757612',
        'http://www.bbc.com/news/world-asia-india-41748195', 'http://www.bbc.com/news/world-us-canada-41766991',
        'http://www.bbc.co.uk/news/world-asia-41329669', 'http://www.bbc.com/news/uk-northern-ireland-34132633',
        'http://www.bbc.com/news/business-41006673', 'http://www.bbc.com/news/business-41344946', 
        'http://www.bbc.com/news/business-41646443', 'http://www.bbc.com/news/business-40998065',
        'http://www.bbc.com/news/business-18341082', 'http://www.bbc.com/news/business-38914905', 
        'http://www.bbc.com/news/uk-scotland-scotland-politics-41774015', 'http://www.bbc.com/news/uk-northern-ireland-41783827',
        'http://www.bbc.com/news/uk-politics-41780876', 'http://www.bbc.com/news/uk-wales-politics-41779384',
        'http://www.bbc.com/news/uk-wales-politics-41763146', 'http://www.bbc.co.uk/news/uk-politics-41761297',
        'http://www.bbc.com/news/uk-wales-41728836', 'http://www.bbc.co.uk/news/uk-politics-41720244',
        'http://www.bbc.com/news/entertainment-arts-41736435', 'http://www.bbc.com/news/uk-england-41309977',
        'http://www.bbc.com/news/uk-england-birmingham-41751228', 'http://www.bbc.co.uk/news/entertainment-arts-40681026',
        'http://www.bbc.com/news/uk-wales-south-east-wales-40431680', 'http://www.bbc.com/news/world-us-canada-38888018',
        'http://www.bbc.co.uk/news/entertainment-arts-37870495', 'http://www.bbc.com/news/entertainment-arts-34473788',
        'http://www.bbc.com/news/entertainment-arts-40873610', 'http://www.bbc.com/news/entertainment-arts-40592356',
        'http://www.bbc.com/news/entertainment-arts-26864817', 'http://www.bbc.co.uk/news/entertainment-arts-41634226',
        'http://www.bbc.com/news/entertainment-arts-41510200', 'http://www.bbc.com/news/entertainment-arts-41159573',
        'http://www.bbc.com/news/world-europe-isle-of-man-41720520', 'http://www.bbc.co.uk/news/uk-england-merseyside-41746311',
        'http://www.bbc.co.uk/news/uk-england-merseyside-41713271', 'http://www.bbc.com/news/uk-england-merseyside-41678807',
        'http://www.bbc.co.uk/news/uk-england-norfolk-41595014', 'http://www.bbc.co.uk/news/uk-england-bristol-41448194',
        'http://www.bbc.co.uk/news/business-41320568', 'http://www.bbc.co.uk/news/technology-41147007', 
        'http://www.bbc.co.uk/news/technology-41080478', 'http://www.bbc.co.uk/news/technology-40506609',
        'http://www.bbc.com/news/technology-41758407', 'http://www.bbc.com/news/technology-39997585',
        'http://www.bbc.com/news/uk-39417937', 'http://www.bbc.com/news/business-38495804',
        'http://www.bbc.co.uk/news/technology-36865208', 'http://www.bbc.com/news/technology-37009319', 
        'http://www.bbc.co.uk/news/uk-england-birmingham-41788720', 'http://www.bbc.com/news/technology-41730636',
        'http://www.bbc.com/news/technology-41651836', 'http://www.bbc.com/news/technology-41594924',
        'http://www.bbc.com/news/science-environment-18693744', 'http://www.bbc.co.uk/news/world-us-canada-31881518',
        'http://www.bbc.co.uk/news/entertainment-arts-29499007', 'http://www.bbc.co.uk/news/world-18702455',
        'http://www.bbc.com/news/uk-england-hereford-worcester-40512419', 'http://www.bbc.co.uk/news/business-39544442',
        'http://www.bbc.co.uk/news/business-39841987', 'http://www.bbc.com/news/business-41666820',
        'http://www.bbc.com/news/business-41732865', 'http://www.bbc.co.uk/news/business-41559761',
        'http://www.bbc.co.uk/news/business-41131306', 'http://www.bbc.co.uk/news/uk-scotland-scotland-business-40686965',
        'http://www.bbc.com/news/business-40604703', 'http://www.bbc.com/news/business-33196075',
        'http://www.bbc.com/news/business-40400216', 'http://www.bbc.co.uk/news/uk-scotland-scotland-business-32908125',
        'http://www.bbc.com/news/business-40523173', 'http://www.bbc.com/news/business-39871217', 
        'http://www.bbc.com/news/business-41390704', 'http://www.bbc.com/news/business-40679274',
        'http://www.bbc.com/news/technology-41785158', 'http://www.bbc.co.uk/news/business-41766782',
        'http://www.bbc.com/news/uk-england-leeds-41724535', 'http://www.bbc.com/news/uk-41784827',
        'http://www.bbc.co.uk/news/uk-northern-ireland-39098863', 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-38593289',
        'http://www.bbc.co.uk/news/world-us-canada-40109935', 'http://www.bbc.co.uk/news/business-35035743',
        'http://www.bbc.com/news/technology-37307826', 'http://www.bbc.com/news/technology-36785872',
        'http://www.bbc.com/news/technology-34278163', 'http://www.bbc.com/news/uk-northern-ireland-foyle-west-41721184',
        'http://www.bbc.co.uk/news/uk-england-lincolnshire-41734424', 'http://www.bbc.co.uk/news/world-latin-america-41702706',
        'http://www.bbc.co.uk/news/business-38515974', 'http://www.bbc.co.uk/news/business-37049835', 
        'http://www.bbc.co.uk/news/business-36266179', 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-37638720',
        'http://www.bbc.co.uk/news/business-36609834', 'http://www.bbc.co.uk/news/business-41007319',
        'http://www.bbc.com/news/uk-scotland-glasgow-west-38717338', 'http://www.bbc.co.uk/news/technology-40456033',
        'http://www.bbc.co.uk/news/business-23759838', 'http://www.bbc.co.uk/news/business-41766781',
        'http://www.bbc.co.uk/news/world-asia-china-41757971', 'http://www.bbc.co.uk/news/world-asia-china-41746245',
        'http://www.bbc.com/news/business-41493494', 'http://www.bbc.co.uk/news/technology-41775968',
        'http://www.bbc.com/news/technology-40367632', 'http://www.bbc.co.uk/news/business-40205638',
        'http://www.bbc.co.uk/news/technology-39589019', 'http://www.bbc.com/news/business-41041139',
        'http://www.bbc.com/news/business-40701930', 'http://www.bbc.co.uk/news/business-40858954', 
        'http://www.bbc.com/news/business-40211163', 'http://www.bbc.co.uk/news/business-40659617',
        'http://www.bbc.com/news/business-38232592', 'http://www.bbc.co.uk/news/business-38232311',
        'http://www.bbc.com/news/business-39204744', 'http://www.bbc.com/news/business-39892251',
        'http://www.bbc.co.uk/news/business-36583846', 'http://www.bbc.co.uk/news/world-latin-america-41529994',
        'http://www.bbc.com/news/world-latin-america-41791591', 'http://www.bbc.com/news/world-latin-america-41748838',
        'http://www.bbc.com/news/world-latin-america-41747575', 'http://www.bbc.co.uk/news/world-latin-america-41704429',
        'http://www.bbc.com/news/world-us-canada-41786470', 'http://www.bbc.com/news/world-europe-41766353',
        'http://www.bbc.co.uk/news/technology-41740768', 'http://www.bbc.co.uk/news/world-europe-41753599',
        'http://www.bbc.co.uk/news/technology-41551356', 'http://www.bbc.co.uk/news/world-europe-41522748',
        'http://www.bbc.co.uk/news/entertainment-arts-41567216', 'http://www.bbc.com/news/entertainment-arts-40742496', 
        'http://www.bbc.com/news/world-us-canada-41726134', 'http://www.bbc.co.uk/news/entertainment-arts-41735269',
        'http://www.bbc.com/news/world-us-canada-41423077', 'http://www.bbc.co.uk/news/world-us-canada-41382495',
        'http://www.bbc.co.uk/news/world-us-canada-37986429', 'http://www.bbc.com/news/world-asia-china-40171319',
        'http://www.bbc.co.uk/news/world-us-canada-39774674', 'http://www.bbc.co.uk/news/world-us-canada-39712732',
        'http://www.bbc.com/news/technology-41772604', 'http://www.bbc.com/news/uk-scotland-north-east-orkney-shetland-41729484',
        'http://www.bbc.com/news/business-41637791', 'http://www.bbc.co.uk/news/uk-scotland-north-east-orkney-shetland-41650660',
        'http://www.bbc.co.uk/news/entertainment-arts-41559076', 'http://www.bbc.co.uk/news/uk-scotland-north-east-orkney-shetland-41582045',
        'http://www.bbc.co.uk/news/uk-scotland-scotland-business-41552060', 'http://www.bbc.com/news/uk-scotland-glasgow-west-29368036']


#For loop to scrape things 
author = 'bbc'
bbcLinks =[]
num = 0
for y in allLinks:
    newURL = allLinks[num]
    fetched = requests.get(newURL)
    soup = BeautifulSoup(fetched.text, 'html.parser')
    title = soup.find('h1', attrs={'class': 'story-body__h1'}).text.strip()
    date = soup.find('div', attrs={'class': 'date date--v2'}).text.strip()
    print(title)
    storyText = soup.find('div', attrs={'class':'story-body__inner'}).find_all('p')
    newText = ''
    for x in storyText:
        i = 0
        j = storyText[i].text.strip(' "\'\t\r\n')
        newText = newText + ' ' + j
        i+=1
    
    bbcLinks.append((author, date, title, newText, newURL))
    num+=1
    
df = pd.DataFrame(bbcLinks, columns=['author', 'published', 'title', 'text', 'site_url']) 
df

df.to_csv('BBCScrape.csv', index = False, encoding = 'utf-8')