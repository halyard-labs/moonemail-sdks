
# ListReceivedEmails200ResponseDataInnerAuthentication

Provider receipt verdicts; not sender-supplied headers. Older messages may omit this.

## Properties

Name | Type
------------ | -------------
`spf` | string
`dkim` | string
`dmarc` | string

## Example

```typescript
import type { ListReceivedEmails200ResponseDataInnerAuthentication } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "spf": null,
  "dkim": null,
  "dmarc": null,
} satisfies ListReceivedEmails200ResponseDataInnerAuthentication

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListReceivedEmails200ResponseDataInnerAuthentication
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


