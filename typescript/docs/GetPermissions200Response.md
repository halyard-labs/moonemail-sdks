
# GetPermissions200Response


## Properties

Name | Type
------------ | -------------
`permission` | string
`scopes` | Array&lt;string&gt;
`domainId` | string
`expiresAt` | string
`canManageApiKeys` | boolean
`billingRequiresOwner` | boolean

## Example

```typescript
import type { GetPermissions200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "permission": null,
  "scopes": null,
  "domainId": null,
  "expiresAt": null,
  "canManageApiKeys": null,
  "billingRequiresOwner": null,
} satisfies GetPermissions200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetPermissions200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


