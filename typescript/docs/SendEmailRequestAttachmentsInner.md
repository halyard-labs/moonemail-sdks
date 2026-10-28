
# SendEmailRequestAttachmentsInner


## Properties

Name | Type
------------ | -------------
`filename` | string
`content` | string
`path` | string
`contentType` | string
`contentId` | string

## Example

```typescript
import type { SendEmailRequestAttachmentsInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "filename": null,
  "content": null,
  "path": null,
  "contentType": null,
  "contentId": null,
} satisfies SendEmailRequestAttachmentsInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SendEmailRequestAttachmentsInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


