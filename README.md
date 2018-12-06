# BehavioralCoding CS410Project
Psychological behavioral coding toolbox

## Author
ciciling netID: ling10
## 
This toolbox is the project of cs 410 UIUC. It is used to help psychologists to conduct behavioral coding analysis. By using this toolbox, we recognize the text of dialog in the video, then match the coding code and give the suggestion.

## 1. Installation

Please install ffmpeg before you go on.
#### Step 1: FFmpeg package
on OSX
~~~
brew install ffmpeg
~~~
on Ubuntu
~~~
sudo apt install ffmpeg
~~~
on Windows
download ffmpeg windows build: https://ffmpeg.zeranoe.com/builds/ and extract it.



#### Step 2: Python package
~~~{.python}
pip install baidu-aip # Baidu AIP service
pip install thulac # THU Lexical Analyzer for Chinese
pip install metapy # Meta analysis for English
pip install jieba # 
pip install snowNLP # sentimental analysis pretrained model
~~~

#### Step3: Clone this project to the local machine



## 2. Usage

#### Step1: Download test video

You can use your own video. We can't publish our test video because it is under protection.

#### Step2:

##### File-> load video 
Load the video and process it. generate a few textbox.
##### File -> load processed data
Load the preprocessed data.

#### Methods
Edit -> Save

##### Analysis -> match words 
We use words in the “words_set_file” as a dictionary to match all the words in the text. Then we show the results in the following textbox.

##### Analysis -> search words 
Example: we search the word “mood”, then we get the results.


##### Analysis -> sentimental analysis 
Our semtimental analysis is based on a pre-trained model because there is not enough data
in this field.
The model is based on Bayesian predictive model:
1. firstly, filter the stop words and use n-gram model to label the sentence.
2. secondly, used pretrained Bayesian model to get the results.
