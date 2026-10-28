
# UpdateDomainRequest


## Properties

Name | Type
------------ | -------------
`openTracking` | boolean
`clickTracking` | boolean
`trackingSubdomain` | string
`tls` | string

## Example

```typescript
import type { UpdateDomainRequest } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "openTracking": null,
  "clickTracking": null,
  "trackingSubdomain": null,
  "tls": null,
} satisfies UpdateDomainRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateDomainRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


