import configparser
import openai


# more info: https://github.com/openai/openai-python
config = configparser.ConfigParser()
config.read('config.ini')
openai.organization = config.get('API', 'ORG_ID')
openai.api_key = config.get('API', 'OPENAI_API_KEY')


test = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    messages = [{"role" : "user", "content" : "What is the capital of Hungary?"}]
)

print(test)