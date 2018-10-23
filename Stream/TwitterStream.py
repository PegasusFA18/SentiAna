import tweepy
import webbrowser
import ProcessCompanyKeywords as ProcessKeywords
from StoreDetails import save_dill, load_dill


tweets = []


class Streamer(tweepy.StreamListener):

    def on_connect(self):
        print("Connection established!!")

    def on_disconnect(self, notice):
        print("Connection ended :(")
        print(notice)

    def on_error(self, status_code):
        print('error notice')
        print(status_code)

    def on_warning(self, notice):
        print('warning notice')
        print(notice)

    def on_limit(self, status):
        print('on limit')
        print(status)

    def on_status(self, status):
        #handle status
        if should_track(keyword_list, status):
            try:
                0
                print(status.text)
            except:
                None





def should_track(keywords, status):
    text = status.text.lower()

    if 'rt' in text:
        return False
    elif keywords_in_text(keywords, text):
        return True
    else:
        return False

def keywords_in_text(keywords, text):
    for keyword in keywords:
        if keyword.lower() in text:
            return True
    return False





def authenticate_with_tokens(access_token, access_secret, consumer_key, consumer_secret):
    try:
        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        return api
    except Exception as error:
        print(error)
        return error




def authenticate_with_browser(consumer_key, consumer_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        url = auth.get_authorization_url(signin_with_twitter=True)
        print(url)
        webbrowser.open(url)
        pin = input('Verification pin number from twitter.com: ').strip()
        auth.get_access_token(verifier=pin)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        api.verify_credentials()

        return api

    except Exception as error:
        print(error)
        return error




def login(api_file_name='cached_api.dl'):
    consumer_key = 'gdbs2XKFHWuJYaUXMDlaXUYhh'
    consumer_secret = 'e42si7oOZbacjHow01vNWdyaFHLIGUW1hks8DK1PlQd11z88ey'

    cached_api = load_dill(api_file_name)

    if cached_api:
        return cached_api
    else:
        api = authenticate_with_browser(consumer_key, consumer_secret)
        save_dill(api, api_file_name)
        return api




def create_stream(api, keywords):
    stream = tweepy.Stream(api.auth, Streamer())
    stream.filter(track=keywords, async=True, stall_warnings=True, languages=['en'])




api = login()
# list_of_companies = ProcessKeywords.load_companies_from_file('keywords.txt')

keyword_list = []

keyword_list.extend(ProcessKeywords.find_company('nike').keywords)
keyword_list.extend(ProcessKeywords.find_company('apple').keywords)
keyword_list.extend(ProcessKeywords.find_company('tesla').keywords)
keyword_list.extend(ProcessKeywords.find_company('netflix').keywords)
keyword_list.extend(ProcessKeywords.find_company('google').keywords)


create_stream(api, keyword_list)
# print(company_to_track.keywords)