# Moonemail Go

```sh
go get github.com/halyard-labs/moonemail-sdks/go@v0.1.0
```

```go
package main

import (
    "context"
    "log"
    "os"
    moonemail "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
    email, err := moonemail.New(os.Getenv("MOONEMAIL_API_KEY"))
    if err != nil { log.Fatal(err) }
    to := "recipient@example.com"
    body := moonemail.NewSendEmailRequest(
        "Acme <hello@your-verified-domain.com>",
        moonemail.StringAsSendEmailRequestTo(&to),
        "Your receipt",
    )
    body.SetText("Thanks for your order.")
    sent, response, err := email.EmailsAPI.SendEmail(context.Background()).
        SendEmailRequest(*body).IdempotencyKey("order-123-receipt").Execute()
    if response != nil { defer response.Body.Close() }
    if err != nil { log.Fatal(err) }
    log.Println(sent.Id)
}
```

`New` configures bearer authentication and a 30-second HTTP timeout. For custom
transport settings, use the generated `NewConfiguration` / `NewAPIClient`.
Each API call accepts a context. Arrays of recipients use
`ArrayOfStringAsSendEmailRequestTo(&recipients)`.

Generated APIs cover all 36 public operations. Inspect the returned HTTP status,
headers (including `Retry-After`) and error before retrying, and reuse the same
idempotency key and payload. No automatic send retries or hidden pagination.
