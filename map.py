import base64
from cgitb import html

import folium

#create map object
import img as img
from branca.element import IFrame
from pip._internal.cli.cmdoptions import src

#create custom logo icon
logoIconPub = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub2 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub3 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub4 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub5= folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))
logoIconPub6 = folium.features.CustomIcon('./static/img/logoPub.png',icon_size=(50,50))

#create custom logo Restaurant

logoIconRestaurant1 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant2 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant3 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant4 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant5= folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))
logoIconRestaurant6 = folium.features.CustomIcon('./static/img/RestaurantLogo.png',icon_size=(50,50))

#create custom logo Museum
logoIconMuseum1 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum2 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum3= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum4 = folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum5= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))
logoIconMuseum6= folium.features.CustomIcon('./static/img/MuseumLogo.png',icon_size=(50,50))

#create cutom logo Park
logoIconPark1 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark2 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark3= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark4 = folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark5= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))
logoIconPark6= folium.features.CustomIcon('./static/img/ParkLogo.png',icon_size=(50,50))

#create monument logo
logoIconMonument1 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument2 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument3 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))
logoIconMonument4 = folium.features.CustomIcon('./static/img/Monument.png',icon_size=(50,50))






html = '<img src="data:image/png;base64,{}">'.format

m=folium.Map(location=[45.7711901, 21.2581345],zoom_start=12)


#popup Timisoara
pictureTm= base64.b64encode(open('./static/img/Tm.jpg','rb').read()).decode()
iframeTm=IFrame(html(pictureTm)+'<p>Timișoara</p>'+
                '<p> Description: Timișoara is the municipality of residence of Timiș County, Banat, Romania. </p>' +
                '<p> It is located in western Romania, close to the borders with Hungary and Serbia, on the banks of the river Bega. </p>' +
                '<p> Area: 130.5 km² </p>' +
                '<p> Metropolitan area: 244 ha </p>' +
                '<p> Weather: 15 ° C, wind from the S at 18 km / h, humidity of 56% </p>' +
                '<p> Population: 306,462 (2012) </p>' +
                '<p> Postal code: 300001-300990 </p>', width = 1280, height = 720)
popupTm= folium.Popup(iframeTm,max_width=1400)

folium.CircleMarker(
    location=[45.7560376, 21.2288460],
    radius=300,
    popup=popupTm ,
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)



#Global tooltip
tooltip='Click For more info'
#pub tooltip
tooltip1="Like pub"
tooltip2="Beraria 700"
tooltip3="The irish pub"
tooltip4="The Note Pub"
tooltip5="La capite"
tooltip6="Scart Loc Lejer"
#Restaurant tooltip
tooltip7="Restaurant Dinar"
tooltip8="Restaurant Yugoslavia"
tooltip9="Restaurant Sabres"
tooltip10="Restaurant Merlot"
tooltip11="Sky Restaurant"
tooltip12="Pescada"
#Museums
tooltip13="Muzeul de Arta"
tooltip14="Muzeul Banatului"
tooltip15="Muzeul Satului"
tooltip16="Muzeul Communist"
tooltip17="Muzeul de Transport Public „Corneliu Miklosi"
tooltip28="Typopassage museum"
#Parks
tooltip18="Zoo Garden"
tooltip19="Water Plant Park"
tooltip20="Roses Park"
tooltip21="Childrens Park"
tooltip22="Central Park"
tooltip23="Botanic Park"
#Monument
tooltip24="monumentul ostasului necunoscut din timisoara Timisoara"
tooltip25="Statuia Lupoaicei"
tooltip26="Momentul Ciumei"
tooltip27="Momentul Fercioara Maria"


#image popup
picture1= base64.b64encode(open('./static/img/like pub.png','rb').read()).decode()
iframe1=IFrame(html(picture1)+'<p>street address:Lascăr Catargiu Nr.2, Timișoara</p>'
               +'<p>Numeber phone:+40 770 157 710</p>'
               +'<a href= "https:https://www.facebook.com/likepub/">link</a>', width=594, height=594)
popup1= folium.Popup(iframe1,max_width=594)
#Monumentul Ostașului Necunoscut imagine
picture2= base64.b64encode(open('./static/img/timisoara-monument-romanian-solider.jpg','rb').read()).decode()
iframe2=IFrame(html(picture2)+'<p> Over time, the plateau in front of the Unknown Soldier Monument in Central Park has become a hot spot on Army Day. Here, in addition to the traditional wreath-laying, '
                              'There are exercises in mastering the handling of weapons, along with artistic moments of the marching band in honor of the soldiers who fought and are fighting for their country. Romanian Army Day is celebrated between October 25-28 in Timisoara, '
                              'as a tribute to those who guarded the freedom of the country. </p>', width = 500, height = 500,)
popup2= folium.Popup(iframe2,max_width=594)
#Monumentul Statuia Lupoaicei
picture3= base64.b64encode(open('./static/img/Timisoara,_Lupa_Capitolina.jpg','rb').read()).decode()
iframe3=IFrame(html(picture3)+'<p> The statue of the She-Wolf in Timisoara is a statue depicting the legend of the founders of Rome, the brothers Romulus and Remus, breastfed by a she-wolf. '
                              'The statue depicts the legend of the founding of Rome, according to which the two brothers who founded the city were cared for by a wolf. </p>', width = 394, height = 394)
popup3= folium.Popup(iframe3,max_width=394)
#Momentul sfanta treime
picture4= base64.b64encode(open('./static/img/MomentulCiumei.jpg','rb').read()).decode()
iframe4=IFrame(html(picture4)+'<p>The Plague Column, also known as the Plague Statue or the Holy Trinity Monument, is erected in the middle of the Union Square in Timisoara, in accordance with the architectural style of the surrounding buildings. </p> ', width = 594, height = 594)
popup4= folium.Popup(iframe4,max_width=594)
#Monumentul Feciora Maria
picture5= base64.b64encode(open('./static/img/Fecioara_Maria.jpg','rb').read()).decode()
iframe5=IFrame(html(picture5)+'<p> The Sfânta Maria monument is located in Timișoara, in Sfânta Maria square and was erected in 1906 on the site of an older statue of Saint Maria. '
                              'Tradition says that Gheorghe Doja was executed here. </p>', width = 300, height = 300)
popup5= folium.Popup(iframe5,max_width=300)
#Beraria 700
picture6= base64.b64encode(open('./static/img/beraria7.png','rb').read()).decode()
iframe6=IFrame(html(picture6)+'<p>street address:Coriolan Brediceanu 4</p>'+
                              ' <p>Number phone: +40 256 706 767</p>'+
                              '<p>Web site:'+'<a href= "https:https://www.facebook.com/likepub/">beraria 700</p>',width=300 ,height=300)
popup6= folium.Popup(iframe6,max_width=300)
#The irish pub
picture7= base64.b64encode(open('./static/img/The irish pub.jpg','rb').read()).decode()
iframe7=IFrame(html(picture7)+'<p>street address:str. Tarcului nr. 1,Timisoara</p>'+
                              '<p> Number phone: +40 769 222 586</p>'+
                              '<p>Web site:'+'<a href= "https://www.facebook.com/irishpubtimisoara/"</a>The irish pub</p>',width=300 ,height=300)
popup7= folium.Popup(iframe7,max_width=300)

#The Note Pub
picture8= base64.b64encode(open('./static/img/notepub.jpg','rb').read()).decode()
iframe8=IFrame(html(picture8)+'<p>street address:Bulevardul Mihai Eminescu, nr. 2</p>'+
                              ' <p>Number phone: +40 256 488 958</p>'+
                              '<p>Web site:'+'<a href= "https://www.facebook.com/TheNotePub/"</a>The Note Pub</p>',width=300 ,height=300)
popup8= folium.Popup(iframe8,max_width=300)

#La Capite
picture9= base64.b64encode(open('./static/img/Lacapite.jpg','rb').read()).decode()
iframe9=IFrame(html(picture9)+'<p>street address:Vasile Parvan, nr. 9</p>'+
                              ' <p>Number phone: +40 720 400 333</p>'+
                              '<p>Web site:'+'<a href= "https://www.facebook.com/lacapitetm/"</a>La capite</p>',width=300 ,height=300)
popup9= folium.Popup(iframe9,max_width=300)
#Scart Loc Lejer
picture10= base64.b64encode(open('./static/img/scart.jpg','rb').read()).decode()
iframe10=IFrame(html(picture10)+'<p>street address:Arhitect Laszlo Szekely, nr. 1</p>'+
                              ' <p>Number phone: +40 751 892 340</p>'+
                              '<p>Web site:'+'<a href= "https://www.facebook.com/scartloclejer/"</a>scart loc lejer</p>',width=300 ,height=300)
popup10= folium.Popup(iframe10,max_width=300)
#Restaurant Dinar

picture11= base64.b64encode(open('./static/img/logo_dinar.png','rb').read()).decode()
iframe11=IFrame(html(picture11)+'<p>street address:Barbu Iscovescu nr. 2, Timișoara, România, nr. 1</p>'+
                '<p> Number phone: +40 728 116 230 </p>' +
                '<p> Description: The old atmosphere, full of tradition, from the Balkans, you can find it now in Timisoara, at Restaurant Dinar!'
                "We aim for guests who step on our doorstep to have an authentic, place-specific experience and to be left with a special memory!"
                'Restaurant Dinar Timisoara together with Etno Kuca Dinar from Vrsac bring for the first time in Romania the traditional Balkan recipes and dishes awarded by the Global Trade Leaders Club - International Hotel & Restaurant. </p>' +
                              '<p>Web site:'+'<a href= "http://www.restaurantdinar.ro/"</a>Restaurant Dinar</p>',width=300 ,height=300)
popup11= folium.Popup(iframe11,max_width=300)

#Restaurant Yugoslavia

picture12= base64.b64encode(open('./static/img/logo-yugoslavia.jpg','rb').read()).decode()
iframe12=IFrame(html(picture12)+'<p>street address:Vadul Calugareni 1, Timișoara 300425, România, nr. 1</p>'+
                              '<p> Number phone: +40 737 394 794</p>'+
                '<p> Description: At the Yugoslavia restaurant in Timisoara, the culinary style of Serbian cuisine blends harmoniously with the unmistakable style of traditional Romanian cuisine, resulting in a variety of delicious dishes that can easily cope with the most demanding culinary tastes.'
                'The mastery and passion with which the master chefs cook at this restaurant is reflected in some real culinary masterpieces that you will surely be impressed and want to try again and the attention always directed to your requirements, make the Yugoslavia restaurant a reliable partner when you want to order food online. '
                'On the business card of this restaurant will always be written professionalism through which it is desired to offer a pleasant and unforgettable culinary experience. </p>' +
                              '<p>Web site:'+'<a href= "http://restaurantyugoslavia.ro/"</a>Restaurant Yugoslavia</p>',width=300 ,height=300)
popup12= folium.Popup(iframe12,max_width=300)

#Restaurant Sabres
picture13= base64.b64encode(open('./static/img/sabres.png','rb').read()).decode()
iframe13=IFrame(html(picture13)+'<p>street address:Craiova nr. 1, Timișoara 300587, România</p>'+
                              ' <p>Number phone: +40 356 430001</p>'+
                            '<p> Description: Sabers Restaurant is a place of soul, only good to start the journey in the culinary realms. '
                            'Passion defines and motivates us, and the relaxing atmosphere is a place of honor. </p>' +
                              '<p>Web site:'+'<a href= "http://www.sabres.ro/ro/index.php?id=1"</a>Restaurant Sabres</p>',width=300 ,height=300)
popup13= folium.Popup(iframe13,max_width=300)
#Sky Restaurant
picture14= base64.b64encode(open('./static/img/sky.jpg','rb').read()).decode()
iframe14=IFrame(html(picture14)+'<p>street address:Coriolan Brediceanu 10, Timișoara 300011, România</p>'+
                              ' <p>Number phone: +40 770 422 816</p>'+
                '<p> Description: Sky Restaurant stops the need to close your eyes when you want to escape from reality. I put your chair in the pleasant breezes, to stop your slipping and to climb close to the stars, just as fresh even in the middle of the day, in the plates full of taste. '
                'We dare to promise you the liberating feeling you give yourself every time you look at the sunset and make room for whims. We naturally make the sensations that, most of the time, you dont even expect. </P> '+

                              '<p>Web site:'+'<a href= "https://sky.restaurant/"</a>Restaurant Sky</p>',width=300 ,height=300)
popup14= folium.Popup(iframe14,max_width=300)
#Restaurant pescada
picture15= base64.b64encode(open('./static/img/pescada.png','rb').read()).decode()
iframe15=IFrame(html(picture15)+'<p>street address:Calea Sever Bocu 74, Timișoara 300254, România</p>'+
                              '<p> Number phone: +40 770 221 161</p>'+
                '<p> Description: Pescada is a Mediterranean restaurant, whose menu includes a variety of fish delicacies, masterfully prepared by Chef Daian. </p>' +
                              '<p>Web site:'+'<a href= "http://pescada.ro/"</a>Restaurant Pescada</p>',width=300 ,height=300)
popup15= folium.Popup(iframe15,max_width=300)
#Restaurant Merlot
picture16= base64.b64encode(open('./static/img/merlot.jpg','rb').read()).decode()
iframe16=IFrame(html(picture16)+'<p>street address:Splaiul Nistrului 1, Timișoara, România</p>'+
                              ' <p>Number phone: +40 356 177 247</p>'+
                '<p> Description: Merlot Restaurant was born out of the desire to offer our guests a special experience and not just quality food.'
                'The menu is Mediterranean-inspired, featuring Italian and French cuisine.'
                '"All the ingredients were carefully chosen because we only wanted fresh and very good quality raw materials."'
                '"Pasta, sauces, syrups, sweets, all are made" at home "and without artificial ingredients."'
                'Merlot Restaurant was born out of the desire to offer our guests a special experience and not just quality food. </p>' +
                '<p>Web site:'+'<a href= "http://www.restaurant-merlot.ro/"</a>Restaurant Merlot</p>',width=300 ,height=300)
popup16= folium.Popup(iframe16,max_width=300)
#Muzeul de Arta
picture17= base64.b64encode(open('./static/img/muzeuarta.jpg','rb').read()).decode()
iframe17=IFrame(html(picture17)+'<p>street address:Piata Unirii  nr.1, Timișoara, România</p>'+
                              '</p> Number phone: +40 256 491 592</p>'+
                '<p> Description: The Art Museum of Timișoara is an art museum located in the Baroque Palace of Timișoara.'
                'The museum was created after the detachment of the art section of the Banat Museum, which operated for a period in a wing of the current building. </p>' +
                              '<p>Web site:'+'<a href= "http://www.muzeuldeartatm.ro/"</a>Mumseum of the Art</p>',width=300 ,height=300)
popup17= folium.Popup(iframe17,max_width=300)
#Muzeul Banatului
picture18= base64.b64encode(open('./static/img/banatului.jpg','rb').read()).decode()
iframe18=IFrame(html(picture18)+'<p>street address:Strada Martin Luther  nr.4, Timișoara, România</p>'+
                              ' <p>Number phone: +40 256 491 339</p>'+
                            '<p> Description: The National Museum of Banat is a museum in Timisoara with its headquarters in Huniade Castle.'
                            'It was founded in 1872 as the "Society of History and Archeology." '
                            'It houses the most important collection of archaeological objects in Banat, </p>' +
                              '<p>Web site:'+'<a href= "https://mnab.ro/"</a>The Banat museum </p>',width=300 ,height=300)
popup18= folium.Popup(iframe18,max_width=300)
#Muzeul Satului
picture19= base64.b64encode(open('./static/img/muzeusat.jpg','rb').read()).decode()
iframe19=IFrame(html(picture19)+'<p>street address:Avram Imbroane, nr 1, Timișoara, România</p>'+
                              ' <p>Number phone: +40 256 225 588</p>'+
                                 '<p> The Banat Village Museum in Timisoara is the only ethnographic museum in Romania that includes the civic center of the village,'
                                'consisting of the City Hall, the Church, the School, the National House and the birt, where most of the cultural-educational and scientific activities of a locality take place. </p>' +
                                '<p>Web site:' + '<a href= "http://muzeulsatuluibanatean.ro/"</a>The village museum </p>', width=300, height=300)

popup19= folium.Popup(iframe19,max_width=300)
#Muzeul Communist
picture20= base64.b64encode(open('./static/img/comunist.jpg','rb').read()).decode()
iframe20=IFrame(html(picture20)+'<p>street address:Arhitect Laszlo Szekely,nr 1, Timișoara, România</p>'+
                              ' <p>Number phone: +40 751 892 340</p>'+
                              '<p>Web site:'+'<a href= "http://muzeulsatuluibanatean.ro/"</a>The Communist museum </p>',width=300 ,height=300)
popup20= folium.Popup(iframe20,max_width=300)
#Tyropassage museum
picture21= base64.b64encode(open('./static/img/tyro.jpg','rb').read()).decode()
iframe21=IFrame(html(picture21)+'<p>street address:Pasaj, Podul Tinereţii, Timișoara, România</p>'+
                              '<p>Web site:'+'<a href= "https://www.typopassage.ro/"</a>Tyropassage </p>',width=300 ,height=300)
popup21= folium.Popup(iframe21,max_width=300)
#Transport Museum
picture22= base64.b64encode(open('./static/img/muztrans.jpg','rb').read()).decode()
iframe22=IFrame(html(picture22)+'<p>street address:Take Ionescu nr.56, Timișoara, România</p>'+
                                '<p>Phone Number:+40 256 277 710</p>'+
                              '<p>Web site:'+'<a href= "http://www.ratt.ro/muzeuCM.html"</a>Transport Museum </p>',width=300 ,height=300)
popup22= folium.Popup(iframe22,max_width=300)

#Roses Park
picture23= base64.b64encode(open('./static/img/gallery/rozecol.jpg','rb').read()).decode()
iframe23=IFrame(html(picture23)+'<p>Describe:Roses Park is a very beautiful park placed on the shore of the river Bega.'+
                                'The park in known for the beautfull flowers there and the white wooden arches'+
                                'The park also haves a concert hall, where most of the time organized concerts can have place.</p>'+
                              '<p>Web site:'+'<a href= "http://www.timisoara-info.ro/ro/atracii-turistice/alte-atracii/338-parcul-rozelor.html"</a>Roses Park </p>',width=1500 ,height=709)
popup23= folium.Popup(iframe23,max_width=1600)
#Botanic Park
picture24= base64.b64encode(open('./static/img/gallery/botanic-park.jpg','rb').read()).decode()
iframe24=IFrame(html(picture24)+'<p>Describe:Situated near the city center, the Botanic Park allows you to'
                                'rest from urban part of Timisoara, breathe the clean air and talk a relaxing stroll among the woods.</p>' ,width=800,height=762 )
popup24= folium.Popup(iframe24,max_width=800)
#Childrens Park
picture25= base64.b64encode(open('./static/img/gallery/child-park.jpg','rb').read()).decode()
iframe25=IFrame(html(picture25)+'<p>Describe:This is a big free playground, There are plenty of attractions for the kids+adults'
                                '(beautiful, modern slides, swings, boats, obstacles, small wooden huts, fountain and many more).'
                                'There are many trees so you can hide in the shade if it s a hot day and its placed next to Roses Park.</p>' ,width=800,height=762 )
popup25= folium.Popup(iframe25,max_width=800)
#Central Park
picture26= base64.b64encode(open('./static/img/gallery/parcul-central.jpg','rb').read()).decode()
iframe26=IFrame(html(picture26)+'<p>Describe:Central Park is one of the oldest parks in Timisoara,'
                    'dating from 1880, it haves a lot of monuments of a lot of important personalities.'
'                      The bigest one is the Romanian Soldier monument.</p>' ,width=799,height=459 )
popup26= folium.Popup(iframe26,max_width=800)
#Water Plant Park
picture27= base64.b64encode(open('./static/img/gallery/Prcul-Uzinei-13.jpg','rb').read()).decode()
iframe27=IFrame(html(picture27)+'<p>Describe:Water Plants Park is placed right next to Timisoaras Water Plant, a beautifull old building,'
'the park is very big, on both sides of the Bega river, with little playgrounds, banches, lots of trees and tables.</p>' ,width=1920,height=1080)
popup27= folium.Popup(iframe27,max_width=1920)
#Zoo Garden
picture28= base64.b64encode(open('./static/img/gallery/zoocol.jpg','rb').read()).decode()
iframe28=IFrame(html(picture28)+'<p>Describe:Placed in the Green Forest in Timsioara the Zoo is widely spread with a lot of diverse species of animals.'
                                'Cared pathways , places to stop and rest, some stops where you can even see closely the animals.</p>' ,width=1920,height=1080)
popup28= folium.Popup(iframe28,max_width=1920)

#Create markers
folium.Marker([45.7501565,21.2435880],
              popup=popup1,
              tooltip=tooltip1,
              icon = logoIconPub).add_to(m),
folium.Marker([45.75643395,21.22377593864379],
              popup=popup6,
              tooltip=tooltip2,
              icon = logoIconPub2).add_to(m),
folium.Marker([45.7572214,21.2288186],
              popup=popup7,
              tooltip=tooltip3,
              icon = logoIconPub3).add_to(m),
folium.Marker([45.7514933,21.2261728],
              popup=popup8,
              tooltip=tooltip4,
              icon = logoIconPub4).add_to(m),
folium.Marker([45.7490729,21.232528],
              popup=popup9,
              tooltip=tooltip5,
              icon = logoIconPub5).add_to(m),
folium.Marker([45.7432666,21.22441792848435],
              popup=popup10,
              tooltip=tooltip6,
              icon = logoIconPub6).add_to(m),

#Marker Restaurant

folium.Marker([45.7521036,21.240429105831176],
              popup=popup11,
              tooltip=tooltip7,
              icon=logoIconRestaurant1).add_to(m),

folium.Marker([45.7397008,21.2211746],
              popup=popup12,
              tooltip=tooltip8,
              icon=logoIconRestaurant2).add_to(m),

folium.Marker([45.7424781,21.2382903],
              popup=popup13,
              tooltip=tooltip9,
              icon=logoIconRestaurant3).add_to(m),

folium.Marker([45.7566323,21.241885075020434],
              popup=popup16,
              tooltip=tooltip10,
              icon=logoIconRestaurant4).add_to(m),

folium.Marker([45.7568019,21.2217609],
              popup=popup14 ,
              tooltip=tooltip11,
              icon=logoIconRestaurant5).add_to(m),
folium.Marker([45.7756976,21.233407907552547],
              popup=popup15,
              tooltip=tooltip12,
              icon=logoIconRestaurant6).add_to(m),


#marker Museums
folium.Marker([45.7573543,21.2292917],
              popup=popup17,
              tooltip=tooltip13,
              icon=logoIconMuseum1).add_to(m),
folium.Marker([45.7530646,21.2270757],
              popup=popup18,
              tooltip=tooltip14,
              icon=logoIconMuseum2).add_to(m),
folium.Marker([45.7770772,21.2660725],
              popup=popup19,
              tooltip=tooltip15,
              icon=logoIconMuseum3).add_to(m),
folium.Marker([45.7432619,21.2243079],
              popup=popup20,
              tooltip=tooltip16,
              icon=logoIconMuseum4).add_to(m),
folium.Marker([45.749713423026634, 21.22523713493029],
              popup=popup21,
              tooltip=tooltip28,
              icon=logoIconMuseum6).add_to(m),
folium.Marker([45.76289225,21.245905860455096],
              popup=popup22,
              tooltip=tooltip17,
              icon=logoIconMuseum5).add_to(m),
#marker park
folium.Marker([45.78158705,21.267827340914387],
              popup=popup28,
              tooltip=tooltip18,
              icon=logoIconPark1).add_to(m),
folium.Marker([45.758223099999995,21.2652973850292],
              popup=popup27,
              tooltip=tooltip19,
              icon=logoIconPark2).add_to(m),
folium.Marker([45.75151746880004, 21.22894679008122],
              popup=popup23,
              tooltip=tooltip20,
              icon=logoIconPark3).add_to(m),
folium.Marker([45.752033,21.2333900],
              popup=popup25,
              tooltip=tooltip21,
              icon=logoIconPark4).add_to(m),
folium.Marker([45.7529012, 21.2207699],
              popup=popup26,
              tooltip=tooltip22,
              icon=logoIconPark5).add_to(m),
folium.Marker([45.760199099999994,21.22484718178763],
              popup=popup24,
              tooltip=tooltip23,
              icon=logoIconPark6).add_to(m),

#Monuments
folium.Marker([45.75114316856265, 21.22112107359635],
              popup=popup2,
              tooltip=tooltip24,
              icon=logoIconMonument1).add_to(m),
folium.Marker([45.752585415704985, 21.225324374674834],
              popup=popup3,
              tooltip=tooltip25,
              icon=logoIconMonument2).add_to(m),
folium.Marker([45.757960252002604, 21.22908268767883],
              popup=popup4,
              tooltip=tooltip26,
              icon=logoIconMonument3).add_to(m),
folium.Marker([45.74915521908834, 21.218918125125253],
              popup=popup5,
              tooltip=tooltip27,
              icon=logoIconMonument4).add_to(m),





#Monuments





#generate map
m.save('map.html')
