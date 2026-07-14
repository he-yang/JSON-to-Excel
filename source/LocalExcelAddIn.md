# Local Excel Add-in (JSON-to-Excel Localized Excel Add-in)

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/LocalExcelAddIn.html)

JSON-to-Excel by WTSolutions is a toolkit of tools which can convert JSON to Excel, both Flat and Nested JSON can be converted to Excel. It offers a full-scenario solution for "Converting JSON to Excel", including Excel add-ins, WPS add-ins, web applications, API service and MCP service.

* Web Based Solutions
     * [Web App: Convert JSON to Excel directly in Web Browser.](WebApp.md)
     * [Excel add-in: Convert JSON to Excel in Excel, works with Excel environment seamlessly.](ExcelAddIn.md)
     * [WPS add-in: Convert JSON to Excel in WPS, works with WPS environment seamlessly. ](WPSAddIn.md)
     * [API: Convert JSON to Excel in API by HTTPS POST request](API.md)
     * [MCP Server: Convert JSON to Excel in MCP Server](MCP.md)
* Localized Solutions
     * [Localized App: Convert JSON to Excel in Localized App, works without Internet Connection](LocalApp.md)
     * <mark>Localized Excel Add-in, Convert JSON to Excel in Localized Excel, works without Internet Connection.</mark>(<-- You are here)
     * Localized WPS Add-in, Coming soon.

:::{note}
    Currently, Excel-to-JSON Localized Excel addin is in public test. 
    If you have difficulties using it, email he.yang@wtsolutions.cn
:::

## Requirements

### System Requirements

* Windows 10 or above
* MacOS 11 or above

### Excel Requirements
* Excel 2013 Service Pack 1 or later, 
* Excel 2016 for Mac, 
* Excel 2016 or later, 
* Office 365 etc.

## Download, Installation and Access

* For Windows User, please refer to [Usage Guide](./_static/Usage%20Guide-Windows-LocalExcelAddin.docx)
* For MacOS User, please refer to [Usage Guide](./_static/Usage%20Guide-MacOS-LocalExcelAddin.docx)


## Usage

* Prepare your JSON data
* In the [Conversion Settings](profeatures.md), select conversion mode etc.
* Load your JSON data (Choose one of the following two ways)
    1. Copy and Paste your JSON data in the text area, or
    2. Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing, max 20 files can be loaded at once.
* Click on Go button
* Your JSON data will be converted to Excel, and you can find one newly added sheet to your Excel.

### Video Guide to Use add-in (side-load in Excel)

<iframe width="560" height="315" src="https://www.youtube.com/embed/nn3AIptQ-p8?si=4DSrC5wog7yEmPyO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


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
- Arrays in values will be converted to strings in Excel
- Maximum 20 loaded local JSON files can be converted at once