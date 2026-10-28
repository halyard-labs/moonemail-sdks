
# ListEmailEvents200ResponseDataInnerData


## Properties

Name | Type
------------ | -------------
`bounce` | [ListEmailEvents200ResponseDataInnerDataBounce](ListEmailEvents200ResponseDataInnerDataBounce.md)
`click` | [ListEmailEvents200ResponseDataInnerDataClick](ListEmailEvents200ResponseDataInnerDataClick.md)
`failed` | [ListEmailEvents200ResponseDataInnerDataFailed](ListEmailEvents200ResponseDataInnerDataFailed.md)
`suppressed` | [ListEmailEvents200ResponseDataInnerDataFailed](ListEmailEvents200ResponseDataInnerDataFailed.md)

## Example

```typescript
import type { ListEmailEvents200ResponseDataInnerData } from 'moonemail'

// TODO: Update the object below with actual values
const example = {
  "bounce": null,
  "click": null,
  "failed": null,
  "suppressed": null,
} satisfies ListEmailEvents200ResponseDataInnerData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListEmailEvents200ResponseDataInnerData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


