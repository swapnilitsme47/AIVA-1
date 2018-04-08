import speech_recognition as sr
from gtts import gTTS
import os
from weather import Weather
from googleplaces import GooglePlaces, types, lang
import googlemaps
import geocoder
import wolframalpha
import wikipedia

API_KEY= 'AIzaSyAG-kguNoHCCQDME4L3xTd0IivBgnt2J84'

google_places= GooglePlaces(API_KEY)


sample_rate=48000
chunk_size=2048

r=sr.Recognizer()



repeat =1
while(repeat == 1):
    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        
        print "Say something"
        audio = r.listen(source)
        print "Done !"

        try:
            text = r.recognize_google(audio)
            print text
            if "your name" in text:
                
                print "My name is Jessica, How can I help you"
                speechtext="I am Jessica, How can I help you ?"
                tts=gTTS(text=speechtext, lang='en', slow=False)
                tts.save("one.mp3")
                os.system("mpg321 one.mp3")

            

            if "weather" in text:
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    r2.adjust_for_ambient_noise(source)
                    print("Please say a city name")
                    audio2=r2.listen(source)
                    text2 =r2.recognize_google(audio2)
                    print text2
                    print "Done !"

                    try:
                        weather=Weather()
                        location = weather.lookup_by_location(text2)
                        condition = location.condition()
                        hepburn = condition.text()
                        speechtext="The weather in"+text2+"is"+hepburn   
                        tts=gTTS(text=speechtext, lang='en', slow=False)
                        tts.save("one.mp3")
                        os.system("mpg321 one.mp3")
                    except sr.UnknownValueError:
                        print("Unable fuck")
                    except sr.RequestError as e:
                        print("could not request results from google")


            if "coffee" in text:
                speechtext="Here are the nearest coffee shops"
                tts=gTTS(text=speechtext, lang='en', slow=False)
                tts.save("one.mp3")
                os.system("mpg321 one.mp3")
                query_result = google_places.nearby_search(lat_lng = {'lat':34.083656, 'lng':74.797371}, keyword='Coffee Shops', radius=5000, types=[types.TYPE_FOOD])
                if query_result.has_attributions:
                    print query_result.html_attributions

                for place in query_result.places:
                    print place.name
                    place.get_details()
                    print place.place_id

            if "restaurants" in text:
                speechtext="Here are the nearest restaurants"
                tts=gTTS(text=speechtext, lang='en', slow=False)
                tts.save("one.mp3")
                os.system("mpg321 one.mp3")
                query_result = google_places.nearby_search(lat_lng = {'lat':34.083656, 'lng':74.797371}, keyword='restaurants', radius=5000, types=[types.TYPE_FOOD])
                if query_result.has_attributions:
                    print query_result.html_attributions

                for place in query_result.places:
                    print place.name
                    place.get_details()
                    print place.place_id

            else:
                try:
                    input = text
                    app_id="Q8H27P-UUP3WY98PK"
                    client=wolframalpha.Client(app_id)
                    res=client.query(input)
                    answer= next(res.results).text
                    tts=gTTS(text = answer, lang='en', slow= False)
                    tts.save("one.mp3")
                    os.system("mpg321 one.mp3")
                    print answer
                    
                except:
                    article= wikipedia.summary(input, sentences=2)
                    print article
                    tts=gTTS(text= article, lang='en',slow= False)
                    tts.save("one.mp3")
                    os.system("mpg321 one.mp3")
                
                    
            
                        
        except sr.UnknownValueError:
            print("Unable to understand audio sir")

        except sr.RequestError as e:
            print("Could not request results from google")



    

