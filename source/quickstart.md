
# 1. Introduction

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/quickstart.html)

JSON to Excel is a **Microsoft Excel add-in** or **Web Application** which can convert JSON to Excel. Both Flat/Nested JSON can be converted.

# 2. Requirements

Option 1. Load JSON to Excel in Web Browser
* A web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.

Option 2. Side-load JSON to Excel in Excel (recommended)
* Excel 2013 Service Pack 1 or later, 
* Excel 2016 for Mac, 
* Excel 2016 or later, 
* Excel Online, 
* Office 365 etc.

# 3. Quick Start
This quick start is for v 3.0.0

## 3.1 (Side-)Load JSON to Excel

Option 1. Load JSON to Excel in Web Browser
* Open a web browser that supports JavaScript, such as Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.
* Open the following URL in your web browser: <a href="https://s.wtsolutions.cn/json-to-excel.html" target="_blank">https://s.wtsolutions.cn/json-to-excel.html</a>


Option 2. Side-load JSON to Excel in Excel (recommended)
* Open a new datasheet in Excel 2013/2016 or Excel Online or Office 365.
* **Home** Tab or **Insert** Tab > Add-ins
* In the search box, type in "JSON to Excel"
* Follow the instructions on the screen to install the add-in, and you will see an button JSON-to-Excel added to your **Home** Tab.
* **Home** Tab > JSON to Excel > Convert
* Now you are ready to use this add-in.

### Video Guide to Get add-in (side-load in Excel)

<iframe width="560" height="315" src="https://www.youtube.com/embed/U3uQQ9i6IGs?si=kZFaGT89tT3wk21C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 3.2 Use JSON to Excel
* Prepare your JSON data
* In the settings box, select conversion mode etc.
* Load your JSON data (Choose one of the two ways)
    1. Copy and Paste your JSON data in the text area, or
    2. Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing (Pro Features), max 20 files can be loaded at once.
* Click on Go button

### Limitations
- Maximum 1000 objects (rows) per conversion
- Maximum 100 unique properties (columns) per dataset
- Arrays in values will be converted to strings in Excel
- Maximum 20 loaded local JSON files can be converted at once (Pro Feature)



### Video Guide to Use add-in (side-load in Excel)

<iframe width="560" height="315" src="https://www.youtube.com/embed/nn3AIptQ-p8?si=4DSrC5wog7yEmPyO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 3.3 Conversion Settings

### Conversion Mode
There are two conversion modes: Flat JSON Mode and Nested JSON Mode.

> refer to Examples below first to assit you understand the two modes

- Flat JSON Mode   
   - Use for simple JSON objects without nested structures
   - Each property becomes a column in Excel
- Nested JSON Mode
   - Use for JSON objects with nested structures
   - Nested properties are flattened using dot/underscore/doubleunderscore/slash delimiter
   - Unlimited depth converted by default. Customize max depth (1 to 20, or unlimited) of nested objects using Max Depth Nested setting using [Pro Features](profeatures.md)

### Nested Delimiter

The delimiter used to separate nested properties in the Excel output.

- Dot (.)
- Underscore (_) [Pro Feature]
- Double Underscore (__) [Pro Feature]
- Slash (/) [Pro Feature]

### Max Depth Nested

The maximum depth of nested objects to be flattened.

- Unlimited
- 1 to 20 [Pro Feature]



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

## 3.4 Load JSON Data

There are two ways to load JSON data:
- Copy and Paste your JSON data in the text area
- Click on the Load JSON File(s) file selector, and select your JSON file(s) from your local computer, for batch processing (Pro Features), max 20 files can be loaded at once.

### Acceptable JSON format
#### Required Format
The input must be a valid JSON array containing objects. Each object in the array represents one row in the Excel output.

```json
[
    {"property1": "value1", "property2": "value2", ...},
    {"property1": "value3", "property2": "value4", ...}
]
```

#### JSON Format Rules
- Must be wrapped in square brackets [], as array
- Must contain at least one object {}
- Each object must have at least one property

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



# 4. Examples

## 4.1 Valid JSON example
```json
// simple, one flat object
{"name": "John", "age": 30}

// Simple, flat objects
[
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

// Objects with different properties
[
    {"name": "John", "age": 30},
    {"name": "Jane", "city": "New York"}
]

// Objects with nested structures (use Nested JSON Mode)
// Customize delimiter (dot, underscore, slash) using Nested Delimeter setting using Pro Features
// Customize max depth (1 to 20, or unlimited) of nested objects using Max Depth Nested setting using Pro Features
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
## 4.2 Invalid JSON Examples

```json
// Not wrapped in array
{"name": "John"},{"name": "Lily", "age": 30}

// Empty array
[]

// Array with non-object elements
[1, 2, 3]
["a", "b", "c"]

// Array with empty object
[{}]

// Array with null
[null]

// Array with mixed types
[{"name": "John"}, "text"]

```

## 4.3 Conversion Examples

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

   - Customize delimiter (dot, underscore, double underscore, slash) using Nested Delimeter setting using [Pro Features](profeatures.md)
   - Customize max depth (1 to 20, or unlimited) of nested objects using Max Depth Nested setting using [Pro Features](profeatures.md)
   


# 5. Errors

## 5.1 Invalid JSON

When JSON to Excel pops up with an error alert of invalid JSON, it means the JSON is not meeting the JSON schema. 

### Addin Checking
* The addin will check if your JSON data matches the abovementioned acceptable JSON format required. If error, an error message will be displayed.


## 5.2 Too many columns

When you have a pop up of too many columns error, it means you have too many key-value pairs in one single element.

One single element has two key-value pairs, 
```
    {
        "name":"Lily",
        "age":22
    }
```
and the addin now can accept no more than 100 key-value pairs.
