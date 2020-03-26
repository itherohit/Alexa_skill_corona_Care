import requests
# import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"


def build_speechlet_response(title, speech, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': speech
        },
        'card': {
            'type': 'Standard',
            'title': title
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def WhatIsCorona():
    session_attributes = {}
    card_title = "What is Corona ?"
    speech_output = "<speak>" \
                    "Coronaviruses are a large family of viruses, which may cause illness in animals, or humans. " \
                    "In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases, such as Middle East Respiratory Syndrome (MERS) " \
                    "and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19." \
                    "</speak>"
    reprompt_text = "Anything else?. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def WhatIsCovid():
    session_attributes = {}
    card_title = "What is Corona ?"
    speech_output = "<speak>" \
                    "COVID-19 is the infectious disease, caused by the most recently discovered coronavirus. " \
                    "This new virus, and disease were unknown before the outbreak began in Wuhan, China, in December 2019. " \
                    "</speak>"
    reprompt_text = "you can try some corona songs."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Symptoms():
    session_attributes = {}
    card_title = "SYMPTOMS"
    speech_output = "<speak>" \
                    "The most common symptoms of COVID-19 are fever, tiredness, and dry cough. " \
                    "Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing. " \
                    "Older people, and those with underlying medical problems like high blood pressure, heart problems or diabetes, " \
                    "are more likely to develop serious illness. People with fever, cough and difficulty breathing should seek medical attention. " \
                    "</speak>"
    reprompt_text = "Ask about the total corona cases in the world."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Spread():
    session_attributes = {}
    card_title = "How corona Spreads?"
    speech_output = "<speak>" \
                    "People can catch COVID-19 from others who have the virus. " \
                    "The disease can spread from person to person through small droplets from the nose " \
                    "or mouth, which are spread when a person with COVID-19 coughs or exhales. " \
                    "These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by " \
                    "touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch COVID-19 " \
                    "if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. " \
                    "This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick." \
                    "</speak>"
    reprompt_text = "Ask something about the total corona cases."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def AirSpread():
    session_attributes = {}
    card_title = "Can it spread through Air?"
    speech_output = "<speak>" \
                    "Studies to date suggest that, the virus that causes COVID-19 is mainly " \
                    "transmitted through contact with respiratory droplets, rather than through the air." \
                    "</speak>"
    reprompt_text = "Ask something else."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def NoSymptomSpread():
    session_attributes = {}
    card_title = "Can it spread through a person who has no symptoms?"
    speech_output = "<speak>" \
                    "The risk of catching COVID-19, from someone with no symptoms at all is very low. " \
                    "However, many people with COVID-19 experience only mild symptoms. " \
                    "This is particularly true at the early stages of the disease. " \
                    "</speak>"
    reprompt_text = "you can do risk check for corona."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Prevention():
    session_attributes = {}
    card_title = "Prevention"
    speech_output = "<speak>" \
                    "You can reduce your chances of being infected or spreading COVID-19 by taking some simple precautions. " \
                    "clean your hands regularly and thoroughly with an alcohol-based hand rub. " \
                    "Maintain at least 1 metre distance between yourself and anyone. " \
                    "Avoid touching eyes, nose and mouth. " \
                    "Stay home if you feel unwell. " \
                    "and finally, avoid traveling to places. " \
                    "</speak>"
    reprompt_text = "Try Knowing the corona cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def CatchCovid():
    session_attributes = {}
    card_title = "Will You get COVID-19 ?"
    speech_output = "<speak>" \
                    "The risk depends on where you  are, and more specifically, whether there is a COVID-19 outbreak unfolding there. " \
                    "For most people in most locations, the risk of catching COVID-19 is still low. " \
                    "</speak>"
    reprompt_text = "try to knonw the corona death cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def WorryCovid():
    session_attributes = {}
    card_title = "Will You get COVID-19 ?"
    speech_output = "<speak>" \
                    "Illness due to COVID-19 infection is generally mild, especially for children and young adults. " \
                    "However, it can cause serious illness, about 1 in every 5 people who catch it need hospital care. " \
                    "It is therefore quite normal for people to worry about how the COVID-19 outbreak will affect them and their loved ones. " \
                    "</speak>"
    reprompt_text = "Try Knowing the corona  recovered cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def WhoHighRisk():
    session_attributes = {}
    card_title = "High Risk?"
    speech_output = "<speak>" \
                    "While we are still learning about how COVID-19 affects people, " \
                    "older persons and persons with pre-existing medical conditions such as high blood pressure, " \
                    "heart disease, lung disease, cancer or diabetes, appear to develop serious illness more often than others.  " \
                    "</speak>"
    reprompt_text = "Try Knowing the corona cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def AntiEffect():
    session_attributes = {}
    card_title = "Antibiotics for COVID-19 ?"
    speech_output = "<speak>" \
                    "No. Antibiotics do not work against viruses, they only work on bacterial infections. " \
                    "COVID-19 is caused by a virus, so antibiotics do not work.  " \
                    "</speak>"
    reprompt_text = "get information about any country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def MedPrevent():
    session_attributes = {}
    card_title = "Medicines will cure corona?"
    speech_output = "<speak>" \
                    "While some western, traditional or home remedies may provide comfort and alleviate symptoms of COVID-19, " \
                    "there is no evidence that current medicine can prevent or cure the disease.  " \
                    "</speak>"
    reprompt_text = "get information about any country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def WearMask():
    session_attributes = {}
    card_title = "MASK for Corona?"
    speech_output = "<speak>" \
                    "Only wear a mask if you are ill with COVID-19 symptoms, " \
                    "especially coughing, or looking after someone who may have COVID-19. Disposable face mask can only be used once. " \
                    "</speak>"
    reprompt_text = "get information about any country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def IsVaccine():
    session_attributes = {}
    card_title = "Medicines will cure corona?"
    speech_output = "<speak>" \
                    "Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-19. " \
                    "Possible vaccines and some specific drug treatments are under investigation. " \
                    "</speak>"
    reprompt_text = "Try Knowing the corona cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Isolation():
    session_attributes = {}
    card_title = "Incubation OR Isolation Period"
    speech_output = "<speak>" \
                    "The incubation, or Isolation Period means, the time between catching the virus and beginning to have symptoms of the disease. " \
                    "Most estimates of the incubation period for COVID-19 range from 1-14 days, most commonly around five days." \
                    "</speak>"
    reprompt_text = "Hear some corona songs."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def AnimalSource():
    session_attributes = {}
    card_title = "Can I get infected from Animals ? "
    speech_output = "<speak>" \
                    "Possible animal sources of COVID-19 have not yet been confirmed. " \
                    "To protect yourself, avoid direct contact with animals and surfaces in contact with animals." \
                    "</speak>"
    reprompt_text = "Check you risk."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def PetCovid():
    session_attributes = {}
    card_title = "Can I get infected by my Pet? "
    speech_output = "<speak>" \
                    "While there has been one instance of a dog being infected in Hong Kong, to date, " \
                    "there is no evidence that a dog, cat or any pet can transmit COVID-19. " \
                    "</speak>"
    reprompt_text = "check your risk."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def VirusSurvive():
    session_attributes = {}
    card_title = "Can I get infected by my Pet? "
    speech_output = "<speak>" \
                    "It is not certain how long the virus that causes COVID-19 survives on surfaces, " \
                    "but it seems to behave like other coronaviruses. Studies suggest that coronaviruses including preliminary " \
                    "information on the COVID-19 virus, may persist on surfaces for a few hours or up to several days. " \
                    "</speak>"
    reprompt_text = "Try Knowing the corona cases count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def TotalCases():
    session_attributes = {}
    card_title = "Total CORONA Cases"
    if (data.tcases == 0):
        speech_output = "<speak>As per the internet, around {} people are affected by corona virus.</speak>".format(
            data.Total)
        data.tcases = 1
    else:
        speech_output = "<speak>As of now, there are {} people affected by corona virus.</speak>".format(data.Total)
    reprompt_text = "Try Knowing the death cases or know about your country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def DeathCases():
    session_attributes = {}
    card_title = "Total CORONA DEATH Cases"
    if (data.dcases == 0):
        speech_output = "<speak>As per the internet, around {} people are dead by corona virus.</speak>".format(
            data.Death)
        data.dcases = 1
    else:
        speech_output = "<speak>Till now, we have lost {} lives due to corona virus.</speak>".format(data.Death)
    reprompt_text = "Try to know the recovery count."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def RecoveryCases():
    session_attributes = {}
    card_title = "Total Recovered Cases"
    if (data.rcases == 0):
        speech_output = "<speak>As per the internet, around {} people are recovered from corona virus.</speak>".format(
            data.Recovered)
        data.rcases = 1
    else:
        speech_output = "<speak>Till now, around {} people got recovered from corona infection.</speak>".format(
            data.Recovered)
    reprompt_text = "Try to know the details of your country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def CountryInfo(intent, session):
    session_attributes = {}
    card_title = "Country Information"
    country_name = intent['slots']['country']['value']
    index = data.countries.index(country_name.lower())
    total_cases = data.cTotal_cases[index].strip()
    new_cases = data.cNew_cases[index][1:].strip()
    death_cases = data.cDeaths[index].strip()
    critical_cases = data.cCritical[index].strip()
    recovered_cases = data.cRecovered[index].strip()
    if (new_cases == "" and death_cases != "" and critical_cases != "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases but with {} deaths and {} critical cases. Around {} people got recovered.</speak>".format(
            country_name, total_cases, death_cases, critical_cases, recovered_cases)
    elif (new_cases != "" and death_cases == "" and critical_cases != "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, and {} critical cases. {} has no death cases, and Around {} people got recovered.</speak>".format(
            country_name, total_cases, new_cases, critical_cases, country_name, recovered_cases)
    elif (new_cases != "" and death_cases != "" and critical_cases == "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, and {} deaths. with no critical cases, around {} people got recovered.</speak>".format(
            country_name, total_cases, new_cases, death_cases, recovered_cases)
    elif (new_cases != "" and death_cases != "" and critical_cases != "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, and {} deaths, with {} critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, new_cases, death_cases, critical_cases)
    elif (new_cases == "" and death_cases == "" and critical_cases != "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases and zero deaths. with {} critical cases, around {} people got recovered.</speak>".format(
            country_name, total_cases, critical_cases, recovered_cases)
    elif (new_cases == "" and death_cases != "" and critical_cases == "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases, and critical cases. with {} death cases, Around {} people got recovered.</speak>".format(
            country_name, total_cases, death_cases, recovered_cases)
    elif (new_cases == "" and death_cases != "" and critical_cases != "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases, but with {} deaths and {} critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, death_cases, critical_cases)
    elif (new_cases != "" and death_cases == "" and critical_cases == "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, with zero deaths, and zero critical cases. Around {} people got recovered.</speak>".format(
            country_name, total_cases, new_cases, recovered_cases)
    elif (new_cases != "" and death_cases == "" and critical_cases != "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, with zero deaths, and {} critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, new_cases, critical_cases)
    elif (new_cases != "" and death_cases != "" and critical_cases == "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, and {} deaths, with zero critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, new_cases, death_cases)
    elif (new_cases != "" and death_cases == "" and critical_cases == "" and recovered_cases == ""):
        speech_output = "<speak> {} has around {} people affected by corona virus, in which we have {} new cases, with zero deaths and zero critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, new_cases)
    elif (new_cases == "" and death_cases != "" and critical_cases == "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases, but with {} deaths. with zero critical cases and no one got recovered.</speak>".format(
            country_name, total_cases, death_cases)
    elif (new_cases == "" and death_cases == "" and critical_cases == "" and recovered_cases != ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with zero new cases, deaths, and critical cases. Happily {} got recovered.</speak>".format(
            country_name, total_cases, recovered_cases)
    elif (new_cases == "" and death_cases == "" and critical_cases != "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with zero new cases, and deaths. {} has {} critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases, country_name, critical_cases)
    elif (new_cases == "" and death_cases == "" and critical_cases == "" and recovered_cases == ""):
        speech_output = "<speak>{} has around {} people affected by corona virus, with no new cases, deaths, and critical cases. sadly no one got recovered.</speak>".format(
            country_name, total_cases)
    else:
        speech_output = "<speak>{} has around {} people affected by corona virus, in which we have {} new cases, and {} deaths, with {} critical cases. Happily, around {} people got recovered.</speak>".format(
            country_name, total_cases, new_cases, death_cases, critical_cases, recovered_cases)
    reprompt_text = "Try checking your risk."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def CheckRisk():
    session_attributes = {}
    card_title = "CHECK YOUR RISK"
    if (data.risk_no == 0):
        speech_output = "<speak>Answer the following questions to calculate your risk. <break time='1s'/>" \
                        "Do you have cough? </speak>"
    elif (data.risk_no == 1):
        speech_output = "<speak>Do you have cold? </speak>"
    elif (data.risk_no == 2):
        speech_output = "<speak>Do you have sore throat?</speak>"
    elif (data.risk_no == 3):
        speech_output = "<speak>Do you have a headache?</speak>"
    elif (data.risk_no == 4):
        speech_output = "<speak>Are you having Diarrhea?</speak>"
    elif (data.risk_no == 5):
        speech_output = "<speak>Are you experiencing body pain?</speak>"
    elif (data.risk_no == 6):
        speech_output = "<speak>Do you have fever? </speak>"
    elif (data.risk_no == 7):
        speech_output = "<speak>Are you having difficulty in breathing? </speak>"
    elif (data.risk_no == 8):
        speech_output = "<speak>Are you experiencing fatigue? </speak>"
    elif (data.risk_no == 9):
        speech_output = "<speak>have you traveled recently in the past fourteen days? </speak>"
    elif (data.risk_no == 10):
        speech_output = "<speak>Do you have a travel history to a covid-19 infected area?</speak>"
    elif (data.risk_no == 11):
        speech_output = "<speak>Do you have direct contact with a positive covid-19 patient? </speak>"
    else:
        if (data.score == 0):
            speech_output = "<speak>Your risk score is zero. you can enjoy yourself, but be safe. you dont have to worry about corona. </speak>"
        elif (data.score < 3):
            speech_output = "<speak>Your risk score is {}. it might be due to stress. you dont have to worry about corona. </speak>".format(
                data.score)
        elif (data.score < 6):
            speech_output = "<speak>Your risk score is {}. Hydrate properly, take care of your personal hygiene. observe and re-check after two days.</speak>".format(
                data.score)
        elif (data.score < 13):
            speech_output = "<speak>Your risk score is {}. It is adviced that you consult a doctor as soon as possible and stay hydrated, and hygiene. </speak>".format(
                data.score)
        elif (data.score < 25):
            speech_output = "<speak>Your risk score is {}. please isolate yourself from others. consult a doctor immediately and also call the hotline number. </speak>".format(
                data.score)
    reprompt_text = "Bored? Try some corona songs."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def YesIntent():
    data.risk_no = data.risk_no + 1
    if (data.risk_no < 7):
        data.score = data.score + 1
    elif (data.risk_no < 9):
        data.score = data.score + 2
    else:
        data.score = data.score + 3
    return CheckRisk()


def NoIntent():
    data.risk_no = data.risk_no + 1
    return CheckRisk()


def SongIntent():
    session_attributes = {}
    card_title = "Corona Song"
    if (data.song_no == 0):
        speech_output = "<speak>" \
                        "A song by Anup. " \
                        "<audio src='https://alexaskillcoronacare.s3-ap-northeast-1.amazonaws.com/GO+CORONA.mp3'/>" \
                        "</speak>"
        data.song_no = 1
    elif (data.song_no == 1):
        speech_output = "<speak>" \
                        "A song by Jason chen. " \
                        "<audio src='https://alexaskillcoronacare.s3-ap-northeast-1.amazonaws.com/Washing+Hand+Corona+Song+(Ghen+C%C3%B4+Vy)+-+English+Version.mp3'/>" \
                        "</speak>"
        data.song_no = 2
    elif (data.song_no == 2):
        speech_output = "<speak>" \
                        "A song by broke vibes. " \
                        "<audio src='https://alexaskillcoronacare.s3-ap-northeast-1.amazonaws.com/Dance+Monkey+parody+Corona.mp3'/>" \
                        "</speak>"
        data.song_no = 3
    elif (data.song_no == 3):
        data.song_no = 4
        speech_output = "<speak>" \
                        "A song from mirchi kolkata. " \
                        "<audio src='https://alexaskillcoronacare.s3-ap-northeast-1.amazonaws.com/CORONA+Parody+Feat.+Mirchi+Somak+%26+Mirchi+Agni.mp3'/>" \
                        "</speak>"
    else:
        data.song_no = 0
        speech_output = "<speak>" \
                        "A tamil song by mirchi anand and team. " \
                        "<audio src='https://alexaskillcoronacare.s3-ap-northeast-1.amazonaws.com/Kutty+story+corona+song.mp3'/>" \
                        "</speak>"
    reprompt_text = "Try to Know the corona case count, or know about your country."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    session_attributes = {}
    card_title = "CORONA CARE"
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        table_data = soup.find_all(class_='maincounter-number')
        data.Total = table_data[0].get_text()
        data.Death = table_data[1].get_text()
        data.Recovered = table_data[2].get_text()
        chtml = requests.get(url + "#countries")
        csoup = BeautifulSoup(chtml.content, "html.parser")
        ctable = csoup.find(id='main_table_countries_today')
        tr = ctable.find_all('tr')
        data.cdata = []
        data.countries = []
        data.cTotal_cases = []
        data.cNew_cases = []
        data.cDeaths = []
        data.cRecovered = []
        data.cCritical = []
        for i in range(1, len(tr) - 1):
            td = tr[i].find_all('td')
            for i in range(0, 8):
                data.cdata.append(td[i].get_text())
        i = 0
        while (i < (len(tr) - 2) * 8):
            data.countries.append(data.cdata[i].lower())
            data.cTotal_cases.append(data.cdata[i + 1])
            data.cNew_cases.append(data.cdata[i + 2])
            data.cDeaths.append(data.cdata[i + 3])
            data.cRecovered.append(data.cdata[i + 5])
            data.cCritical.append(data.cdata[i + 7])
            if (data.cdata[i].lower() == "usa"):
                data.countries.append("united states")
                data.cTotal_cases.append(data.cdata[i + 1])
                data.cNew_cases.append(data.cdata[i + 2])
                data.cDeaths.append(data.cdata[i + 3])
                data.cRecovered.append(data.cdata[i + 5])
                data.cCritical.append(data.cdata[i + 7])
            if (data.cdata[i].lower() == "uk"):
                data.countries.append("united kingdom")
                data.cTotal_cases.append(data.cdata[i + 1])
                data.cNew_cases.append(data.cdata[i + 2])
                data.cDeaths.append(data.cdata[i + 3])
                data.cRecovered.append(data.cdata[i + 5])
                data.cCritical.append(data.cdata[i + 7])
            if (data.cdata[i].lower() == "s. korea"):
                data.countries.append("south korea")
                data.cTotal_cases.append(data.cdata[i + 1])
                data.cNew_cases.append(data.cdata[i + 2])
                data.cDeaths.append(data.cdata[i + 3])
                data.cRecovered.append(data.cdata[i + 5])
                data.cCritical.append(data.cdata[i + 7])
            if (data.cdata[i].lower() == "uae"):
                data.countries.append("united arab emirates")
                data.cTotal_cases.append(data.cdata[i + 1])
                data.cNew_cases.append(data.cdata[i + 2])
                data.cDeaths.append(data.cdata[i + 3])
                data.cRecovered.append(data.cdata[i + 5])
                data.cCritical.append(data.cdata[i + 7])
            i = i + 8
        if (data.welcome_no == 0):
            speech_output = "<speak>" \
                            "welcome to corona care. corona care is created to give you clarification, and additional information " \
                            "about corona. You can ask any questions related to corona, or even you can also get information about the total number of " \
                            "corona cases, deaths, and recovered cases. Get a detailed information about any country related to corona. You can also do a risk check for corona. " \
                            "and the cool thing is, you can hear some cool corona songs. To exit, just say, Thank you." \
                            "</speak>"
            data.welcome_no = 1
        else:
            speech_output = "<speak>" \
                            "welcome back. you can ask anything related to corona or you can also get information about the total number of " \
                            "corona cases, deaths, and recovered cases. Get a detailed information about any country related to corona. You can also do a risk check for corona. " \
                            "and the cool thing is, you can hear some cool corona songs. To exit, just say, Thank you." \
                            "</speak>"
        should_end_session = False
    except:
        speech_output = "<speak>There is a problem with your internet connection. please reconnect and check for total cases.</speak>"
        should_end_session = True
    reprompt_text = "Ask me something about corona. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


class data:
    welcome_no = 0
    tcases = 0
    dcases = 0
    rcases = 0
    Total = ""
    Death = ""
    Recovered = ""
    cdata = []
    countries = []
    cTotal_cases = []
    cNew_cases = []
    cDeaths = []
    cRecovered = []
    cCritical = []
    score = 0
    risk_no = 0
    song_no = 0


def handle_session_end_request():
    card_title = "THANK YOU"
    speech_output = "<speak>" \
                    "Thank you. hope corona care gave you useful information about corona. please share this with your friends and family to spread awareness. be safe and hygiene." \
                    "</speak>"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def invalid():
    card_title = "INVALID"
    session_attributes = {}
    should_end_session = False
    speech_output = "<speak>sorry i could not recognize that.</speak>"
    reprompt_text = "Ask me something else. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    # Dispatch to your skill's intent handlers
    if intent_name == "WhatIsCorona":
        return WhatIsCorona()
    elif intent_name == "WhatIsCovid":
        return WhatIsCovid()
    elif intent_name == "Symptoms":
        return Symptoms()
    elif intent_name == "Spread":
        return Spread()
    elif intent_name == "AirSpread":
        return AirSpread()
    elif intent_name == "NoSymptomSpread":
        return NoSymptomSpread()
    elif intent_name == "Prevention":
        return Prevention()
    elif intent_name == "CatchCovid":
        return CatchCovid()
    elif intent_name == "WorryCovid":
        return WorryCovid()
    elif intent_name == "WhoHighRisk":
        return WhoHighRisk()
    elif intent_name == "AntiEffect":
        return AntiEffect()
    elif intent_name == "MedPrevent":
        return MedPrevent()
    elif intent_name == "IsVaccine":
        return IsVaccine()
    elif intent_name == "WearMask":
        return WearMask()
    elif intent_name == "Isolation":
        return Isolation()
    elif intent_name == "AnimalSource":
        return AnimalSource()
    elif intent_name == "PetCovid":
        return PetCovid()
    elif intent_name == "VirusSurvive":
        return VirusSurvive()
    elif intent_name == "TotalCases":
        return TotalCases()
    elif intent_name == "DeathCases":
        return DeathCases()
    elif intent_name == "RecoveryCases":
        return RecoveryCases()
    elif intent_name == "CountryInfo":
        return CountryInfo(intent, session)
    elif intent_name == "CheckRisk":
        data.risk_no = 0
        data.score = 0
        return CheckRisk()
    elif intent_name == "YesIntent":
        return YesIntent()
    elif intent_name == "NoIntent":
        return NoIntent()
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_end_request()
    elif intent_name == "SongIntent":
        return SongIntent()
    else:
        return invalid()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

