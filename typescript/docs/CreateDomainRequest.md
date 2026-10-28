
# CreateDomainRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`region` | string
`customReturnPath` | string
`openTracking` | boolean
`clickTracking` | boolean
`trackingSubdomain` | string
`tls` | string

## Example

```typescript
import type { CreateDomainRequest } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "region": null,
  "customReturnPath": null,
  "openTracking": null,
  "clickTracking": null,
  "trackingSubdomain": null,
  "tls": null,
} satisfies CreateDomainRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDomainRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


