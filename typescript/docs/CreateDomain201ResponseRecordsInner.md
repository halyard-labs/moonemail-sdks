
# CreateDomain201ResponseRecordsInner


## Properties

Name | Type
------------ | -------------
`record` | string
`name` | string
`type` | string
`ttl` | string
`status` | string
`value` | string
`priority` | number

## Example

```typescript
import type { CreateDomain201ResponseRecordsInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "record": null,
  "name": null,
  "type": null,
  "ttl": null,
  "status": null,
  "value": null,
  "priority": null,
} satisfies CreateDomain201ResponseRecordsInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDomain201ResponseRecordsInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


