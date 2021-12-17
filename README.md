# Page by Page summarizer of pdf Files

This is an automatic bot based on python tools and quilbot. It accepts pdf file as an input and provides summary of the whole pdf


# Installing Tools:

# Page by Page summarizer of pdf Files

This is an automatic bot based on python tools and quilbot. It accepts pdf file as an input and provides summary of the whole pdf


# Installing Tools:

We’ll need to install a couple things:

1. Selenium, which allows you to control browsers from Python
2. ChromeDriver, which allows software to control Chrome (like Selenium!)





### **Installing ChromeDriver**

#### STEP ONE: Downloading ChromeDriver

First, download ChromeDriver from its terribly ugly site. It looks like a scam or like it was put together by a 12 year old, but I promise it’s good and cool and nice.

You’ll want chromedriver_win32.zip. That link should download 2.40, but if you want something more recent just go to the page and download the right thing.

#### STEP TWO: Unzipping ChromeDriver

Extract chromedriver_win32.zip and it will give you a file called chromedriver.exe. This is the magic software!

#### STEP THREE: Moving ChromeDriver somewhere sensible

Now we need to move ChromeDriver somewhere that Python and Selenium will be able to find it (a.k.a. in your PATH).

The easiest place to put it is in C:\Windows. So move it there!

If you can’t move chromedriver there, you can always just tell Python where it is when you’re loading it up. See Selenium snippets under “But Python can’t find chromedriver”

## Installing Selenium

If you google about Selenium, a lot of the time you see things about “Selenium server” and blah blah blah - you don’t need that, you aren’t running a huge complex of automated browser testing machines. You don’t need that. We just need plain ol’ Selenium.

Let’s use pip3 to install Selenium for Python 3.

```python
pip install selenium
```



### Installing Chrome

Oh, you also need to make sure you have Chrome (or Firefox) installed and it lives in one of the normal places applications do.

If Python can’t find Chrome/Firefox, you can always just tell Python where it is when you’re loading it up. See Selenium snippets under “But Python can’t find Chrome/Firefox”

### Test it

Want to make sure it works? Run the following to pull all of the headlines from the New York Times homepage.

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())
```







## Running Algorithm:



### Specify the pdf file path:

```python
pdfFileObj = open('JFQ-68_99-104_Stejskal.pdf', 'rb') #give the file path of pdf
```

### Hit RUN:

Hit run and you're good to go.
Web browser will open which will autofill and summarize text page by page from pdf.

You will get your results.
![image](https://user-images.githubusercontent.com/45047495/146603779-407632a9-3a1e-4cc6-9ffd-93660b2f9eb4.png)
