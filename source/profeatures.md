# Pro Features

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/profeatures.html)

The JSON-to-Excel add-in offers a set of pro features that enhance the functionality of the add-in. These features are only available to users who have subscribed to the add-in.

## Subscription

7 days free trial, then you will be charged monthly at one of the following rates for the Pro Features. You can cancel your subscription at any time before the 7th day, and you will not be charged:
- USD US$2.66 / month,
- CNY ¥19.90 / month,
- EUR €2.36 / month,
- HKD HK$21.80 / month
- Your local currency, if Stripe supports it.

Each Pro Code can offer 10 devices to access Pro Features.After the 7 day trial period, you may cancel your subscription at any time, which will take effect at the end of your current billing cycle.

Each Pro Code is valid for both the Excel-to-JSON add-in and the JSON-to-Excel add-in provided by WTSolutions.

Subscribe through Stripe, here [https://buy.stripe.com/00gdQT2iz0Vp32E002](https://buy.stripe.com/00gdQT2iz0Vp32E002)

Payment method:
- Bank Card (Visa, Mastercard, American Express, JCB, 银联)
- Apple Pay (needs to open the above link using your Apple/IOS/Mac Device)
- Google Pay (needs to open the above link using your Google/Andriod Device)
- Link

For subscription terms, kindly refer to the [Terms of Use](termsofuse.md)

## Pro Code

Pro Code is the `email address` you used during the checkout process of the Excel-to-JSON add-in on Stripe. This code is required to access pro features.

## Pro Features


### No Ads

After a successful conversion with a valid Pro Code, starting from the next launch (you can shut down the add-in and then start it again), the add-in will no longer display ads. 
Ads will be displayed if you do not have a valid Pro Code, or if you do not have a valid subscription to the add-in.

> Note, If you still see ads displayed from time to time, try to make a conversion with a valid Pro Code, then restart the add-in.

### Nested Delimeter

The Nested Delimeter specifies how to handle nested objects in JSON. You can choose from:
- Dot (.) - Default
- Underscore (_)
- Forward slash (/)

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

The Max Depth setting controls how deep the add-in will process nested objects:
- Default: unlimited number of depths
- Acceptable Range: 1 ~ 20  (requires Pro feature)

Note: When Max Depth is set to a value between 1 to 20, you must use Nested JSON Mode.

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

### Load JSON File(s)

The Load JSON File(s) feature allows you to load multiple JSON files into the add-in, and then convert them to Excel sheets. This feature is only available to users who have subscribed to the add-in.

After each conversion, a report will be generated, which includes:
- The filename of selected JSON file(s)
- The conversion result (success or failure)
- The sheet name if success
- The error message if failure

Note: Max 20 files per conversion.

## More features

If you have subscribed, and would like to see more features, kindly please send us email at he.yang@wtsolutions.cn

## Aftersale services

You can contact us via email at he.yang@wtsolutions.cn for any questions or concerns. We will try our best to respond you within 24 hours, but not later than 72 hours. Please include your `Pro Code` in the email if your question is related to your subscription.
