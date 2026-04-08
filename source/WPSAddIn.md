# WPS Add-in (JSON-to-Excel WPS Add-in)

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/WPSAddIn.html)


JSON-to-Excel by WTSolutions is a toolkit of tools which can convert JSON to Excel, both Flat and Nested JSON can be converted to Excel. It offers a full-scenario solution for "Converting JSON to Excel", including Excel add-ins, WPS add-ins, web applications, API service and MCP service.

 * Web Based Solutions
      * [Web App: Convert JSON to Excel directly in Web Browser.](WebApp.md)
      * [Excel add-in: Convert JSON to Excel in Excel, works with Excel environment seamlessly.](ExcelAddIn.md) 
      * <mark> WPS add-in: Convert JSON to Excel in WPS, works with WPS environment seamlessly. </mark> (<-- You are here)
      * [API: Convert JSON to Excel in API by HTTPS POST request](API.md)
 * Localized Solutions
      * [Localized MCP Server: Convert JSON to Excel in MCP Server](MCP.md)
      * Localized App, Coming soon.
      * Localized Excel Add-in, Coming soon.
      * Localized WPS Add-in, Coming soon.


## Requirements

* WPS on Windows, Latest version
* WPS on Linux, Latest version.

## Access

* There are several steps to get WPS add-in (side-load in WPS)
* Visit [https://json-to-wps-workbook.wtsolutions.cn/publish.html](https://json-to-wps-workbook.wtsolutions.cn/publish.html) for detailed steps. (avalibale only in Simplified Chinese)


### Video Guide to Get add-in


Available only in Simplified Chinese.

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115644276153073&bvid=BV12LS2BaEBG&cid=34420558272&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

## Usage

* Prepare your JSON data
* In the [Conversion Settings](profeatures.md), select conversion mode etc.
* Load your JSON data (Choose one of the following two ways)
    1. Copy and Paste your JSON data in the text area, or
    2. Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing, max 20 files can be loaded at once.
* Click on Go button
* Your JSON data will be converted to WPS, and you can find one newly added sheet to your WPS.

### Video Guide to Use add-in (side-load in WPS)

Using WPS add-in is the same as using Excel add-in, refer to the following video guide.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nn3AIptQ-p8?si=4DSrC5wog7yEmPyO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Refer to the following video for a simple demo of using WPS add-in, available only in Simplified Chinese.

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115658553562052&bvid=BV1Ky2hB2EfB&cid=34486682667&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8772217510669640"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-8772217510669640"
     data-ad-slot="2653271427"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## JSON Data and Conversion Settings

Refer to [JSON Data and Conversion Settings](profeatures.md) for more details.


## Limitations
- Maximum 1000 objects (rows) per conversion
- Maximum 100 unique properties (columns) per dataset
- Arrays in values will be converted to strings in WPS
- Maximum 20 loaded local JSON files can be converted at once