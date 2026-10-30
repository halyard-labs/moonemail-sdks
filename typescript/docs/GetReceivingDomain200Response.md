
# GetReceivingDomain200Response


## Properties

Name | Type
------------ | -------------
`domainId` | string
`name` | string
`status` | string
`verifiedUntil` | number
`createdAt` | string
`records` | [Array&lt;GetReceivingDomain200ResponseRecordsInner&gt;](GetReceivingDomain200ResponseRecordsInner.md)

## Example

```typescript
import type { GetReceivingDomain200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "domainId": null,
  "name": null,
  "status": null,
  "verifiedUntil": null,
  "createdAt": null,
  "records": null,
} satisfies GetReceivingDomain200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetReceivingDomain200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


