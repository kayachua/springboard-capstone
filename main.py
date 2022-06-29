import os, argparse
#import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, pipeline
from transformers.utils import logging

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.set_verbosity_error()

# tf.keras.backend.clear_session()

#physical_devices = tf.config.list_physical_devices('GPU')
#for device in physical_devices:
#    tf.config.experimental.set_memory_growth(device, True)

tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base")

bertweet_stock_tweet = TFAutoModelForSequenceClassification.from_pretrained(
    "./models/bertweet_stock_tweet/",
    num_labels=3,
    id2label={0: 'NEGATIVE', 1: 'NEUTRAL', 2: 'POSITIVE'})

sentiment_eval = pipeline(task='sentiment-analysis', model=bertweet_stock_tweet, tokenizer=tokenizer)

# parser = argparse.ArgumentParser(description='Stock Tweet Sentiment Classifier')
# parser.add_argument('tweet', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))



# with open('test.txt') as f:
#     x = f.readlines()
#     f.close()

# print(sentiment_eval(x))

print("\n  Stock Tweet Sentiment Classifier\n")

continue_loop = True
while continue_loop:
    text = input("Please enter tweet (or type 'exit'):")
    if text.strip().casefold() == 'exit':
        continue_loop = False
    else:
        result = sentiment_eval(text)
        # result
        print(f"\n  Predicted Sentiment: {result[0]['label']}")
        print(f"  Score:               {result[0]['score']}\n")
