
# GetDomainHealth200Response


## Properties

Name | Type
------------ | -------------
`checkedAt` | string
`sendingEnabled` | boolean
`metricsEnabled` | boolean
`sendingSuspended` | boolean
`bounce` | [GetDomainHealth200ResponseBounce](GetDomainHealth200ResponseBounce.md)
`complaint` | [GetDomainHealth200ResponseBounce](GetDomainHealth200ResponseBounce.md)

## Example

```typescript
import type { GetDomainHealth200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "checkedAt": null,
  "sendingEnabled": null,
  "metricsEnabled": null,
  "sendingSuspended": null,
  "bounce": null,
  "complaint": null,
} satisfies GetDomainHealth200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetDomainHealth200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


