# 6. JSON Data and Conversion Settings

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/profeatures.html)

JSON-to-Excel offers a set of pro features that enhance the functionality. These rules marked as [Pro Feature](pricing.md) are only available to users who have subscribed the tools.


## 6.1 JSON Data
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|❌|❌|

There are three ways to load JSON data:
- Copy and Paste your JSON data in the text area
- Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing [Pro Features](pricing.md), max 20 files can be loaded at once.
- Load JSON File(s) from Web URLs, for batch processing [Pro Features](pricing.md), max 20 URLs.
> Note, the JSON data shall meet the requirements listed in the below [Section Acceptable JSON format](profeatures.md#acceptable-json-format).

### Copy and Paste JSON data
Copy and Paste your JSON data in the text area, you may see JSON data preview below the text area.
> Note, the JSON data shall meet the requirements listed in the below [Section Acceptable JSON format](profeatures.md#acceptable-json-format).

### Load JSON File(s)

The Load JSON File(s) feature allows you to load multiple JSON files into JSON to Excel, and then convert them to Excel sheets. 

After each conversion, a report will be generated, which includes:
- The filename of selected JSON file(s)
- The conversion result (success or failure)
- The sheet name if success
- The error message if failure

> Note, Max 20 files per conversion.
> Note, the JSON data shall meet the requirements listed in the below Section Acceptable JSON format.

#### Load JSON File(s) video demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/DBd1LzD3HgA?si=jiBqCMlkY7YOBiMm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Load JSON File(s) from Web URLs

The Load JSON File(s) from Web URLs feature allows you to load multiple JSON files into JSON to Excel, and then convert them to Excel sheets. 

After each conversion, a report will be generated, which includes:
- The filename of selected URL(s)
- The conversion result (success or failure)
- The sheet name if success
- The error message if failure

> Note, Max 20 URLs per conversion.
> Note, the JSON data shall meet the requirements listed in the below Section Acceptable JSON format.


### Acceptable JSON format

#### Required Format

The input must be a valid JSON array containing objects. Each object in the array represents one row in the Excel output.

```json
[
    {"property1": "value1", "property2": "value2"},
    {"property1": "value3", "property2": "value4"}
]
```

#### JSON Format Schema

The JSON data must conform to one of the following structures:

1. **Array of Objects**:
   - Must be wrapped in square brackets `[]`
   - Must contain between 1 and 1000 items
   - Each item must be an object `{}` with 1-100 properties
   - Array cannot contain arrays, null values, strings, numbers, booleans, or empty objects

2. **Single Object**:
   - Must be wrapped in curly braces `{}`
   - Must contain between 1 and 100 properties
   - Cannot be an array, null value, string, number, boolean, or empty object

All objects can have additional properties beyond those defined in the schema.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "oneOf": [
    {
      "type": "array",
      "minItems": 1,
      "maxItems": 1000,
      "items": {
        "type": "object",
        "minProperties": 1,
        "maxProperties": 100,
        "additionalProperties": true
      },
      "not": {
        "contains": {
          "anyOf": [
            {
              "type": "array"
            },
            {
              "type": "null"
            },
            {
              "type": "string"
            },
            {
              "type": "number"
            },
            {
              "type": "boolean"
            },
            {
              "type": "object",
              "maxProperties": 0
            }
          ]
        }
      }
    },
    {
      "type": "object",
      "minProperties": 1,
      "maxProperties": 100,
      "additionalProperties": true,
      "not": {
        "anyOf": [
          {
            "type": "array"
          },
          {
            "type": "null"
          },
          {
            "type": "string"
          },
          {
            "type": "number"
          },
          {
            "type": "boolean"
          },
          {
            "type": "object",
            "maxProperties": 0
          }
        ]
      }
    }
  ]
}
```

#### Supported Value Types

- String: "text"
- Number: 123 , 45.67
- Boolean: true , false
- Null: null
    - will be converted to a blank cell in Excel
- Array: [1, 2, 3]
    - will be converted to string in Excel, as "[1,2,3]"
- Object: {"x": 1}
    - will be converted to string in Excel, if flat mode selected, as '{"x": 1}'
    - will be flattened if nested mode selected

### Valid and Invalid JSON Data Examples

Refer to [Examples](examples.md) for valid and invalid JSON data examples.

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

## 6.2 Conversion Settings

### Conversion Mode
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|❌|❌|

There are two conversion modes: Flat JSON Mode and Nested JSON Mode. Refer to [Examples](examples.md#output) for the difference between these two modes.


- Flat JSON Mode   
   - Use for simple JSON objects without nested structures
   - Each property becomes a column in Excel, property name as column name
- Nested JSON Mode
   - Use for JSON objects with nested structures
   - Nested properties are flattened using dot/underscore/doubleunderscore/slash delimiter [Pro Feature](pricing.md)
   - Unlimited depth converted by default. Customize max depth (1 to 20, or unlimited) of nested objects using Max Depth Nested setting using [Pro Features](pricing.md)

### Nested Delimeter
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|❌|❌|

The Nested Delimeter specifies how to handle nested objects in JSON. You can choose from:
- Dot (.) - Default
- Underscore (_) [Pro Feature](pricing.md)
- Double Underscore (__) [Pro Feature](pricing.md)
- Forward slash (/) [Pro Feature](pricing.md)

For example, with this JSON:

```json
[{
    "id": 1,
    "student": {
        "name": "Meimei",
        "familyname": "Han",
        "age": 12
    }
}, {
    "id": 2,
    "student": {
        "name": "Lily",
        "familyname": "Jaskson",
        "age": 15
    }
}]
```

Will be converted to Excel as:

Using Dot(.) as delimiter:
|id|student.name|student.familyname|student.age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

Using Underscore(_):
|id|student_name|student_familyname|student_age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

Using Forward Slash(/):
|id|student/name|student/familyname|student/age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

### Max Depth Nested
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|❌|❌|

The Max Depth setting controls how deep JSON to Excel will process nested objects:
- Default: unlimited number of depths
- Acceptable Range: 1 ~ 20  [Pro Feature](pricing.md)

> Note: When Max Depth is set to a value between 1 to 20, you must use Nested JSON Mode.

For example, with this JSON:

```json
[{
    "id": 1,
    "student": {
        "name": "Meimei",
        "contact": {
            "email": "meimei@school.com",
            "phone": "123-456-7890",
            "address": {
                "street": "123 School St",
                "city": "Beijing"
            }
        }
    }
}, {
    "id": 2,
    "student": {
        "name": "Lily",
        "contact": {
            "email": "lily@school.com",
            "phone": "098-765-4321",
            "address": {
                "street": "456 School Ave",
                "city": "Shanghai"
            }
        }
    }
}]
```

When Max Depth is set to 3, the 4th level nested objects (address) will be converted to string format. If there are the 5th, 6th, etc. levels nested objects, they will also be converted to string format.

The Excel output will look like:

Using Dot(.) as delimiter:
|id|student.name|student.contact.email|student.contact.phone|student.contact.address|
|---|---|---|---|---|
|1|Meimei|meimei@school.com|123-456-7890|{"street":"123 School St","city":"Beijing"}|
|2|Lily|lily@school.com|098-765-4321|{"street":"456 School Ave","city":"Shanghai"}|


## 4.3 No Ads
||[Web App](WebApp.md)|[Excel Add-in](ExcelAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|❌|❌|

If you have a valid subscription to JSON to Excel, you will not see ads after a successful conversion with a valid Pro Code.

Starting from the next launch (you can shut down JSON to Excel and then start it again), JSON to Excel will no longer display ads. 

Ads will be displayed if you do not have a valid Pro Code, or if you do not have a valid subscription to JSON to Excel.

> Note, If you still see ads displayed from time to time, try to make a conversion with a valid Pro Code, then restart JSON to Excel.


## 6.4 More features

If you have subscribed, and would like to see more features, kindly please send us email at he.yang@wtsolutions.cn

## 6.5 Pro Code

Pro Code is the `email address` you used during the checkout process of the JSON to Excel on Stripe or Paddle. This code is required to access pro features.


