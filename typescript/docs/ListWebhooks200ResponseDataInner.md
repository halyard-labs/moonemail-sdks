
# ListWebhooks200ResponseDataInner


## Properties

Name | Type
------------ | -------------
`object` | string
`id` | string
`endpoint` | string
`events` | Array&lt;string&gt;
`status` | string
`createdAt` | string
`signingSecret` | string

## Example

```typescript
import type { ListWebhooks200ResponseDataInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "object": null,
  "id": null,
  "endpoint": null,
  "events": null,
  "status": null,
  "createdAt": null,
  "signingSecret": null,
} satisfies ListWebhooks200ResponseDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListWebhooks200ResponseDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


