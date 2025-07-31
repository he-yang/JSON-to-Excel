# 3. Excel Add-in (JSON-to-Excel Excel Add-in)

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/ExcelAddIn.html)

JSON-to-Excel by WTSolutions is a series of tools which can convert JSON to Excel, both Flat and Nested JSON can be converted to Excel. It offers a full-scenario solution for "Converting JSON to Excel", including Excel add-ins, web applications:

* [Web App: Convert JSON to Excel directly in Web Browser.](WebApp.md)
* <mark>Excel add-in: Convert JSON to Excel in Excel, works with Excel environment seamlessly.</mark>(<-- You are here)



## 3.1 Requirements

* Excel 2013 Service Pack 1 or later, 
* Excel 2016 for Mac, 
* Excel 2016 or later, 
* Excel Online, 
* Office 365 etc.


## 3.2 Access

* Open a new datasheet in Excel 2013/2016 or Excel Online or Office 365.
* **Home** Tab or **Insert** Tab > Add-ins
* In the search box, type in "JSON to Excel"
* Follow the instructions on the screen to install the add-in, and you will see an button "Convert" with JSON-to-Excel logo added to your **Home** Tab.
* **Home** Tab > JSON to Excel > Convert
* Now you are ready to use this add-in.


### Video Guide to Get add-in
<iframe width="560" height="315" src="https://www.youtube.com/embed/U3uQQ9i6IGs?si=kZFaGT89tT3wk21C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



## 3.3 Usage

* Prepare your JSON data
* In the [Conversion Settings](profeatures.md), select conversion mode etc.
* Load your JSON data (Choose one of the following two ways)
    1. Copy and Paste your JSON data in the text area, or
    2. Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing [Pro Features](pricing.md), max 20 files can be loaded at once.
* Click on Go button
* Your JSON data will be converted to Excel, and you can find one newly added sheet to your Excel.

### Video Guide to Use add-in (side-load in Excel)

<iframe width="560" height="315" src="https://www.youtube.com/embed/nn3AIptQ-p8?si=4DSrC5wog7yEmPyO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 3.4 JSON Data and Conversion Settings

Refer to [JSON Data and Conversion Settings](profeatures.md) for more details.


## 3.5 Limitations
- Maximum 1000 objects (rows) per conversion
- Maximum 100 unique properties (columns) per dataset
- Arrays in values will be converted to strings in Excel
- Maximum 20 loaded local JSON files can be converted at once [Pro Feature](pricing.md)