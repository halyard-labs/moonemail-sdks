
# SendEmailRequest


## Properties

Name | Type
------------ | -------------
`from` | string
`to` | [SendEmailRequestTo](SendEmailRequestTo.md)
`subject` | string
`bcc` | [SendEmailRequestTo](SendEmailRequestTo.md)
`cc` | [SendEmailRequestTo](SendEmailRequestTo.md)
`replyTo` | [SendEmailRequestTo](SendEmailRequestTo.md)
`html` | string
`text` | string
`headers` | { [key: string]: string; }
`attachments` | [Array&lt;SendEmailRequestAttachmentsInner&gt;](SendEmailRequestAttachmentsInner.md)
`tags` | [Array&lt;SendEmailRequestTagsInner&gt;](SendEmailRequestTagsInner.md)
`scheduledAt` | string

## Example

```typescript
import type { SendEmailRequest } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "from": null,
  "to": null,
  "subject": null,
  "bcc": null,
  "cc": null,
  "replyTo": null,
  "html": null,
  "text": null,
  "headers": null,
  "attachments": null,
  "tags": null,
  "scheduledAt": null,
} satisfies SendEmailRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SendEmailRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


