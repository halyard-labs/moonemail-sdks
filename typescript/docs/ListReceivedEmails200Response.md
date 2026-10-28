
# ListReceivedEmails200Response


## Properties

Name | Type
------------ | -------------
`object` | string
`hasMore` | boolean
`data` | [Array&lt;ListReceivedEmails200ResponseDataInner&gt;](ListReceivedEmails200ResponseDataInner.md)

## Example

```typescript
import type { ListReceivedEmails200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "object": null,
  "hasMore": null,
  "data": null,
} satisfies ListReceivedEmails200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListReceivedEmails200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


