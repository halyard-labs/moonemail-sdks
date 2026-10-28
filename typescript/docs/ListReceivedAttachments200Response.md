
# ListReceivedAttachments200Response


## Properties

Name | Type
------------ | -------------
`object` | string
`hasMore` | boolean
`data` | [Array&lt;ListReceivedEmails200ResponseDataInnerAttachmentsInner&gt;](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md)

## Example

```typescript
import type { ListReceivedAttachments200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "object": null,
  "hasMore": null,
  "data": null,
} satisfies ListReceivedAttachments200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListReceivedAttachments200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


