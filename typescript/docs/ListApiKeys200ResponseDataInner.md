
# ListApiKeys200ResponseDataInner


## Properties

Name | Type
------------ | -------------
`object` | string
`id` | string
`name` | string
`permission` | string
`scopes` | Array&lt;string&gt;
`domainId` | string
`hint` | string
`createdAt` | string
`lastUsedAt` | string
`expiresAt` | string

## Example

```typescript
import type { ListApiKeys200ResponseDataInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "object": null,
  "id": null,
  "name": null,
  "permission": null,
  "scopes": null,
  "domainId": null,
  "hint": null,
  "createdAt": null,
  "lastUsedAt": null,
  "expiresAt": null,
} satisfies ListApiKeys200ResponseDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListApiKeys200ResponseDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


