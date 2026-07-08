# Web App (JSON-to-Excel Web App)

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/WebApp.html)

JSON-to-Excel by WTSolutions is a toolkit of tools which can convert JSON to Excel, both Flat and Nested JSON can be converted to Excel. It offers a full-scenario solution for "Converting JSON to Excel", including Excel add-ins, WPS add-ins, web applications, API service and MCP service.

* Web Based Solutions
     * <mark>Web App: Convert JSON to Excel directly in Web Browser.</mark> (<-- You are here)
     * [Excel add-in: Convert JSON to Excel in Excel, works with Excel environment seamlessly. ](ExcelAddIn.md)
     * [WPS add-in: Convert JSON to Excel in WPS, works with WPS environment seamlessly. ](WPSAddIn.md)
     * [API: Convert JSON to Excel in API by HTTPS POST request](API.md)
     * [MCP Server: Convert JSON to Excel in MCP Server](MCP.md)
* Localized Solutions
     
     * [Localized App: Convert JSON to Excel in Localized App, works without Internet Connection](LocalApp.md)
     * [Localized Excel Add-in, Convert JSON to Excel in Localized Excel, works without Internet Connection](LocalExcelAddIn.md)
     * Localized WPS Add-in, Coming soon.

## Requirements

* A web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge etc.
* A browser works on Windows, Mac, Linux, Android, iOS, etc.

## Access

* Open a web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge etc.
* Open the following URL in your web browser: <a href="https://s.wtsolutions.cn/json-to-excel.html" target="_blank">https://s.wtsolutions.cn/json-to-excel.html</a>

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

## Usage

* Prepare your JSON data
* In the [Conversion Settings](profeatures.md), select conversion mode etc.
* Load your JSON data (Choose one of the following two ways)
    1. Copy and Paste your JSON data in the text area, or
    2. Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing , max 20 files can be loaded at once.
* Click on Go button
* Your JSON data will be converted to Excel, and you can find a preview Excel appear at the bottom of the page.
* You can click on Download button to download the Excel file.

## JSON Data and Conversion Settings

Refer to [JSON Data and Conversion Settings](profeatures.md) for more details.

## Limitations
- Maximum 1000 objects (rows) per conversion
- Maximum 100 unique properties (columns) per dataset
- Arrays in values will be converted to strings in Excel
- Maximum 20 loaded local JSON files can be converted at once
