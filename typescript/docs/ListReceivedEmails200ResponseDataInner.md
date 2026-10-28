
# ListReceivedEmails200ResponseDataInner


## Properties

Name | Type
------------ | -------------
`id` | string
`inboxId` | string
`from` | string
`to` | Array&lt;string&gt;
`subject` | string
`messageId` | string
`createdAt` | string
`status` | string
`quarantineReason` | string
`attachments` | [Array&lt;ListReceivedEmails200ResponseDataInnerAttachmentsInner&gt;](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md)
`expiresAt` | number
`authentication` | [ListReceivedEmails200ResponseDataInnerAuthentication](ListReceivedEmails200ResponseDataInnerAuthentication.md)

## Example

```typescript
import type { ListReceivedEmails200ResponseDataInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "inboxId": null,
  "from": null,
  "to": null,
  "subject": null,
  "messageId": null,
  "createdAt": null,
  "status": null,
  "quarantineReason": null,
  "attachments": null,
  "expiresAt": null,
  "authentication": null,
} satisfies ListReceivedEmails200ResponseDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListReceivedEmails200ResponseDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


