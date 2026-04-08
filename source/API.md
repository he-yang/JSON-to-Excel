# API (JSON to Excel by HTTPS POST request)

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/API.html)

JSON-to-Excel by WTSolutions is a toolkit of tools which can convert JSON to Excel, both Flat and Nested JSON can be converted to Excel. It offers a full-scenario solution for "Converting JSON to Excel", including Excel add-ins, WPS add-ins, web applications, API service and MCP service.

* Web Based Solutions
     * [Web App: Convert JSON to Excel directly in Web Browser.](WebApp.md)
     * [Excel add-in: Convert JSON to Excel in Excel, works with Excel environment seamlessly. ](ExcelAddIn.md)
     * [WPS add-in: Convert JSON to Excel in WPS, works with WPS environment seamlessly. ](WPSAddIn.md)
     * <mark>API: Convert JSON to Excel in API by HTTPS POST request</mark> (<-- You are here)
* Localized Solutions
     * [Localized MCP Server: Convert JSON to Excel in MCP Server](MCP.md)
     * Localized App, Coming soon.
     * Localized Excel Add-in, Coming soon.
     * Localized WPS Add-in, Coming soon.


## Requirements

HTTPS post request tool, e.g. Postman, Curl, Python Requests, Javascript fetch, etc.
Make sure you properly handle CORS issues by setting up CORS headers.

## Access

Send `POST` request to access point `https://mcp2.wtsolutions.cn/json-to-excel-api` with required parameters described below in usage section. 

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

### Request Format

The API accepts POST requests with a `application/json` body containing one of the following parameter:

| Parameter | Type   | Required | Description                                                                 |
|-----------|--------|----------|-----------------------------------------------------------------------------|
| data      | string | No       | JSON data string to be converted to CSV. Must be a valid JSON array or object. |
| url       | string | No       | URL pointing to an JSON file. Either 'data' or 'url' must be provided |
| options   | object | Yes      | Optional configuration object for customizing the conversion process |

> Note: 
> - Provide either `data` or `url`, not both.
> - `options` is mandatory if you want to use custom conversion settings. 


#### Requirements on data and url

When sending `data`
> - Input data must be a valid JSON string. JSON schema available at [JSON Schema](profeatures.md#json-format-schema) and validator available at [JSON to Excel Web App](https://s.wtsolutions.cn/json-to-excel.html).
> - If the JSON is an array of objects, each object will be treated as a row in the CSV.
> - If the JSON is a single object, it will be converted into a CSV with key-value pairs.
> - The CSV will include headers based on the keys in the JSON objects.
> - This tool returns CSV-formatted data that can be easily converted/imported to Excel.

When sending `url`
> - The url should be publicly accessible.
> - The JSON file should be in .json format.
> - The JSON file should contain a valid JSON array or object. JSON schema available at [JSON Schema](profeatures.md#json-format-schema) and validator available at [JSON to Excel Web App](https://s.wtsolutions.cn/json-to-excel.html).
> - If the JSON is an array of objects, each object will be treated as a row in the CSV.
> - If the JSON is a single object, it will be converted into a CSV with key-value pairs.
> - This tool returns CSV-formatted data that can be easily converted/imported to Excel.

### ptions Object

The options object can contain the following properties:

| Property | Type  |Default | Description                                                                 |
|----------|-------|--------|-----------------------------------------------------------------------------|
| proCode  | string| ""     | Pro Code for Pro Version JSON to Excel subscription. |
|jsonMode| string | “flat”| Format mode for JSON output: “nested”, or “flat”|
|delimiter| string | “.” | Delimiter character for nested JSON keys when using jsonMode: “nested”, acceptable delimiters are “.”, “_”, “__”, “/”.|
|maxDepth|string| "unlimited"| Maximum depth for nested JSON objects when using jsonMode: “nested”. For maxDepth, "unlimited", "1" ~ "20" acceptable.|

Note:
> - Pro Code is optional. If you do not have a valid [Pro Code](pricing.md), you can only process up to 6 rows of data.
> - Detailed conversion rules can be found in [Conversion Settings](profeatures.md).

### Response Format
The API returns a JSON object with the following structure:

| Field   | Type    | Description                                                                 |
|---------|---------|-----------------------------------------------------------------------------|
| isError | boolean | Indicates if there was an error processing the request                      |
| msg     | string  | 'success' or error description                                              |
| data    | string  | Converted CSV data string, '' if there was an error. This CSV data can be easily imported into Excel.                                      |


### Example

#### Example Request with 'data'

Request:

```json
{
     "data": "[{\"name\":\"John\",\"contact\":{\"email\":\"john@example.com\",\"phone\":\"1234567890\"}},{\"name\":\"Jane\",\"contact\":{\"email\":\"jane@example.com\",\"phone\":\"0987654321\"}}]",
     "options":{
          "proCode": "input your Pro Code here",
          "jsonMode": "nested",
          "delimiter": ".",
          "maxDepth": "unlimited"
     }
}
```

Response:

```json
{
     "isError": false,
     "data": "name,contact.email,contact.phone\nJohn,john@example.com,1234567890\nJane,jane@example.com,0987654321",
     "msg": "success"
}
```


#### Example Error Response
```json
{
     "isError": true,
     "msg": "Invalid JSON format",
     "data": ""
}
```

### Data Type Handling

The API automatically handles different data types in JSON:

- **Numbers**: Converted to numeric values in CSV
- **Booleans**: Converted to 'true'/'false' strings
- **Strings**: Escaped and quoted if necessary
- **Arrays**: Converted to JSON.stringify array string
- **Objects**: Converted to JSON.stringify object string


## Error Handling
The API returns descriptive error messages for common issues:
- `Invalid JSON format`: When input data is not a valid JSON string
- `Empty JSON data`: When input data is an empty JSON string
- `Network Error when fetching file`: When there's an error downloading the file from the provided URL
- `File not found`: When the file at the provided URL cannot be found
- `Server Internal Error`: When an unexpected error occurs
- `Max 6 rows processed, upgrade to Pro to process more data`: When the Pro Code is not provided or invalid, and the input data exceeds 6 rows