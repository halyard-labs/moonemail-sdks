
# ListWebhookDeliveries200ResponseDataInner


## Properties

Name | Type
------------ | -------------
`webhookId` | string
`eventId` | string
`eventType` | string
`emailId` | string
`attempt` | number
`statusCode` | number
`ok` | boolean
`durationMs` | number
`error` | string
`createdAt` | string

## Example

```typescript
import type { ListWebhookDeliveries200ResponseDataInner } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "webhookId": null,
  "eventId": null,
  "eventType": null,
  "emailId": null,
  "attempt": null,
  "statusCode": null,
  "ok": null,
  "durationMs": null,
  "error": null,
  "createdAt": null,
} satisfies ListWebhookDeliveries200ResponseDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListWebhookDeliveries200ResponseDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


