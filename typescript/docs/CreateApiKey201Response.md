
# CreateApiKey201Response


## Properties

Name | Type
------------ | -------------
`object` | string
`id` | string
`token` | string
`hint` | string
`permission` | string
`scopes` | Array&lt;string&gt;
`expiresAt` | string

## Example

```typescript
import type { CreateApiKey201Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "object": null,
  "id": null,
  "token": null,
  "hint": null,
  "permission": null,
  "scopes": null,
  "expiresAt": null,
} satisfies CreateApiKey201Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateApiKey201Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


