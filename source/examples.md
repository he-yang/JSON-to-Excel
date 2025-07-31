# 4. Examples

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/examples.html)

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
   

