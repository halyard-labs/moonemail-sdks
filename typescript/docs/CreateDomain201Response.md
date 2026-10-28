
# CreateDomain201Response


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`status` | string
`createdAt` | string
`region` | string
`object` | string
`openTracking` | boolean
`clickTracking` | boolean
`trackingSubdomain` | string
`customReturnPath` | string
`tls` | string
`capabilities` | [CreateDomain201ResponseCapabilities](CreateDomain201ResponseCapabilities.md)
`records` | [Array&lt;CreateDomain201ResponseRecordsInner&gt;](CreateDomain201ResponseRecordsInner.md)

## Example

```typescript
import type { CreateDomain201Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "status": null,
  "createdAt": null,
  "region": null,
  "object": null,
  "openTracking": null,
  "clickTracking": null,
  "trackingSubdomain": null,
  "customReturnPath": null,
  "tls": null,
  "capabilities": null,
  "records": null,
} satisfies CreateDomain201Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDomain201Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


