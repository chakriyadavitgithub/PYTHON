users=[{"eid":1,"ename":"Orel","email":"obraferton0@abc.net.au","gender":"Female"},
{"eid":2,"ename":"Lindie","email":"lvaleri1@baidu.com","gender":"Female"},
{"eid":3,"ename":"Noel","email":"nborrott2@fc2.com","gender":"Male"},
{"eid":4,"ename":"Tarrah","email":"tgatehouse3@123-reg.co.uk","gender":"Female"},
{"eid":5,"ename":"Ana","email":"aeccleshare4@homestead.com","gender":"Female"},
{"eid":6,"ename":"Orren","email":"obaiss5@cyberchimps.com","gender":"Male"},
{"eid":7,"ename":"Darbie","email":"dbaurerich6@wiley.com","gender":"Female"},
{"eid":8,"ename":"Blakeley","email":"bwildsmith7@acquirethisname.com","gender":"Female"},
{"eid":9,"ename":"Esta","email":"ebasilotta8@surveymonkey.com","gender":"Female"},
{"eid":10,"ename":"Berkie","email":"bhavenhand9@deliciousdays.com","gender":"Male"},
{"eid":11,"ename":"Ashely","email":"alevera@smh.com.au","gender":"Female"},
{"eid":12,"ename":"Sandro","email":"scomptonb@rediff.com","gender":"Male"},
{"eid":13,"ename":"Carilyn","email":"cnuddsc@ebay.com","gender":"Female"},
{"eid":14,"ename":"Jordan","email":"jbirtchnelld@sphinn.com","gender":"Male"},
{"eid":15,"ename":"Kermit","email":"kcurraghe@jigsy.com","gender":"Male"},
{"eid":16,"ename":"Suzi","email":"smcdermottrowf@independent.co.uk","gender":"Female"},
{"eid":17,"ename":"Vinni","email":"vpulhosterg@ucoz.com","gender":"Female"},
{"eid":18,"ename":"Towny","email":"ttrumanh@linkedin.com","gender":"Male"},
{"eid":19,"ename":"Sandro","email":"sflemingi@goo.gl","gender":"Male"},
{"eid":20,"ename":"Shirl","email":"sipslyj@ucoz.com","gender":"Female"},
{"eid":21,"ename":"Phil","email":"pschonfeldk@prnewswire.com","gender":"Male"},
{"eid":22,"ename":"Mathe","email":"mhouseagol@intel.com","gender":"Male"},
{"eid":23,"ename":"Marnia","email":"mketcherm@gmpg.org","gender":"Agender"},
{"eid":24,"ename":"Rutherford","email":"rfoulsern@boston.com","gender":"Male"},
{"eid":25,"ename":"Garald","email":"gkenwrighto@webnode.com","gender":"Genderfluid"},
{"eid":26,"ename":"Carlie","email":"cbrendekep@hp.com","gender":"Male"},
{"eid":27,"ename":"Clayton","email":"cbutterickq@cnn.com","gender":"Male"},
{"eid":28,"ename":"Barclay","email":"bjorir@timesonline.co.uk","gender":"Male"},
{"eid":29,"ename":"Giuditta","email":"gleggitts@buzzfeed.com","gender":"Genderqueer"},
{"eid":30,"ename":"Selene","email":"sdanielskit@sitemeter.com","gender":"Female"},
{"eid":31,"ename":"Tymothy","email":"tvilau@apple.com","gender":"Genderqueer"},
{"eid":32,"ename":"Georgina","email":"gcarrabotv@blogs.com","gender":"Agender"},
{"eid":33,"ename":"Claire","email":"catrillw@shinystat.com","gender":"Male"},
{"eid":34,"ename":"Hugh","email":"hbrownsteinx@slate.com","gender":"Male"},
{"eid":35,"ename":"Caty","email":"cstanworthy@blinklist.com","gender":"Female"},
{"eid":36,"ename":"Vivyan","email":"vfoystonz@arstechnica.com","gender":"Female"},
{"eid":37,"ename":"Harriott","email":"htuer10@1und1.de","gender":"Agender"},
{"eid":38,"ename":"Catherin","email":"ccutriss11@salon.com","gender":"Female"},
{"eid":39,"ename":"Deb","email":"dwrathmall12@hao123.com","gender":"Female"},
{"eid":40,"ename":"Hall","email":"hkeaves13@cdc.gov","gender":"Male"},
{"eid":41,"ename":"Dudley","email":"dedess14@gmpg.org","gender":"Male"},
{"eid":42,"ename":"Marillin","email":"mjasiak15@sphinn.com","gender":"Female"},
{"eid":43,"ename":"Karel","email":"ksinden16@europa.eu","gender":"Male"},
{"eid":44,"ename":"Filippa","email":"fwoffinden17@theglobeandmail.com","gender":"Female"},
{"eid":45,"ename":"Tore","email":"tvillalta18@ft.com","gender":"Male"},
{"eid":46,"ename":"Domini","email":"deasum19@uiuc.edu","gender":"Female"},
{"eid":47,"ename":"Boigie","email":"bgoldin1a@surveymonkey.com","gender":"Male"},
{"eid":48,"ename":"Kimberlee","email":"kclutten1b@gmpg.org","gender":"Female"},
{"eid":49,"ename":"Bordy","email":"bpleace1c@privacy.gov.au","gender":"Male"},
{"eid":50,"ename":"Crysta","email":"cgurney1d@chron.com","gender":"Female"}]
no_of_male_users=0
no_of_female_users=0
i=0
while i<=len(users)-1:
    if users[i]['gender'] =='Male':
        no_of_male_users = no_of_male_users +1
    elif users[i]['gender']=='Female':
        no_of_female_users = no_of_female_users+1
    i=i+1   
print("No of Male:", no_of_male_users)
print("No of FeMale: ", no_of_female_users)