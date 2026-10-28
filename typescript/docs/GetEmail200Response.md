
# GetEmail200Response


## Properties

Name | Type
------------ | -------------
`id` | string
`messageId` | string
`to` | Array&lt;string&gt;
`from` | string
`createdAt` | string
`subject` | string
`bcc` | Array&lt;string&gt;
`cc` | Array&lt;string&gt;
`replyTo` | Array&lt;string&gt;
`lastEvent` | string
`scheduledAt` | string
`object` | string
`html` | string
`text` | string
`tags` | [Array&lt;GetEmail200ResponseTagsInner&gt;](GetEmail200ResponseTagsInner.md)

## Example

```typescript
import type { GetEmail200Response } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "messageId": null,
  "to": null,
  "from": null,
  "createdAt": null,
  "subject": null,
  "bcc": null,
  "cc": null,
  "replyTo": null,
  "lastEvent": null,
  "scheduledAt": null,
  "object": null,
  "html": null,
  "text": null,
  "tags": null,
} satisfies GetEmail200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetEmail200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


