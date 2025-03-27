# JSON-to-Excel

JSON to Excel is a Microsoft Excel add-in which can convert JSON to Excel within Excel Environment, both Flat and Nested JSON mode are supported.

## Documentation
[https://json-to-excel.wtsolutions.cn](https://json-to-excel.wtsolutions.cn)


## Requirements
This add-in works in: Excel 2013 Service Pack 1 or later, Excel 2016 for Mac, Excel 2016 or later, Excel Online, Excel for Mac, Office 365 etc.

## Get add-in
* Open a new datasheet in Excel 2013/2016 or Excel Online or Office 365.
* **Home** Tab or **Insert** Tab > Add-ins
* In the search box, type in "JSON-to-Excel"
* Follow the instructions on the screen to install the add-in, and you will see an button JSON-to-Excel added to your **Home** Tab.
* **Home** Tab > JSON to Excel > Convert
* Now you are ready to use this add-in.

## Use add-in
* Prepare your JSON data
* Fill the text area of JSON-to-Excel with your JSON data
* Select conversion mode , and click on Go button


## Conversion Examples

### Sample JSON to Excel

#### Input
```json
[
    {
        "name": "John",
        "contact": {
            "email": "john@example.com",
            "phone": "1234567890"
        }
    },
    {
        "name": "Jane",
        "contact": {
            "email": "jane@example.com",
            "phone": "0987654321"
        }
    }
]

```
#### Output
> with Flat JSON mode

|name|contact|
|--|--|
|John|{"email":"john@example.com","phone":"1234567890"}|
|Jane|{"email":"jane@example.com","phone":"0987654321"}|

> with Nested JSON mode

|name|contact.email|contact.phone|
|--|--|--|
|John|john@example.com|1234567890|
|Jane|jane@example.com|987654321|


## Documentation
[https://json-to-excel.wtsolutions.cn](https://json-to-excel.wtsolutions.cn)
