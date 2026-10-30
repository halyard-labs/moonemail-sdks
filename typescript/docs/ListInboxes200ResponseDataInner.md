
# ListInboxes200ResponseDataInner


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`address` | string
`status` | string
`createdAt` | string
`aliases` | Array&lt;string&gt;
`domainId` | string

## Example

```typescript
import type { ListInboxes200ResponseDataInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "address": null,
  "status": null,
  "createdAt": null,
  "aliases": null,
  "domainId": null,
} satisfies ListInboxes200ResponseDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListInboxes200ResponseDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


